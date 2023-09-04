rm -rf jellyfish/openapi_client
openapi-generator-cli generate \
    -i https://raw.githubusercontent.com/jellyfish-dev/jellyfish/openapi-generator-compatibility/openapi.yaml \
    -g python \
    -t templates \
    --package-name jellyfish_openapi_client \
    -o jellyfish/openapi_client 