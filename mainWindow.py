# importing libraries
from GameWindow import *
from Self_Play import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

# class mainwindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # add title to window
        self.setWindowTitle("Welcome Window")

        # setting window size
        self.resize(400,400)

        # set window icone 
        self.setWindowIcon(QIcon("resources/icon.png"))

        # call style window methods
        self.style_Mwindow()

        # displying window
        self.show()

     # style of window
    def style_Mwindow(self):
        # change color of main window
        self.setStyleSheet("background-color: grey")

        # create button one allow to user play itself
        player_button = QPushButton("Play Game",self)
        player_button.setGeometry(20,100,360,40)
        player_button.setStyleSheet("border-radius:10px;font-size:25px;bacKground:#344D67;color:white;")
        player_button.clicked.connect(self.start)

        # create button two allow game play itself using algorithm
        itselfPlay_button = QPushButton("self Play Game",self)
        itselfPlay_button.setGeometry(20,250,360,40)
        itselfPlay_button.setStyleSheet("border-radius:10px;font-size:25px;bacKground:#344D67;color:white;")
        itselfPlay_button.clicked.connect(self.start_play_itself)
            
    def start_user_play(self):
        game = GameWindow()
        game.Run_Game()

    def start_play_itself(self):
        main()

if __name__ == '__main__':

    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = MainWindow()

    # start the app
    sys.exit(App.exec_())
