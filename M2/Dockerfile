FROM solr:8.10

COPY final_lol.csv /data/final_lol.csv

COPY schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
