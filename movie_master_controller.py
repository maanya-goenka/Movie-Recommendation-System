from movie_master import *
from movie_master_graphic import *
from graphics import *
import time

class Movie_Master_Controller:
  def __init__(self):
    self.master = Movie_Master(gui=True)

  def start(self):
    recommendations = self.master.generate()
    self.startOver()

  def startOver(self):
    if self.master.gui:
      window = self.master.movie_master_graphic.window

      button_yes = Rectangle(Point(8,3),Point(13,5))
      button_yes_text = Text(button_yes.getCenter(),"Start")
      button_yes.setFill('green')
      button_no = Rectangle(Point(17,3),Point(22,5))
      button_no_text = Text(button_no.getCenter(),"Exit")

      button_yes.draw(window)
      button_yes_text.draw(window)
      button_no.draw(window)
      button_no_text.draw(window)

      self.master.movie_master_graphic.guide.setText("")

      while True:
        clickPoint = window.getMouse()
        if inside(clickPoint,button_yes):
          self.master.movie_master_graphic.reset_display()
          button_yes.undraw()
          button_yes_text.undraw()
          button_no.undraw()
          button_no_text.undraw()
          self.start()
          break
        elif inside(clickPoint,button_no):
          button_yes.undraw()
          button_yes_text.undraw()
          button_no.undraw()
          button_no_text.undraw()
          bye_box = Rectangle(Point(8,3),Point(22,5))
          bye_text = Text(bye_box.getCenter(), "I hope you enjoy the movie recommendations. Bye!")
          bye_box.draw(window)
          bye_text.draw(window)
          time.sleep(2)
          bye_box.undraw()
          button_no_text.undraw()
          window.close()
          break

      button_yes.undraw()
      button_yes_text.undraw()
      button_no.undraw()
      button_no_text.undraw()
    else:
      startOver = input("Start Over? (Y/N)")
      if startOver.lower() == "y":
        self.start()
      else:
        print("Good bye!")

# for GUI button
def inside(point, rectangle):

  lowerLeft = rectangle.getP1()  
  upperRight = rectangle.getP2()

  return lowerLeft.getX() < point.getX() < upperRight.getX() and lowerLeft.getY() < point.getY() < upperRight.getY()

if __name__ == "__main__":
  controller = Movie_Master_Controller()
  controller.start()