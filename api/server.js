'use strict';

// grab the packages we need
var express = require('express');
var app = express();

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

var port = process.env.PORT || 8080;

var file = 'smartPi.db';
var sqlite3 = require('sqlite3').verbose();

// routes will go here
app.get('/api', function(req, res) {
    var table_name = req.query.table_name;

    var db = new sqlite3.Database(file);
    var query = "SELECT dt, value FROM " + table_name;

    var from = req.query.from;
    var to = req.query.to;
    if (from && to) {
        query += " WHERE dt BETWEEN " + "'" + from + "'" + " AND " + "'" + to + "'";
    }

    db.all(query, function(err, rows) {
        res.json(rows);
        db.close();
    });
});

app.post('/api', function(req, res) {
    var table_name = req.body.table_name;
    var value = req.body.value;

    var db = new sqlite3.Database(file);

    try {
        db.run("INSERT INTO " + table_name + "(value) VALUES(?)", value);
    } catch (e) {

    } finally {
        db.close();
        res.end();
    }
});

app.get('/api/leds', function(req, res) {
    var table_name = "leds";
    var color = req.query.color;
    var from = req.query.from;
    var to = req.query.to;

    var db = new sqlite3.Database(file);
    var query = "SELECT dt FROM " + table_name;

    if (from && to) {
        query += " WHERE dt BETWEEN " + "'" + from + "'" + " AND " + "'" + to + "'";
        query += " AND color_id = " + color + "";
    } else {
        query += " WHERE color_id = " + color + "";
    }

    db.all(query, function(err, rows) {
        res.json(rows);
        db.close();
    });
});

app.post('/api/leds', function(req, res) {
    var table_name = "leds";
    var color = req.body.color;

    var db = new sqlite3.Database(file);

    try {
        db.run("INSERT INTO " + table_name + "(color_id) VALUES(?)", color);
    } catch (e) {

    } finally {
        db.close();
        res.end();
    }
});

// start the server
app.listen(port);
console.log('Server started! At http://localhost:' + port);
