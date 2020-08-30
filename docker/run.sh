#!/usr/bin/env bash
set -e
cd $(dirname $0)

docker-compose build python
docker-compose run --rm python $@
