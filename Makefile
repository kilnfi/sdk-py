# This makefile is meant to be used locally to rebuild the automatic
# SDK from an OpenAPI spec. For now it's not fully CI-ed which is fine
# considering we are at the early stages here and it may evolve in
# many directions.

TMP_DIR=/tmp/kiln-openapi
TARGET_SDK=kiln_connect/openapi_client

all:

regenerate: kiln_connect

kiln_connect:
	rm -rf $(TMP_DIR) && mkdir -p $(TMP_DIR)
	openapi-generator generate -i ./specs/openapi.yaml -g python-nextgen -o $(TMP_DIR) -c specs/generator.yaml -t specs/templates --package-name kiln_connect.openapi_client
	rm -rf $(TARGET_SDK)
	cp -R $(TMP_DIR)/kiln_connect/openapi_client $(TARGET_SDK)


.PHONY: kiln_connect
