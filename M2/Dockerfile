FROM solr:8.10

COPY meic_courses.json /data/meic_courses.json

COPY simple_schema.json /data/simple_schema.json

COPY field_title_type.json /data/field_title_type.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
