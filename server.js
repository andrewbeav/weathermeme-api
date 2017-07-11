// Dependencies
var express = require('express');

// Setting up express
var app = express();

// Routes
app.use('/weathermeme', require('./routes/weathermeme'));

// Starting server
app.listen(3000);
console.log('API listening on port 3000');
