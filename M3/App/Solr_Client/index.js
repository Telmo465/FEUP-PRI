const express = require('express');
const app = express();
const cors = require("cors");
var SolrNode = require('solr-node');
//require('log4js').getLogger('solr-node').level = 'DEBUG';

var client = new SolrNode({
    host: '127.0.0.1',
    port: '8983',
    core: 'imdb_movies',
    protocol: 'http'
});

port = process.argv[2] || 5001;

app.use(cors());
app.use(express.json());

app.listen(port, () => {
    console.log('port running at port number : 5001')
})

app.get('/' , (req,res) => {
    res.send('hey solr!')
})

app.post('/search' , async (req, res) => {

    let query = req.body.query
    let op = req.body.op
    let fl = req.body.fl
    let fq = req.body.fq
    let sort = req.body.sort

    var objQuery = client.query()
                        .q(query)
                        .qop(op)
                        .fl(fl)
                        .fq(fq)
                        .sort("desc")
                        .start(0)
                        .rows(10)
                        
    
    client.search(objQuery, function (err, result) {

        if (err) {
           console.log(err);
           res.status(201).send("Error catching the information from solr")
           return;
        }
        console.log(result.response)
        res.json(result.response.docs)
     });
})