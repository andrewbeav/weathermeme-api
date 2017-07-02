const owm_appid = '5f0dabe0a94eb1d907d7a79ff7562b93';

$(function() {
  navigator.geolocation.getCurrentPosition(updateMeme, function() {
    console.log("Error getting location");
  });
});

function updateMeme(position) {
  $.getJSON('http://andrewbevelhymer.com/weathermeme/api/?owm_appid='+owm_appid+'&lat='+position.coords.latitude+'&lon='+position.coords.longitude, function(data) {
    console.log('data: ' + data);
  });
}
