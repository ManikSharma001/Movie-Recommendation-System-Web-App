// Controller file for backend
var movie1;
var movie2;
var movie3;
var recommendedMovieInformation;
var recommendedMovieInformationSend;

// GET request
// GET recommended movie for user 
const getRecommendedMovie = (req, res) => {
	console.log("Movies: " + movie1 + " " + movie2 + " "  + movie3);
	const spawn = require('child_process').spawn;
	const pythonProcess = spawn('python', ['../server/scripts/main.py', movie1, movie2, movie3]);

	pythonProcess.stdout.on('data', (data) => {
		res.status(200).json({mssg: data.toString().split('\r\n')});
	});
	pythonProcess.stderr.on('data', (data) => {
		// Error output from the Python script (if any)
		console.log('Python script error:', data.toString());
	 	});

		pythonProcess.on('close', (code) => {
		// Python script has completed
		console.log(`Python script exited with code ${code}`);
		});
};

// Obtain data from frontend react form
// Route to handle movie data POST request
const receiveMovieData = (req, res) => {
	movie1 = req.body.movie1;
	movie2 = req.body.movie2;
	movie3 = req.body.movie3;

	console.log('Received Movie Data');

	// Obtain recommended movie
	// Send signal to "recommend_movie.js" to start
	getRecommendedMovie(req, res);

};

module.exports = { getRecommendedMovie, receiveMovieData };