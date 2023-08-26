// express app
const express = require('express');
const app = express();
const cors = require('cors');
const movieRoutes = require('./routes/movieRoutes');

// Importing and configuring different dependencies
const path = require('path');
const mongoose = require('mongoose');
const PORT = process.env.PORT || 3001;
require('dotenv').config();

// middleware
app.use(express.json());
app.use(cors());

app.use((req, res, next) => {
	console.log(req.path, req.method)
	next()
});

// routes
app.use('/api/movies', movieRoutes);

// connect to MongoDB
mongoose.connect(process.env.MONGO_URI).then(() => {
	console.log("Connected to database")
	app.listen(PORT, () => {
	console.log("Server running on PORT: " + PORT)
	})
}).catch((error) => {
	console.log(error)
});
