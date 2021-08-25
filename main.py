from random import randint

class Game:
    def __init__(self, word):
        self.score = 5
        self.spaces = len(word)
        self.answer = word

    def validate_single(self, x):
        if len(x) != 1:
            return False
        if not x.isalpha():
            return False
        return True

    def inner_game(self):
        while self.score > 0:
            candidate = input(f"{self.spaces} letter word")
            if not self.validate_single(candidate):
                continue
            if candidate in self.answer:
                print("yay")
                print(f"your score is {self.score}")
            else:
                print("Nooooo")
                self.score -= 1
                print(f"your score is {self.score}")


bigstring = """This is more of a guess the word game the core concepts you have to use while
developing this project are variables random integer strings char input and output and boolean 
in the game users have to enter letter guesses and each user will have a limited number of guesses 
a counter variable is needed for limiting the guesses this is one of the interesting python projects to begin with"""
wordlist = bigstring.split()

wordnum = randint(0, len(wordlist))

this_game = Game(wordlist[wordnum])

this_game.inner_game()





