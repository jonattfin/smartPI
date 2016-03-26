var fs = require('fs');
var file = 'smartPi.db';
var exists = fs.existsSync(file);

var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database(file);

db.serialize(function() {
    if (!exists) {
        // create temperatures table
        db.run("CREATE TABLE temperatures(" +
            "id INT PRIMARY_KEY, " +
            "dt DATETIME DEFAULT CURRENT_TIMESTAMP, " +
            "value REAL NOT NULL)");

        // create luminosities table
        db.run("CREATE TABLE luminosities(" +
            "id INT PRIMARY_KEY, " +
            "dt DATETIME DEFAULT CURRENT_TIMESTAMP, " +
            "value REAL NOT NULL)");

        // create humidities table
        db.run("CREATE TABLE humidities(" +
            "id INT PRIMARY_KEY, " +
            "dt DATETIME DEFAULT CURRENT_TIMESTAMP, " +
            "value REAL NOT NULL)");

        db.run("CREATE TABLE colors(" +
            "id INT PRIMARY_KEY, " +
            "name TEXT NOT NULL)");

        var colors = ['red', 'blue', 'yellow', 'green'];

        for (var i = 0; i < colors.length; i++) {
            db.run("INSERT INTO colors(name) VALUES(?)", colors[i]);
        }

        // create leds table
        db.run("CREATE TABLE leds(" +
            "id INT PRIMARY_KEY, " +
            "color_id INT, " +
            "dt DATETIME DEFAULT CURRENT_TIMESTAMP, " +
            "FOREIGN KEY(color_id) REFERENCES colors(id))");
    }
});

db.close();
