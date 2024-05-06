from hangman.game import Hangman
from hangman.player import HumanPlayer, ComputerPlayer

human_player = HumanPlayer("Salim")
computer_player = ComputerPlayer("Alain")

game = Hangman([human_player, computer_player])
game.play()
