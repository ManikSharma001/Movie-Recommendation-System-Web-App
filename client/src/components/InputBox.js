// Form to take in user input 
import { useState } from 'react';
import MovieRecommendation from './MovieRecommendation'

const InputBox = () => {
  // State variables to store user input
  const [movieTitle1, setMovieTitle1] = useState('');
  const [movieTitle2, setMovieTitle2] = useState('');
  const [movieTitle3, setMovieTitle3] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);

  // Handler functions to update state variables when user inputs data
  const handleMovieTitle1 = (event) => {
    setMovieTitle1(event.target.value);
  };

  const handleMovieTitle2 = (event) => {
    setMovieTitle2(event.target.value);
  };

  const handleMovieTitle3 = (event) => {
    setMovieTitle3(event.target.value);
  };

  // Handler function to handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsSubmitted(true);

    // Send data to the backend
    try {
        // Send the data to the backend using fetch
        const response = await fetch('/api/movies', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            movie1: movieTitle1,
            movie2: movieTitle2,
            movie3: movieTitle3,
          }),
        });

        if (response.ok) {
          console.log('Data sent to the backend successfully!');
        } 
        else {
          console.error('Failed to send data to the backend.');
        }
      } 

      catch (error) {
        console.error('An error occurred while sending data to the backend:', error);
      }

    // Reset Submission form 
    setMovieTitle1('');
    setMovieTitle2('');
    setMovieTitle3('');
  };

  return (
    <div className="center-container">
      <form onSubmit={handleSubmit} className="user-input-form">
      	<div>
	        <label>
	          Movie 1:
	          <input type="text" value={movieTitle1} onChange={handleMovieTitle1} />
	        </label>
	      </div>
	      <div>
	        <label>
	          Movie 2:
	          <input type="text" value={movieTitle2} onChange={handleMovieTitle2} />
	        </label>
	      </div>
	      <div>
	        <label>
	          Movie 3:
	          <input type="text" value={movieTitle3} onChange={handleMovieTitle3} />
	        </label>
	    	</div>
	      <button type="submit">Submit</button>
	    </form>
    {isSubmitted && <MovieRecommendation />}
	  </div>
  );
};

export default InputBox;
