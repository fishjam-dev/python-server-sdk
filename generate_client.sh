#!/bin/bash

rm -rf jellyfish/openapi_client
openapi-generator-cli generate \
    -i https://raw.githubusercontent.com/jellyfish-dev/jellyfish/main/openapi.yaml \
    -g python \
    -o . \
    -t templates \
    --package-name jellyfish.openapi_client \
    --global-property apis,models,modelTests=false,modelDocs=false,apiDocs=false
