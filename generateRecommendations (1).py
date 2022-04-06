from fuzzywuzzy import fuzz
import movieScraper
import recommender
from tabulate import tabulate

'''
installation requirements

/opt/virtualenvs/python3/bin/python3 -m pip install --upgrade pip
pip install fuzzywuzzy
pip install sklearn
pip install pandas
pip install python-Levenshtein
pip install tabulate
'''
# movies = movieScraper.extractWeb()
movies = movieScraper.imdbExtraction()
# Levenshtein Distance calculation
def similarityScore(movie1, movie2):
   return fuzz.ratio(movie1, movie2)

def getMovieTitle(index):
   return movies[movies.index == index]["Title"].values[0]

def getIndex(movieTitle):
   return movies[movies.Title == movieTitle].index.values[0]

def closestTitle(movieTitle):
    levenshteinScoreList = list()
    indexCount = 0
    for title in movies["Title"]:
        levenshteinScoreList.append((indexCount, similarityScore(title, movieTitle)))
        indexCount += 1
    sortedScores = sorted(levenshteinScoreList, key = lambda x: x[1], reverse=True)
    movie = getMovieTitle(sortedScores[0][0])
    score = sortedScores[0][1]
    return movie, score
    
def recommendationEngine(inputMovie, numberOfRecommendations):
    #print("\nYou want to find movies similar to: ", inputMovie, '\n')
    recommendedMovie, levenshteinScore = closestTitle(inputMovie)
    # if levenshteinScore != 100:
    #     print('Hmm, did you mean '+ str(recommendedMovie)+'?\n')
    index = int(getIndex(recommendedMovie))
    listOfRecommendations = list(enumerate(recommender.tfidf_cosine()[index]))
    sortedListOfRecommendations = sorted(listOfRecommendations,key=lambda x:x[1], reverse=True)
    # remove the movie itself
    listOfSimilarMovies = list(filter(lambda x:x[0] != int(index), sortedListOfRecommendations)) 
    result = []
    # print("-------------------------------------")
    # print("Movie Recommendations based on Content")
    # print("-------------------------------------\n")
    for index, value in listOfSimilarMovies[:numberOfRecommendations]:
        movie = ""
        movieName = getMovieTitle(index)
        if movieName[len(movieName)-5:] == ", The":
            movie = "The " + movieName[:len(movieName)-5]
        else:
            movie = movieName
        percentValue = round(value * 100, 2)
        result.append([movie, percentValue])
    return recommendedMovie, levenshteinScore, result
    #print(tabulate(result, headers=["Movie Name", "Similarity with Original Movie (in %)"]))