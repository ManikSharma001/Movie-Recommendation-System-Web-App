// Schema and Model for Database
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const movieSchema = new Schema({
	title: {
		type: String,
		required: true
	},
	genre: {
		type: String,
		required: true
	},
	rating: {
		type: Number,
		required: false
	},
	parental_guide: {
		type: String,
		required: false
	},
	runtime: {
		type: Number,
		required: false
	},
	actors: {
		type: Array,
		required: false
	}

}, {timestamps: true});

module.exports = mongoose.model('Movie', movieSchema);