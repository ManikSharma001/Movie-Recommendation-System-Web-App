#!/usr/bin/env python3

'''
Python script to generate a recommened movie based upon previously liked movies using machine learning.
'''
import sys
import os
import requests
import numpy as np
import pandas as pd
from ast import literal_eval


def getDirector(crew):
  # Find and return the director of a film in the crew data 
  res = 'N/A'
  for person in crew:
    if person['job'].lower() == 'director':
      res = person['name']
  
  return res



def getArrayofInformation(source):
  # Create an array (list) of information
  names = []
  if isinstance(source, list):
    names = [i['name'] for i in source]
    if len(names) > 3:
      names = names[:3]
      
  return names


  
def initModel():
  # Initalize global variables needed throughtout the program
  global director_weight
  global cast_weight
  global genre_weight
  global keyword_weight

  director_weight = {}
  cast_weight = {}
  genre_weight = {}
  keyword_weight = {}
  
  # Get intial movie information through csv file 
  global movie_data
  movie_data = pd.read_csv(r"C:\Users\manik\Documents\MovieRecommendationSystem\server\scripts\movies_metadata.csv", low_memory=False)
  movie_data['overview'] = movie_data['overview'].fillna('')
  # The following Movie ID's are wrong - therefore drop them
  movie_data = movie_data.drop([19730, 29503, 35587])
  
  # Get more information about the movies 
  movie_credits = pd.read_csv(r"C:\Users\manik\Documents\MovieRecommendationSystem\server\scripts\credits.csv")
  movie_keywords = pd.read_csv(r"C:\Users\manik\Documents\MovieRecommendationSystem\server\scripts\keywords.csv")
  
  # Change each data type from id to int
  movie_credits['id'] = movie_credits['id'].astype('int')
  movie_keywords['id'] = movie_keywords['id'].astype('int')
  movie_data['id'] = movie_data['id'].astype('int')
  
  # Combine the movie credits and movie keywords data into main movie database
  movie_data = movie_data.merge(movie_credits, on='id')
  movie_data = movie_data.merge(movie_keywords, on='id')

  # Apply certain features to movie database for easy access
  important_features = ['cast', 'crew', 'keywords', 'genres']
  for feature in important_features:
    movie_data[feature] = movie_data[feature].apply(literal_eval)

  movie_data['director'] = movie_data['crew'].apply(getDirector)
  specific_features = ['cast', 'keywords', 'genres']
  for feature in specific_features:
    movie_data[feature] = movie_data[feature].apply(getArrayofInformation)

  # Initialize a score of 0 for all movies in the beginning
  movie_data['Score'] = 0

    

def getMovieInfo(movie):
  # Need to get movie info from web database as the user may input new movies not available in the older Kaggle movie database
  info = ""
  base_link = "http://www.omdbapi.com/?t=" 
  if " " in movie:
    movie_title_str = ""
    movie_title = movie.split()
    # Need to format the link properly which involves putting underscores between each word of the title
    for i in range(len(movie_title)):
      movie_title_str += movie_title[i]
      movie_title_str += "_"

    movie_title_str = movie_title_str[0:-1] # Remove the last unnecessary underscore from the words of the title 
    link = base_link + movie_title_str.lower() + "&apikey=ec1d2d40" 
  else:
    link = base_link + movie.lower() + "&apikey=ec1d2d40"

    
  response = requests.get(link)
  if (response.status_code == 200): # The API call worked
    info = response.json()
  else:
    print("Movie Not Found")
    
  return info


def parseData(movie1, movie2, movie3):
  global director_weight
  global cast_weight
  global genre_weight
  global keyword_weight
  global movie_data

  # Remove the same movies from database so as to not output the same movie
  movie_data.drop(movie_data.loc[movie_data['original_title'] == movie1].index, inplace=True)
  movie_data.drop(movie_data.loc[movie_data['original_title'] == movie2].index, inplace=True)
  movie_data.drop(movie_data.loc[movie_data['original_title'] == movie3].index, inplace=True)
  
  # Obtain movie information for all 3 inputted movies
  movie1_info = getMovieInfo(movie1)
  movie2_info = getMovieInfo(movie2)
  movie3_info = getMovieInfo(movie3)

  basic_words = ["the", "as", "is", "out", "with", "in", "from", "a", "an", "while", "they", "each" "have", "has", "can't", "couldn't", "hadn't", "or", "on", "and", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero", "then", "who", "what", "where", "when", "why", "how", "first", "second", "third", "therefore", "of", "must", "his", "him", "her", "she", "he", "to", "too", ]

  # Identify similarities and change recommendation weights based upon commonalties - useful for the content-based filtering
  # Essentially identifying similar content between movies

  # Movie 1
  director1 = movie1_info['Director']
  director_weight[director1] = 2

  actors1 = movie1_info['Actors'].split(',')
  for i in range(len(actors1)):
    cast_weight[actors1[i]] = 2

  genre1 = movie1_info['Genre'].split(',')
  for j in range(len(genre1)):
    genre_weight[genre1[j]] = 2

  keywords1 = movie1_info['Plot'].split(' ')
  for k in range(len(keywords1)):
    if keywords1[k].replace(',', '').replace('.', '').lower() not in basic_words:
      keyword_weight[keywords1[k].replace(',', '').replace('.', '').lower()] = 0.5

  # Movie 2
  i = 0
  j = 0
  k = 0
  director2 = movie2_info['Director']
  if director2 in director_weight.keys():
    director_weight[director2] *= 2
  else:
    director_weight[director2] = 2

  actors2 = movie2_info['Actors'].split(', ')
  for i in range(len(actors2)):
    if actors2[i] in cast_weight.keys():
      cast_weight[actors2[i]] *= 2
    else:
      cast_weight[actors2[i]] = 2

  genre2 = movie2_info['Genre'].split(',')
  for j in range(len(genre2)):
    if genre2[j] in genre_weight.keys():
      genre_weight[genre2[j]] *= 2
    else:
      genre_weight[genre2[j]] = 2

  keywords2 = movie2_info['Plot'].split(' ')
  for k in range(len(keywords2)):
    if keywords2[k].replace(',', '').replace('.', '').lower() in keyword_weight.keys():
      keyword_weight[keywords2[k].replace(',', '').replace('.', '').lower()] += 0.5
    elif keywords2[k].replace(',', '').replace('.', '').lower() not in basic_words:
      keyword_weight[keywords2[k].replace(',', '').replace('.', '').lower()] = 0.5
  
  # Movie 3
  i = 0
  j = 0
  k = 0
  director3 = movie3_info['Director']
  if director3 in director_weight.keys():
    director_weight[director3] *= 2
  else:
    director_weight[director3] = 2

  actors3 = movie3_info['Actors'].split(', ')
  for i in range(len(actors3)):
    if actors3[i] in cast_weight.keys():
      cast_weight[actors3[i]] *= 2
    else:
      cast_weight[actors3[i]] = 2

  genre3 = movie3_info['Genre'].split(',')
  for j in range(len(genre3)):
    if genre3[j] in genre_weight.keys():
      genre_weight[genre3[j]] *= 2
    else:
      genre_weight[genre3[j]] = 2

  keywords3 = movie3_info['Plot'].split(' ')
  for k in range(len(keywords3)):
    if keywords3[k].replace(',', '').replace('.', '').lower() in keyword_weight.keys():
      keyword_weight[keywords3[k].replace(',', '').replace('.', '').lower()] += 0.5
    elif keywords3[k].replace(',', '').replace('.', '').lower() not in basic_words:
      keyword_weight[keywords3[k].replace(',', '').replace('.', '').lower()] = 0.5



def getMovieRecommendation():
  global director_weight
  global cast_weight
  global genre_weight
  global keyword_weight
  global movie_data
  
  # Run through data frame and compute scores of each movie based upon similarity metrics identified before
  # Sort data frame by score and output the movie with the highest similarity score
  for index, row in movie_data.iterrows():
    score = 0
    # First, calculate director score
    if row['director'] in director_weight.keys():
      score += director_weight[row['director']]

    # Next, calculate cast score
    for i in range(len(row['cast'])):
      if row['cast'][i] in cast_weight.keys():
        score += cast_weight[row['cast'][i]]

    # Next, calculate genre score
    for j in range(len(row['genres'])):
      if row['genres'][j] in genre_weight.keys():
        score += genre_weight[row['genres'][j]]

    # Next, calculate keywords score
    for k in range(len(row['keywords'])):
      if row['keywords'][k] in keyword_weight.keys():
        score += keyword_weight[row['keywords'][k]]

    movie_data.loc[index, 'Score'] = score

  recommended_movie_index = movie_data['Score'].idxmax()
  movie_data.to_csv('ans.csv')
  return movie_data['original_title'][recommended_movie_index]

def formatOutput(movie):
    # Function to obtain necessary data and format it with each piece of information on a newline
    # Makes API calls to obtain extra information about the movie
    recommended_movie_info = getMovieInfo(movie)
    try:
      output = recommended_movie_info['Title'] + "\n" + recommended_movie_info['Genre'] + "\n" + recommended_movie_info['imdbRating'] + "\n" + recommended_movie_info['Rated'] + "\n" + recommended_movie_info['Runtime'] + "\n" + recommended_movie_info['Actors']
    except KeyError:
      output = "Cannot Recommend Movie\nN/A\nN/A\nN/A\nN/A\nN/A"
    return output


if __name__ == "__main__":
  initModel()
  parseData(sys.argv[1], sys.argv[2], sys.argv[3])
  recommendedMovie = getMovieRecommendation()
  print(formatOutput(recommendedMovie))
  sys.stdout.flush()


