docker build . -t meic_solr
docker run -p 8983:8983 meic_solr