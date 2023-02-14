TMP_DIR=/tmp/kiln-openapi
TARGET_SDK=openapi_client

all:

regenerate: openapi_client

openapi_client:
	rm -rf $(TMP_DIR) && mkdir -p $(TMP_DIR)
	openapi-generator generate -i ./openapi.yaml -g python -o $(TMP_DIR)/openapi_client --additional-properties=generateSourceCodeOnly=true,disallowAdditionalPropertiesIfNotPresent=false,projectName=KilnApi
	rm -rf $(TARGET_SDK)
	mv $(TMP_DIR)/openapi_client/openapi_client $(TARGET_SDK)
	rm -rf $(TMP_DIR)


.PHONY: openapi_client
