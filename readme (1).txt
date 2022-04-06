Name: Maanya Goenka
Course: CS 321 - Making Decisions with Artificial Intelligence
Professor: David Musicant
Date: 11/21/2021
Project: Movie Recommendation System

Description: 

For the purposes of the self-guided assignment, I made a content based movie recommendation system that uses tf-idf vectorization and 
cosine similarity to recommend movies to the user based on an initial input - a movie name, and an integer representing the number of 
recommendations the user wants. The dataset used for generating recommendations is the imdb.csv dataset which consists of over 85000 
movies (for the purposes of this recommendation system, the dataset has been limited to 25,000 movies in the interest of saving time 
and memory). If the movie input by the user is not one that is present in the dataset (misspelled movies are not in the dataset anyway), the 
system generates recommendations for a movie in the dataset with a title most similar to the one inputted by the user of the system; this is based 
on the concept of Levenshtein distance. 

How to run the program:

Step 1: Install the following packages/modules (also specified in the generateRecommendations.py file).
- pip install sklearn
- pip install pandas
- pip install fuzzywuzzy
- pip install python-Levenshtein
- pip install tabulate

Step 2: My version of Python has the time and graphics module already installed but if yours does not, install those two modules as well

Step 3: Then run the following command on the terminal: python3 grade.py

Step 4: An interactive chatbot made using Python GUI will pop up on the screen. Follow the instructions as deemed appropriate.
        Text boxes that are left empty accidentally have automatic placeholders associated with them but try to follow instructions. 

Step 5: Wait a few minutes for the final output or set of recommendations to be displayed on the terminal. 

Output: 

- I've attached screenshots of what an example output looks like

Interpretation of Results: 

- the first column of the final output table are the names of the recommended movies
- the second column of the output table are numerical values indicating how similar the recommended movie is to the inputted movie
- when the user doesn't enter a name, the name 'Dave' is used as a placeholders
- when the user doesn't enter a number for recommendations, the number 5 is used as default
- wait times for the program can vary depending on the number of recommendations requested and the OS used
- memory used by the program can vary depending on the OS used, on my system the program consumes 9 GB of memory