import random

class HMPlayer:
    """This is a generic player for the Hangman game."""
    def __init__(self, name: str) -> None:
        self.name = name
        self.lives = 5
        self.score = 0
    
    def propose_letter(self) -> str:
        """To be implemented in derived classes."""
        return ""
    
    def __str__(self) -> str:
        return "{} has {} lives and {} points".format(self.name, self.lives, self.score)
    
    def __lt__(self, other):
        return self.score < other.score
    
    def __gt__(self, other):
        return self.score > other.score


class HumanPlayer(HMPlayer):
    """This is a human player for the Hangman game."""
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def propose_letter(self) -> str:
        letter = input("Please propose a letter: ")
        while len(letter) != 1:
            letter = input("Please propose a single letter: ")
        return letter


class ComputerPlayer(HMPlayer):
    """This is a computer player for the Hangman game."""
    def __init__(self, name: str) -> None:
        super().__init__(name + " (computer)")
        self.proposed_letters = []
    
    def propose_letter(self) -> str:
        letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        while letter in self.proposed_letters:
            letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        self.proposed_letters.append(letter)
        return letter
