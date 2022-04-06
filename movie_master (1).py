import random
from movie_master_graphic import *
from movie_master_controller import *
import generateRecommendations
from tabulate import tabulate

class Movie_Master:
    def __init__(self, gui=True, numberOfRecommendations = 5):
        self.gui = gui
        self.movie_master_graphic = Movie_Master_Graphic()
        self.userName = ""
        self.favoriteMovie = ""
        self.numberOfRecommendations = numberOfRecommendations

    def conversationStarter(self):
        userName = input("Hi. This is Movie Master! And what is your name? ").capitalize()
        print("Oh Great! Hi ", userName, ". ")
        favoriteMovie= input("\nName a movie and I'll generate similar recommendations for you! ").lower()
        numberOfRecommendations = int(input("\nAnd how many recommendations would you like? "))
        return userName, favoriteMovie, numberOfRecommendations

    def generate(self):
        if self.gui:
            self.userName, self.favoriteMovie, self.numberOfRecommendations = self.movie_master_graphic.conversation_starter_graphic()
        else:
            self.userName, self.favoriteMovie, self.numberOfRecommendations = self.conversationStarter()

        userFavoriteMovie = self.favoriteMovie

        if self.numberOfRecommendations:
            numberOfRecommendations = int(self.numberOfRecommendations) 
        else:
            numberOfRecommendations = 5

        initialMovie, levenshteinScore, newListOfRecs = generateRecommendations.recommendationEngine(userFavoriteMovie, numberOfRecommendations)
        if self.gui:
            self.movie_master_graphic.display_recommendations_graphic(tabulate(newListOfRecs, headers=["Movie Name", "Similarity with Original Movie (in %)"]), self.userName, initialMovie, levenshteinScore)
        else:
            print(tabulate(newListOfRecs, headers=["Movie Name", "Similarity with Original Movie (in %)"]))

        self.addNewRecommendations(initialMovie, newListOfRecs)
        return newListOfRecs
  
    # creates a separate text file that contains the recommendations based on the movie input by the user
    def addNewRecommendations(self, initialMovie, recommendations):
        save_file = open(f"recommendations.txt", "a")
        save_file.write(f"\nGenerating recommendations for the movie: {initialMovie}\n\n")
        save_file.write(tabulate(recommendations, headers=["Movie Name", "Similarity with Original Movie (in %)"]))
        save_file.write("\n")
        save_file.close()

def main():
  master = Movie_Master()
  recommendations = master.generate()
  
if __name__ == "__main__":
    main()

