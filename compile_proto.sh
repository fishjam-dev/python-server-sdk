#!/bin/bash

# Terminate on errors
set -e


printf "Synchronising submodules... "
git submodule sync --recursive >> /dev/null
git submodule update --recursive --remote --init >> /dev/null
printf "DONE\n\n"

server_file="./protos/jellyfish/server_notifications.proto"
printf "Compiling: file $server_file"
protoc -I . --python_betterproto_out=./jellyfish/_protos $server_file
printf "\tDONE\n"

peer_file="./protos/jellyfish/peer_notifications.proto"
printf "Compiling: file $peer_file"
protoc -I . --python_betterproto_out=./tests/support/protos $peer_file
printf "\tDONE\n"
