#!/bin/bash

TMP_DIR="openapi_client_generated"
PACKAGE_NAME="_openapi_client"

openapi-generator-cli generate \
    -i https://raw.githubusercontent.com/jellyfish-dev/jellyfish/main/openapi.yaml \
    -g python \
    -o $TMP_DIR \
    -t templates \
    --package-name jellyfish.$PACKAGE_NAME \
    --global-property apis,models,modelTests=false,apiTests=false,modelDocs=false,apiDocs=false,supportingFiles \
    --additional-properties useOneOfDiscriminatorLookup=true &&
rm -rf jellyfish/$PACKAGE_NAME
mv $TMP_DIR/jellyfish/$PACKAGE_NAME jellyfish/$PACKAGE_NAME
rm -rf $TMP_DIR
