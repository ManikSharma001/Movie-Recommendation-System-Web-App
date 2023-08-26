// Explain how to use website

import React from 'react';

const Explainer = () => {
  return (
    <div className="explanation-container">
      <h2>How Our Movie Recommendation System Works</h2>
      <p>
        Our movie recommendation system helps you discover new movies based on your favorite films.
        To get personalized recommendations, follow these steps:
      </p>
      <ol>
        <li>Input three of your favorite movies in the fields provided.</li>
        <li>Click the "Submit" button to generate your personalized movie recommendations.</li>
        <li>We'll analyze your input and suggest some exciting new movies for you to watch.</li>
      </ol>
      <p>Start exploring new movies now!</p>
    </div>
  );
};

export default Explainer;
