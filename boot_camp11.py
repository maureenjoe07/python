# CAPSTONE CHALLANGE.
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |           | |   | |          | |  (_)          | |   
|( \/ )|           | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  / |           | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ A|           | |_) | | (_| | (__|   <| | (_| | (__|   < 
`------'           |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                                          _/ |                
                                         |__/                 
"""
print(logo)
import random
def your_selection():
    your_card = []
    for i in range(0,2):
        cards = random.randint(1,10)
        your_card.append(cards)
    return your_card

def comp_selection():
    comp_card = []
    cards = random.randint(1,10)
    comp_card.append(cards)
    return comp_card

def choice_extend():
    cards = random.randint(1,10)
    my_hand.append(cards)
    return my_hand

def comp_addition():
    cards = random.randint(1,10)
    comp_hand.append(cards)
    return comp_hand

if input('Enter "y" if you want to play BLACKJACK or "n" if otherwise: ').lower() == 'y':
    my_hand = your_selection()
    comp_hand = comp_selection()
    print(f' Your card: {my_hand}')
    print(f"Computer's card: {comp_hand}")
    if input('Enter "y" if you want to pick another card or "n" if otherwise: ').lower() == 'y':
        my_hand = choice_extend()
        comp_hand = comp_addition()
        print(f' Your card: {my_hand}')
        print(f" computer's card: {comp_hand}")
    else:
        my_hand = your_selection()
        comp_hand =  comp_addition()
        print(f' Your card: {my_hand}')
        print(f"computer's card: {comp_hand}")

    my_final_hand = 0
    for num in range(0, len(my_hand)):
        my_final_hand += my_hand[num]
            
    print(my_final_hand)

    comp_final_hand = 0
    for num in range(0, len(comp_hand)):
        comp_final_hand += comp_hand[num]
        
    print(comp_final_hand)

    if my_final_hand <= 21 and my_final_hand > comp_final_hand:
        print('You win!')
    elif my_final_hand == comp_final_hand:
        print("It's a draw")
    else:
        print('You lose!')
else:
    print('Exist game. Thank you!')