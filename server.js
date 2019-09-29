let express = require('express');
let http = require('http');
let history = require('connect-history-api-fallback');

// Setup Express App.
let app = express();

// Allow direct URL access. (ie. typing 8Squad.com.au/contact)
app.use(history());

// Redirect all requests to HTTPS.
app.all('*', function(req, res) {
    res.redirect(300,'https://' + req.headers.host + req.url);
});

// Setup and start server.
let server = http.createServer(app);
let port = process.env.PORT || 5000;
server.listen(port);