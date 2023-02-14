# This makefile is meant to be used locally to rebuild the automatic
# SDK from an OpenAPI spec. For now it's not fully CI-ed which is fine
# considering we are at the early stages here and it may evolve in
# many directions.

TMP_DIR=/tmp/kiln-openapi
TARGET_SDK=openapi_client

all:

regenerate: openapi_client

openapi_client:
	rm -rf $(TMP_DIR) && mkdir -p $(TMP_DIR)
	openapi-generator generate -i ./specs/openapi.yaml -g python -o $(TMP_DIR)/openapi_client -c specs/generator.yaml
	rm -rf $(TARGET_SDK)
	cp -R $(TMP_DIR)/openapi_client/openapi_client $(TARGET_SDK)


.PHONY: openapi_client
