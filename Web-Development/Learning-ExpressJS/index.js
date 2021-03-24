// Oliver Keen
// index.js
// Follows tutorial from https://github.com/hacksu/express-tutorial
// 3/23/2021

// References this module as "express"
// Creates application by running module as function
const express = require("express");
const app = express();

// Root of app, responds with "Hello, world!" when '/' visited with GET request
app.get('/', function(req, res) {
  res.send("Hello, world!")
})

// Responds with current server time at "/time"
app.get("/time", (req, res) => { // Shorthand func declaration in JavaScript
  res.send(new Date().toString())
})

// Visit some routes
let port = 8080; // Listens on 8080

app.listen(port, () => {console.log("Listening on http://localhost:" + port)
});

/// Creating an API for the web app ////////////////////////////////////////////
// Allows cross-origin requests
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", '*')
  next()
})

// Gets new router for API routes
// Essentially is mini app that hooks to main app on line 47
let api = new express.Router();

api.get('/', (req, res) => {
  res.send("This is the root of the API!")
})

// "/api/welcome/Oliver" returns "Welcome to my app, Oliver!"
api.get("/welcome/:name", (req, res) => {
  res.send("Welcome to my app, " + req.params.name + '!')
})

// Mounts API router to app
app.use("/api", api);