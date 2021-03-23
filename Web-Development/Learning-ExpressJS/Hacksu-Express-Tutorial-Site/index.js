// Oliver Keen
// index.js
// 3/9/2021

// Lets us reference this module as "express"
// Creates application by running module as function
const express = require("express");
const app = express();

// Root of app, responds with "Hello, world!" when visited with GET request
app.get('/', function(req, res) {
  res.send("Hello, world!")
})

// At /time, responds with current server time
app.get("/time", (req, res) => { // Shorthand func declaration in JavaScript
  res.send(new Date().toString())
})

// Visit some routes
let port = 8080; // Listen on 8080

app.listen(port, () => {console.log("Listening on http://localhost:" + port)
});
