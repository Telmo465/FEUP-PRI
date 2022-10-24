FROM solr:8.10

COPY final.csv /data/final.csv

COPY field_title_type.json /data/field_title_type.json

COPY startup.sh /scripts/startup.sh

RUN bin/post -c courses /data/final.csv

ENTRYPOINT ["/scripts/startup.sh"]
