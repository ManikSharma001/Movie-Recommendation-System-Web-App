import React, { useState, useEffect } from 'react';

const MovieRecommendation = () => {
    const [title, setTitle] = useState('');
    const [genre, setGenre] = useState('');
    const [rating, setRating] = useState('');
    const [parental_guide, setParentalGuide] = useState('');
    const [runtime, setRuntime] = useState('');
    const [actors, setActors] = useState('');

    useEffect(() => {
      const fetchRecommendedMovie = async () => {
        try {
          const response = await fetch('http://localhost:3001/api/movies');

          if (response.ok) {
            const data = await response.json();
            console.log(data); 
            setTitle(data.mssg[0]);
            setGenre(data.mssg[1]);
            setRating(data.mssg[2]);
            setParentalGuide(data.mssg[3]);
            setRuntime(data.mssg[4]);
            setActors(data.mssg[5]);
          } 
          else {
            console.log('Error:', response.status);
          }
        } 
        catch (error) {
          console.log('Fetch Error:', error);
        }
      };

      fetchRecommendedMovie();
    }, []);


  return (
    <div className="movie-recommendation">
      <h2>{title}</h2>
      <p>
        Genre: {genre}<br></br>
        Rating: {rating}<br></br>
        Parental Guide: {parental_guide}<br></br>
        Runtime: {runtime} minutes<br></br>
        Actors: {actors} <br></br>
      </p>
    </div>
  );
};

export default MovieRecommendation;
