const owm_appid = '5f0dabe0a94eb1d907d7a79ff7562b93';

$(function() {
  navigator.geolocation.getCurrentPosition(updateMeme, function() {
    console.log("Error getting location");
  });
});

function updateMeme(position) {
  let apiString = 'http://andrewbevelhymer.com/weathermeme/api/?owm_appid='+owm_appid+'&lat='+position.coords.latitude+'&lon='+position.coords.longitude
  $.getJSON(apiString, function(data) {
    console.log(data.meme_location);
    $('#meme').attr('src', data.meme_location);
    $('#locationLabel').html(data.weather_info.name);
  });
}
