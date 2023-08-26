// Router for Express App
const express = require('express');
const { getRecommendedMovie, receiveMovieData } = require('../controllers/movieController');
const router = express.Router();

// Obtain data from frontend react form
// Route to handle movie data POST request
router.get('/', getRecommendedMovie);

// Send data to frontend with recommended movie
router.post('/', receiveMovieData);

module.exports = router;