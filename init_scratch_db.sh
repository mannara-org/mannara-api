#!/usr/bin/env bash

# initializaing the DB
dropdb -U postgres --if-exists scratch
createdb -U postgres scratch

psql -U postgres -d scratch -f $1
