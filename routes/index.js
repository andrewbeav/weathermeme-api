var express = require('express');
var router = express.Router();

var PythonShell = require('python-shell');
var fs = require('fs');

/* GET home page. */
router.get('/', function(req, res, next) {
  var apiKey, lat, lon;
  if (req.query.owm_appid) {
    apiKey = req.query.owm_appid;
  } else {
    res.send("Need Api Key");
  }
  if (req.query.lat && req.query.lon) {
    lat = req.query.lat;
    lon = req.query.lon;
  } else {
    res.send("Need location");
  }

  var pythonShellOptions = {
    mode: 'text',
    pythonPath: '/usr/bin/python2',
    scriptPath: './weathermeme_engine',
    args: [apiKey, lat, lon]
  }

  var pyshell = new PythonShell('weathermeme.py', pythonShellOptions);

  var weathermemeJsonString;

  pyshell.on('message', function(message) {
    console.log(message);
    weathermemeJsonString = message;
    fs.writeFile('weathermeme_result.json', weathermemeJsonString, function(err) {
  });

  pyshell.end(function(err) {
    if (err) res.send('Something went wrong. Check the paramaters'); // TODO more specific error checking
    else {
      if (err) return console.log(err);

      res.send(require('../weathermeme_result.json'));
    }
  });
});

module.exports = router;
