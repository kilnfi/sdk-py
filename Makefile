# This makefile is meant to be used locally to rebuild the automatic
# SDK from an OpenAPI spec. For now it's not fully CI-ed which is fine
# considering we are at the early stages here and it may evolve in
# many directions.

LOCAL_IMAGE=openapi-generator
TMP_DIR=tmp/kiln-openapi
TARGET_SDK=kiln_connect/openapi_client
SPEC_SOURCE=https://docs.api.devnet.kiln.fi/openapi.specs.yaml

all:

regenerate: kiln_connect

specs/openapi.yaml:
	wget $(SPEC_SOURCE) -O $@

clean_specs:
	rm -f specs/openapi.yaml

kiln_connect: specs/openapi.yaml
	# Need sudo here as docker may output as root.
	sudo rm -rf $(TMP_DIR) && mkdir -p $(TMP_DIR)

	docker run --rm -v "${PWD}:/local" ${LOCAL_IMAGE} generate \
	    -c /local/specs/generator.yaml -t /local/specs/templates --package-name kiln_connect.openapi_client \
	    -i /local/specs/openapi.yaml -g python-nextgen -o /local/${TMP_DIR}

	rm -rf $(TARGET_SDK)
	cp -R $(TMP_DIR)/kiln_connect/openapi_client $(TARGET_SDK)
	mv ${TARGET_SDK}/docs/* docs

upgrade: clean_specs kiln_connect

.PHONY: kiln_connect clean_specs
