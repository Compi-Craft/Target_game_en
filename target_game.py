"""
Target game
"""
from typing import List
from random import choice
def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. letters for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    alpha_lst = []
    game_lst = []
    for i in range(ord('a'), ord("z") + 1):
        alpha_lst.append(chr(i))
    i = 0
    while i < 3:
        small_lst = []
        k = 0
        while k < 3:
            small_lst.append(choice(alpha_lst))
            k += 1
        game_lst.append(small_lst)
        i += 1
    return game_lst


def get_words(file_read: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(file_read, "r", encoding="utf-8") as file:
        word_lst = []
        for i in file:
            i = i.replace("\n", "")
            word_lst.append(i.lower())
    fin_lst = []
    for i in word_lst:
        if len(i) >= 4 and letters[4] in i:
            for k in i:
                if k in letters and i.count(k) <= letters.count(k):
                    check = True
                else:
                    check = False
                    break
            if check is True:
                fin_lst.append(i)
    return fin_lst

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    player_lst = []
    while True:
        try:
            word = input()
            player_lst.append(word.lower())
        except EOFError:
            break
    return player_lst


def get_pure_user_words(user_words: List[str], letters: List[str],\
words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    win_lst = []
    for i in user_words:
        if i not in words_from_dict:
            start_word = i
            i = i.lower()
            if len(i) >= 4 and letters[4] in i:
                for k in i:
                    if k in letters and i.count(k) <= letters.count(k):
                        check = True
                    else:
                        check = False
                        break
                if check is True:
                    win_lst.append(start_word)
    return win_lst

def results():
    """
    Main process of the game
    """
    letters = generate_grid()
    print(letters)
    good_grid = []
    i = 0
    while i < len(letters):
        k = 0
        while k < len(letters[i]):
            good_grid.append(letters[i][k])
            k += 1
        i += 1
    player_lst = get_user_words()
    winning_words = get_words("en.txt", good_grid)
    pure_words = get_pure_user_words(player_lst, good_grid, winning_words)
    with open("result.txt", "w", encoding="utf-8") as file:
        counter = 0
        skip_lst = []
        for i in player_lst:
            if i in winning_words:
                counter += 1
        for i in winning_words:
            if i not in player_lst:
                skip_lst.append(i)
        print(counter)
        file.write(str(counter) + '\n')
        for i in skip_lst:
            print(i)
            file.write(i + '\n')
        for i in pure_words:
            print(i)
            file.write(i + '\n')

if __name__ == "__name__":
    import doctest
    print(doctest.testmod())
    results()