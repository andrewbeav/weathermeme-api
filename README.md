# Weathermeme API

## To Use:
* Make sure you have npm installed, then run
<code>
  npm install
</code>

To start the server:
<code>
  node server.js
</code>

To access the server go to localhost:3000 on your browser. The api is accessed at /weathermeme/api/

## The code
The interesting bits of code are in weathermeme_engine, that's where it determines what meme to use

## The API
server.js is the starting point for the server. The actual route for accessing the api is routes/weathermeme.js. Check out the [express documentation](http://expressjs.com/) for more info on the express api.
