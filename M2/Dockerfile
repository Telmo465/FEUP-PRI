FROM solr:8.10

COPY final.csv /data/final.csv

COPY schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
