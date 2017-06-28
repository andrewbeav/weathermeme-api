var express = require('express');
var router = express.Router();

var exec = require('child_process').exec;

/* GET home page. */
router.get('/', function(req, res, next) {
  console.log('Got a get request');
  var apiKey = req.query.owm_appid;
  var lat = req.query.lat;
  var lon = req.query.lon;

  var cmd = 'python2 weathermeme_engine/weathermeme.py ' + apiKey + " " + lat + " " + lon;
  console.log(cmd);
  exec(cmd);
  console.log('executing...')
  var weathermemeJson = require('../weathermeme_engine/weathermeme_result.json');
  console.log(weathermemeJson);
  res.send(weathermemeJson);
});

module.exports = router;
