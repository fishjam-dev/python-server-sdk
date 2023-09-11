#!/bin/bash

pylint --rcfile=pylintrc --ignore-paths jellyfish/openapi_client/ jellyfish tests
