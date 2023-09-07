rm -rf openapi
openapi-generator-cli generate \
    -i https://raw.githubusercontent.com/jellyfish-dev/jellyfish/openapi-generator-compatibility/openapi.yaml \
    -g python \
    -t templates \
    -o openapi \
    --package-name openapi_client