#!/bin/bash

precreate-core courses

# Start Solr in background mode so we can use the API to upload the schema
solr start

# Schema definition via API
bin/post -c courses -url http://localhost:8983/solr/courses/schema /data/schema.csv

# Populate collection
bin/post -c courses /data/final.csv

# Restart in foreground mode so we can access the interface
solr restart -f
