#!/bin/python3

from collections import deque
from copy import deepcopy

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    if start_word == end_word:
        l = [start_word]
        return l
    
    # readlines creates a list of strings
    word_Dict = open(dictionary_file)
    word_List = word_Dict.read().split("\n")
    
    # list = stack
    wordStack = []                  # creating a stack
    wordStack.append(start_word)    # pushing start word onto stack

    #deques = queue
    wordQ = deque()         # creating a queue
    wordQ.append(wordStack) # enqueing stack onto queue

    while len(wordQ) > 0:                                   # while the queue is not empty
        q = wordQ.pop()                                     # dequeu a stack from the queue 
        for word in word_List:                              # for each word in the dictionary
            if _adjacent(word,q[len(q)-1]) is True:         # if the word is adjacent to the top of the stack
                if word == end_word:                        # if this word is the end word
                    q.append(word)                          # append your list which has the front word with this word
                #return wordStack
                copyStack = deepcopy(q)
                copyStack.append(word)
                wordQ.appendleft(copyStack)
                word_List.remove(word)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''

    if len(ladder) == 0:
        return False
    else:
        for i in range(len(ladder)-1):
            if _adjacent(ladder[i], ladder[i+1]) is False:
                return False
        return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    
    s = False

    for i, j in zip(word1, word2):
        if i != j:
            if s:
                return False
            else:
                s = True

    return s 
