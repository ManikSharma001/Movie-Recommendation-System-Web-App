# Movie-Recommendation-System-Web-App
 
The Movie Recommendation System Web App is a user-friendly platform that provides personalized movie recommendations to users based on their previously liked movies. Whether you're a cinephile looking for your next favorite film or just someone seeking entertainment options, my web app has got you covered.

## How It Works ##

The Movie Recommendation System uses content based filtering techniques to suggest movies based on previous movie preferences. It compares the inputted movies togeter to extract features similar in order to suggest a new movie that the user may like. 

## Prerequisites ##
    
    Install Node.js and npm (Node Package Manager) on your system.
    Python (version 3.6 or higher)
    pip (Python package manager)

## Setting Up the Web App ##

### Clone this repository to your local machine. ###

    git clone https://github.com/ManikSharma001/Movie-Recommendation-System-Web-App.git
    cd movie-recommendation-app

### Install server dependencies and start the server. ###

    cd server
    npm install mongodb express cors dotenv 
    npm start

### Install client dependencies and start the client. ###

    cd ../client
    npx create-react-app client
    npm install react-router-dom
    npm start

Access the web app by opening your browser and navigating to http://localhost:3000.

## Using the Web App ## 

    On the home page, enter the names of three of your favorite movies.
    Click the "Submit" button.
    The system will analyze your input and provide you with a recommended movie based on your favorites.
    
### Technologies Used ###

    Python
     - Pandas
     - Requests
     - Numpy
     - Scikit-Learn (to be added)
    JavaScript
     - Frontend
      -> React Frontend
     - Backend
      -> Node.js Express App Backend
    HTML
    CSS
    MongoDB (not in function yet - will be added on in the future)
    Machine Learning (Content Based Filtering)

## Contributing ##

I welcome contributions from the community! Whether you want to report issues, suggest improvements, or submit new features, your input is highly appreciated.

## License ##

This project is licensed under the MIT License.

## Things to Imporve (Not in Any Particular Order) ##
* Increase the Speed of Recommendation Algorithm
* Add in User Error-Checking
* Add semantic analysis using word vectors in order to better identify similar plotlines in movies (separate program already created - just need to add it in seamlessly)
* Add user accounts for users to access and save liked suggestions
