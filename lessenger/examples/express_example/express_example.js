/*
To run:
    (from this directory)
    install requirements:
        make sure you have an npm and nodejs install
        $ npm install
    run server:
        $ npm start
*/
const express = require('express');
const formidable = require('express-formidable');

const app = express();

// middleware for parsing form/multipart requests
app.use(formidable());

app.post('/chat/messages', function (req, res) {
    console.log(req.fields);
    res.set('Access-Control-Allow-Origin', '*');
    res.send({});
})

app.listen(9000, function () {
  console.log('App Started');
})
