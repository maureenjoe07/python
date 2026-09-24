# functions, code blocks and while loops.
def my_fuction():
    print('Hello')
    print('bingo')

my_fuction()



# DAY 7: Hangman project.
print( '''                                       
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   ''' )

import hangman_words
import random
word_list = hangman_words.word_list
word = random.randint(0, len(word_list) - 1)        # or use random.choicw()
chosen_word = word_list[word]
chosen_word = chosen_word.lower()


output = []
for i in range(0, len(chosen_word)):
    output += '_'
print(output)


HANGMAN_PICS = [r'''
  +---+

  |   |
      |

      |
      |
      |
=========''', r'''
  +---+

  |   |
  O   |

      |
      |
      |
=========''', r'''
  +---+

  |   |
  O   |

  |   |
      |

      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |

      |
      |
=========''', r'''
  +---+

  |   |
  O   |
 /|\  |

      |
      |
=========''', r'''
  +---+

  |   |
  O   |
 /|\  |
 /    |

      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

lives = 6
end_of_game = False

while end_of_game == False:
    guess = input('Guess a letter?').lower()

    for p in range(0, len(chosen_word)):
        if guess == chosen_word[p]:
            output[p]= guess
    
    print(output)      

    if guess not in  chosen_word:
        print(HANGMAN_PICS[-lives])
        lives -= 1
        print(f'woops! wrong guess....You have {lives} lives left')  
        print(output)   

    if lives == 0:
        end_of_game = True
        print('You lose!')

    if '_' not in output:
        end_of_game = True
        print('You win!')

print(f'The word is: {word_list[word]}')