import random
from hangman.player import HMPlayer, HumanPlayer, ComputerPlayer

class Hangman:
    def __init__(self, players: list):
        self.word = random.choice(["dog", "cat", "house", "girona", "spain"]).lower()
        self.players = players
        self.guessed_letters = []
    
    def display_word(self) -> str:
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display
    
    def play(self):
        for player in self.players:
            while player.lives > 0 and "_" in self.display_word():
                self.turn(player)

            if "_" not in self.display_word():
                print("Player {} wins!".format(player.name))
                player.score += 10
            else:
                print("Sorry {}, you lose!".format(player.name))
                print("The word was {}".format(self.word))
        
        lives = [player.lives for player in self.players]
        winner = self.players[lives.index(max(lives))]
        loser = self.players[lives.index(min(lives))]

        print("The player that has won the game is {}".format(winner))
        print("The player that has lost the game is {}".format(loser))

    def turn(self, player: HMPlayer):
        print("Player {}. Word: {}".format(player.name, self.display_word()))
        l = player.propose_letter()
        print("Player {} proposes letter {}".format(player.name, l))

        if l not in self.word:
            print("Bad guess!\n")
            player.score -= 0.5
            player.lives -= 1
        else:
            if l not in self.guessed_letters:
                self.guessed_letters.append(l)
                player.score += 1
            else:
                print("Letter already guessed!")
