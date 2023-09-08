#!/bin/bash

rm -rf openapi
openapi-generator-cli generate \
    -i https://raw.githubusercontent.com/jellyfish-dev/jellyfish/openapi-generator-compatibility/openapi.yaml \
    -g python \
    -o openapi \
    --package-name openapi_client \
    --global-property apis,models,modelTests=false,supportingFiles
    
rm -rf openapi/{docs,test,.github,.openapi-generator,.gitignore,.gitlab-ci.yml,.travis.yml,.openapi-generator-ignore,git_push.sh,README.md,setup.cfg,test-requirements.txt,tox.ini}
