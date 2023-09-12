#!/bin/bash

pylint --rcfile=pylintrc --ignore-paths jellyfish/_openapi_client/ jellyfish tests
