from hangman import Hangman, HumanPlayer, ComputerPlayer



def test_game_initialization():
    human_player = HumanPlayer("TestPlayer")
    computer_player = ComputerPlayer("TestComputer")
    game = Hangman([human_player, computer_player])
    
    assert isinstance(game.word, str), "Expected the game word to be a string"
    assert "_" in game.display_word(), "Expected the displayed word to contain underscores"
    assert len(game.players) == 2, "Expected the game to have two players"



def test_correct_guess():
    human_player = HumanPlayer("TestPlayer")
    game = Hangman([human_player])
    
    correct_letter = game.word[0]
    game.guessed_letters.append(correct_letter)  
    
    assert correct_letter in game.display_word(), "Expected correct guess to be in the displayed word"



def test_incorrect_guess():
    human_player = HumanPlayer("TestPlayer")
    game = Hangman([human_player])
    
    initial_lives = human_player.lives
    incorrect_letter = "z"
    game.guessed_letters.append(incorrect_letter)  
    
    game.turn(human_player)  
    
    assert incorrect_letter not in game.word, "Expected incorrect guess to not be in the game word"
    assert human_player.lives < initial_lives, "Expected player's lives to decrease after an incorrect guess"



def test_game_end_conditions():
    human_player = HumanPlayer("TestPlayer")
    game = Hangman([human_player])
    
    
    for letter in game.word:
        game.guessed_letters.append(letter)
    
    assert "_" not in game.display_word(), "Expected no underscores after completing the word"
    assert human_player.score > 0, "Expected positive score after winning the game"
    
    
    while human_player.lives > 0:
        game.guessed_letters.append("x")  
        game.turn(human_player)
    
    assert human_player.lives == 0, "Expected player to have no lives left"
    assert human_player.score <= 0, "Expected zero or negative score after running out of lives"


def run_tests():
    test_game_initialization()
    test_correct_guess()
    test_incorrect_guess()
    test_game_end_conditions()
    
    print("All tests passed!")



if __name__ == "__main__":
    run_tests()
