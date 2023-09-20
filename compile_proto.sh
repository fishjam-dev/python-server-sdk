#!/bin/bash

# Terminate on errors
set -e


printf "Synchronising submodules... "
git submodule sync --recursive >> /dev/null
git submodule update --recursive --remote --init >> /dev/null
printf "DONE\n\n"

files=$(find protos/jellyfish -name "*.proto")

printf "Compiling:\n"
count=1
total=${#files[@]}
for file in $files; do
  printf "Compile file %s %s ... " $count $file
  protoc --python_out=./jellyfish/ $file
  printf "DONE\n"
  count=$(($count + 1))
done

autopep8 -ir jellyfish/protos