#!/bin/bash

# Terminate on errors
set -e


printf "Synchronising submodules... "
git submodule sync --recursive >> /dev/null
git submodule update --recursive --remote --init >> /dev/null
printf "DONE\n\n"

files=$(find protos/jellyfish -name "*.proto")

printf "Compiling files:\n"

for file in $files; do
  printf "* $file\n"
done

protoc -I . --python_betterproto_out=jellyfish/_protos $files
