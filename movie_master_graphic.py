# images were taken from vectorImages.com
from graphics import *
import random

def inside(point, rectangle):
  lowerLeft = rectangle.getP1()
  upperRight = rectangle.getP2()
  return lowerLeft.getX() < point.getX() < upperRight.getX() and lowerLeft.getY() < point.getY() < upperRight.getY()

class Movie_Master_Graphic:
    def __init__(self):
        self.window = GraphWin("Movie Master", 700, 800)
        self.window.setCoords(0,0,30,40)
        self.image = Image(Point(15,32), "popcorn.gif")
        self.message = Text(Point(15, 22),"Hi! This is Movie Master. And what is your name? ")
        self.message.setSize(20)
        self.entry = Entry(Point(15, 5), 15)
        self.entry.setSize(20)
        self.entry.setFill(color_rgb(247,247,222))
        self.guide = Text(Point(15,2), "HIT ENTER TO MOVE ON")
        self.guide.setTextColor('black')
        self.reply = Text(Point(15, 8), "")
        self.reply.setSize(20)
        self.finish_image = Image(Point(15,32), "popcorn.gif")
        self.recommendation_display = Text(Point(15,13),"")
        self.recommendation_display.setSize(15)
        self.recommendation_display.setFace('courier')

    def conversation_starter_graphic(self):
        name = ""
        favoriteMovie = ""
        numberOfRecs = 0

        try:
            self.image.draw(self.window)
        except:
            pass
        try:
            self.message.draw(self.window)
        except:
            pass
        try:
            self.entry.draw(self.window)
        except:
            pass
        try:
            self.guide.draw(self.window)
        except:
            pass
        try:
            self.reply.draw(self.window)
        except:
            pass

        # Get user name
        while self.window.getKey() != "Return":
            name = self.entry.getText().capitalize()
        name = self.entry.getText().capitalize()
        self.entry.undraw()

        # reply to user name
        self.message.setText("")
        if len(name) == 0:
            self.reply.setText("Okay, strange that you don't have a name!\nI'll call you Dave!")
            name = "Dave"
        else:
            self.reply.setText(f"Oh Great! Hi {name}.")

        while self.window.getKey() != "Return":
            self.reply.setSize(20)
        self.reply.setText("")

        self.message.setText("What's a movie you want recommendations similar to? ")
        self.entry.setText("")
        self.entry.draw(self.window)

        while self.window.getKey() != "Return":
            favoriteMovie = self.entry.getText().title()
        favoriteMovie = self.entry.getText().title()
        self.entry.undraw()
        self.message.setText("")

        self.message.setText("And how many recommendations would you like? ")
        self.entry.setText("")
        self.entry.draw(self.window)

        while self.window.getKey() != "Return":
            numberOfRecs = self.entry.getText()
        numberOfRecs = self.entry.getText()
        self.entry.undraw()
        self.message.setText("")

        self.message.setText("...Wait for it...")
        time.sleep(1)
        return name, favoriteMovie, numberOfRecs

    def display_recommendations_graphic(self, formattedRecommendations, userName, initialMovie, levenshteinScore):
        self.image.undraw()
    
        self.finish_image.draw(self.window)
        self.guide.setText("")

        if int(levenshteinScore) != 100:

            self.message.setText(f"We couldn't find that movie in our directory.\nSo we'll show you recommendations for {initialMovie}! \n")
            self.guide.setText("")
            time.sleep(5)

        self.message.setText(f"Ok {userName}, here they are! \n")
        self.recommendation_display.setText(formattedRecommendations)
        self.recommendation_display.draw(self.window)
        self.guide.setText("HIT ENTER TO MOVE ON")
        while self.window.getKey() != "Return":
            self.recommendation_display.setSize(15)

    def reset_display(self):
        self.message.setText("Hi. This is Movie Master! And what is your name? ")
        self.entry.setText("")
        self.finish_image.undraw()
        self.recommendation_display.undraw()