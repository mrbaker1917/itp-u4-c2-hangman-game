from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["Python", "help", "crocodile", "elephant", "exceptional", "father", "developer", "project", "album", "telephone"]


def _get_random_word(list_of_words):
    return random.choice(list_of_words)


def _mask_word(word):
    return "*" * len(word)


def _uncover_word(answer_word, masked_word, character):
    if character in answer_word:
        masked_word = masked_word[:answer_word.find(character)] + character + masked_word[answer_word.find(character)+1:]
    return masked_word


def guess_letter(game, letter):
    if game.remaining_misses == 0:
        return "Sorry, you lost! You have used up all five guesses!"
    if _uncover_word(game.answer_word, game.masked_word, letter) == game.masked_word:
        game.remaining_misses -= 1
        game.previous_guesses.append(letter)
        return f"Sorry, {letter} is not in the word. You have {game.remaining_misses} left."
    if letter in game.previous_guesses:
        return f"You already guessed {letter}! Try again!"
    if _uncover_word(game.answer_word, game.masked_word, letter) != game.masked_word:
        game.previous_guesses.append(letter)
        new_masked = _uncover_word(game.answer_word, game.masked_word, letter)
        return f"Well done, you guessed one of the letters: {new_masked}."


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
