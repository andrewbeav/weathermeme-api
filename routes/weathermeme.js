var express = require('express');
var router = express.Router();

var path = require('path');

var PythonShell = require('python-shell');
var fs = require('fs');

router.get('/meme/:image', function(req, res, next) {
  let imageName = req.params.image;

  res.sendFile(path.join(__dirname, '../res/weathermeme/memes/' + imageName));
});

router.get('/api', function(req, res, next) {
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
    pythonPath: '/usr/bin/python',
    scriptPath: './weathermeme_engine',
    args: [apiKey, lat, lon]
  }

  var pyshell = new PythonShell('weathermeme.py', pythonShellOptions);

  var weathermemeString;

  pyshell.on('message', function(message) {
    weathermemeString = message;
  });

  pyshell.end(function(err) {
    if (err) res.send(err); // TODO more specific error checking
    else {
      res.send(weathermemeString);
    }
  });
});

module.exports = router;
