import random

cards = ["ACE", 2, 3, 4, 5, 6, 7, 8, 9, 10, "JACK", "QUEEN", "KING", "ACE", 2, 3, 4, 5, 6, 7, 8, 9, 10, "JACK", "QUEEN", "KING", "ACE", 2, 3, 4, 5, 6, 7, 8, 9, 10, "JACK", "QUEEN", "KING", "ACE", 2, 3, 4, 5, 6, 7, 8, 9, 10, "JACK", "QUEEN", "KING"]
suits = ['Hearts', 'Diamond', 'Clubs', 'Spades']
names = ["Bob", 'Bender', 'Loki', 'Captain Shepard', 'Joel', 'Ken', 'Ryan', 'Harley']
r_name = None
g_name =  None
hand = None 
r_hand = None
card1 = None
card1_suit = None
card1r = None
card1r_suit = None
card2g = None
card3g = None
card4g = None
card5g = None
card2_suit = None
card3_suit = None
card4_suit = None
card5_suit = None

def main():
    print("Dealer: Welcome to the PvP version of BlackJack!")
    global g_name 
    g_name = input('Dealer: What should we call you?')
    global r_name
    r_name = random.choice(names)
    print("Dealer: Well,", g_name, "today you are going to play against", r_name)
    print(' ')
    print('First, let me deal 1 card to each of you...')
    print(r_name, ":" "HOLD ON! By the way,", g_name, "do you know the rules of PvP BlackJack?")
    choice1 = input("Dealer: If you are not familiar, pleaase type 'rules', if you know the rules, type anything else.")
    if choice1.lower() == 'rules':
        print(' ')
        rules() 
    else: 
        print(' ')
        first()
    
def rules():
    print(r_name, ": " "heh", g_name, "you start playing the game without knowing the rules???")
    print("* Dealer start explaing you the rules of PvP BlackJack *")
    print("Welcome to PvP Blackjack! It's not just a game; it's a showdown between you and the computer dealer. Here's how to roll:")
    print("1. Goal is to get closer to 21 than opponent without going over 21.")
    print("2. Standard 52 card deck. Card values: Number cards are face value. Face cards are 10 points. Aces are 1 or 11 points.")
    print("3. Dealer deals 1 card face up to first player, then 1 card to second player.")
    print("4. First player takes turns asking dealer for more cards to improve hand.") 
    print("5. Can DRAW (take card) or HOLD (keep current hand).")
    print("6. After first player is done, second player follows same process.")
    print("7. If you go over 21, you bust and automatically lose.")
    print("8. If neither player busts, whoever is closer to 21 without going over wins.")
    print("9. If one player busts but the other doesn't, the player who hasn't busted wins.")
    first()

def first():
    print(" ")
    print("Dealer: Now, when we establish that all players know the rules, let's start!")
    print('* First, dealer start dealing 1 card to each of you... *')
        #user pick
    global card1
    card1 = random.choice(cards)
    if card1 == 'KING': 
        card1 = 10
    elif card1 == 'JACK':
        card1 = 10
    elif card1 == 'QUEEN':
        card1 = 10
    elif card1 == 'ACE': 
        card1 = 11
    global card1_suit
    card1_suit = random.choice(suits)
    #our pick
    global card1r
    card1r = random.choice(cards)
    if card1r == 'KING': 
        card1r = 10
    elif card1r == 'JACK':
        card1r = 10
    elif card1r == 'QUEEN':
        card1r = 10
    elif card1r == 'ACE': 
        card1r = 11
    global card1r_suit
    card1r_suit = random.choice(suits)
    print("In your hand you currently have:", card1, "of", card1_suit)
    print("This is equal to:", card1)
    print('   ')
    print("Your opponent", r_name, "have:", card1r, 'of', card1r_suit)
    print('This is equal to:', card1r)
    print('   ')
    global hand
    hand = card1
    global r_hand 
    r_hand = card1r
    choice2 = input("Dealer: Do you want to draw again? Reply DRAW to draw one more card, HOLD to withhold. ")
    if choice2.lower() == "draw":
        second()
    else:
        r_final()
    
def second():
    print(" ")
    print("Dealer: Since", g_name, "want to draw a card...")
    print('* The dealer deal 1 more card for you *')
        #user pick
    card2 = random.choice(cards)
    if card2 == 'KING': 
        card2 = 10
    elif card2 == 'JACK':
        card2 = 10
    elif card2 == 'QUEEN':
        card2 = 10
    elif card2 == 'ACE': 
        if card1 < 11: 
            card2 = 11
        else:
            card2 = 1
    global card2_suit
    card2_suit = random.choice(suits)
    global card2g
    card2g = card2
    print(' ')
    print("* The new card that was dealt to you is ", card2, "of", card2_suit, "*")
    print("In your hand you currently have:", card1, "of", card1_suit, "and", card2, "of", card2_suit)
    hand = card1 + card2
    print("This is equal to:", hand)
    print('   ')
    choice3 = input("Do you want to draw again? Type DRAW for 1 more card, HOLD to keep your hand ")
    if choice3.lower() == "draw":
        third()
    else: 
        r_final() 

def third():
    print(" ")
    print("Dealer: Since", g_name, "want to draw a card...")
    print('* The dealer deal 1 more card for you *')
        #user pick
    card3 = random.choice(cards)
    if card3 == 'KING': 
        card3 = 10
    elif card3 == 'JACK':
        card3 = 10
    elif card3 == 'QUEEN':
        card3 = 10
    elif card3 == 'ACE': 
        if (card1 + card2g) < 11: 
            card3 = 11
        else:
            card3 = 1
    global card3g
    card3g = card3
    card3_suit = random.choice(suits)
    print(' ')
    print("* The new card that was dealt to you is ", card3, "of", card3_suit, "*")
    print("In your hand you currently have:", card1, "of", card1_suit, ",", card2g, "of", card2_suit, 'and', card3, 'of', card3_suit)
    hand = card1 + card2g + card3
    print("This is equal to:", hand)
    print('   ')
    if hand > 21:
        print("Oh nooo! Looks like you have more than 21 in your hand! You lose...")
        print("Let's see if", r_name, "will loose as well...")
        print(" ")
        r_final()
    else:
        choice4 = input("Do you want to draw again? Type DRAW for 1 more card, HOLD to keep your hand ")
        if choice4.lower() == "draw":
            fourth()
        else: 
            r_final()

def fourth():
    print(" ")
    print("Dealer: Since", g_name, "want to draw a card...")
    print('* The dealer deal 1 more card for you *')
        #user pick
    card4 = random.choice(cards)
    if card4 == 'KING': 
        card4 = 10
    elif card4 == 'JACK':
        card4 = 10
    elif card4 == 'QUEEN':
        card4 = 10
    elif card4 == 'ACE': 
        if (card1 + card2g + card3g) < 11: 
            card4 = 11
        else:
            card4 = 1
    global card4g
    card4g = card4
    card4_suit = random.choice(suits)
    print(' ')
    print("* The new card that was dealt to you is ", card4, "of", card4_suit, "*")
    print("In your hand you currently have:", card1, "of", card1_suit, ",", card2g, "of", card2_suit, card3g, 'of', card3_suit, 'and', card4, 'of', card4_suit)
    hand = card1 + card2g + card3g + card4
    print("This is equal to:", hand)
    print('   ')
    if hand > 21:
        print("Oh nooo! Looks like you have more than 21 in your hand! you lose...")
        print("Let's see if", r_name, "will loose as well...")
        print(" ")
        r_final()
    else:
        choice5 = input("Do you want to draw again? type DRAW for 1 more card, HOLD to keep your hand ")
        if choice5.lower() == "draw":
            fifth()
        else: 
            r_final()

def fifth():
    print(" ")
    print("Dealer: Since", g_name, "want to draw a card...")
    print('* The dealer deal 1 more card for you *')
        #user pick
    card5 = random.choice(cards)
    if card5 == 'KING': 
        card5 = 10
    elif card5 == 'JACK':
        card5 = 10
    elif card5 == 'QUEEN':
        card5 = 10
    elif card5 == 'ACE': 
        if hand < 11: 
            card5 = 11
        else:
            card5 = 1
    card5_suit = random.choice(suits)
    print(' ')
    print("* The new card that was dealt to you is ", card5, "of", card5_suit, "*")
    print("In your hand you currently have:", card1, "of", card1_suit, ",", card2g, "of", card2_suit, card3g, 'of', card3_suit, ',', card4g, 'of', card4_suit, 'and', card5, 'of', card5_suit)
    hand = card1 + card2g + card3g + card4g + card5
    print("This is equal to:", hand)
    print('   ')
    if hand > 21:
        print("Oh nooo! Looks like you have more than 21 in your hand! you lose...")
        print("Let's see if", r_name, "will loose as well...")
        print(" ")
        r_final()
    else:
        choice5 = input("Do you want to draw again? type DRAW for 1 more card, HOLD to keep your hand ")
        if choice5() == "DRAW":
            fifth()
        else: 
            r_final()  

def r_final():
    print("Dealer: Since", g_name, "will not draw new cards, I will start dealing to", r_name)
    print("* Dealer deal new card to", r_name, "*")
    card2r = random.choice(cards)
    if card2r == 'KING': 
        card2r = 10
    elif card2r == 'JACK':
        card2r = 10
    elif card2r == 'QUEEN':
        card2r = 10
    elif card2r == 'ACE': 
        if card1r < 11: 
            card2r = 11
        else:
            card2r = 1
    card2r_suit = random.choice(suits)
    print(' ')
    print("* new card that was deal is ", card2r, "of", card2_suit, "*")
    print(r_name, "currenlty have", card1r, "of", card1r_suit, "and", card2r, "of", card2r_suit)
    hand_r = card1r + card2r
    print("This is equal to:", hand_r)
    print('   ')
    if hand_r > 21:
        print("Dealer: Unfortunetely", r_name, "have more than 21")
        end()
    if hand_r < 17:
        print(r_name, ": I wanna draw again!")
        print('* Dealer deal new card to', r_name)
        card3r = random.choice(cards)
        if card3r == 'KING': 
            card3r = 10
        elif card3r == 'JACK':
            card3r = 10
        elif card3r == 'QUEEN':
            card3r = 10
        elif card3r == 'ACE': 
            if hand_r < 11: 
                card3r = 11
            else:
                card3r = 1
        card3r_suit = random.choice(suits)
        print(' ')
        print("* new card that was deal is ", card3r, "of", card3_suit, "*")
        print(r_name, "currenlty have", card1r, "of", card1r_suit, ',', card2r, 'of', card2_suit, "and", card3r, "of", card3r_suit)
        hand_r = card1r + card2r + card3r
        print("This is equal to:", hand_r)
        print('   ')
        if hand_r > 21:
            print("Dealer: Unfortunetely", r_name, "have more than 21")
            end()
        if hand_r < 17:
            print(r_name, ": I wanna draw again!")
            print('* Dealer deal new card to', r_name)
            card4r = random.choice(cards)
            if card4r == 'KING': 
                card4r = 10
            elif card4r == 'JACK':
                card4r = 10
            elif card4r == 'QUEEN':
                card4r = 10
            elif card4r == 'ACE': 
                if card4r < 11: 
                    card4r = 11
                else:
                    card4r = 1
            card4r_suit = random.choice(suits)
            print(' ')
            print("* new card that was deal is ", card4r, "of", card4_suit, "*")
            print(r_name, "currenlty have", card1r, "of", card1r_suit, ',', card2r, 'of', card2_suit, ',', card3r, 'of', card3r_suit, "and", card4r, "of", card4r_suit)
            hand_r = card1r + card2r + card3r + card4r
            print("This is equal to:", hand_r)
            print('   ')
            print(r_name, ": HOLD! I'm done")
            end()
    else: 
        print(r_name, ": HOLD! I'm done")
        end()

def end():
    if hand <= 21: 
        print("Dealer: Since both platers have full hands, times to establish the winner!")
        if hand == r_hand:
            print("Dealer: Since both players have equal hands, I declare TIE!")
            print("Congradualtions", g_name, 'and', r_name, '!')
            print(r_name, ": Heh, nice game", g_name, "! I hope to play with you again")
            print("Dealer:", g_name, "would you like to play again?")
            final_choice = input('Type AGAIN, to play again, or STOP, to end the game')
            if final_choice.lower() == 'again':
                main()
            else: 
                print("Deaeler: Thank you for playing!")
        elif hand > r_hand:
            print("Dealer:", g_name, "WON the game!")
            print("Congradualtions", g_name, '! For destroying', r_name, '!')
            print(r_name, ": Heh, nice game", g_name, "! I hope to play with you again")
            print("Dealer:", g_name, "would you like to play again?")
            final_choice = input('Type AGAIN, to play again, or STOP, to end the game')
            if final_choice == 'AGAIN':
                main()
            else: 
                print("Deaeler: Thank you for playing champion!")
        elif hand< r_hand:
            print("Dealer:", r_name, "WON the game!")
            print("Congradualtions", r_name, '! For destroying', g_name, '!')
            print(r_name, ": Heh, nice game", g_name, "! I hope to play with you again")
            print("Dealer:", g_name, "would you like to play again?")
            final_choice = input('Type AGAIN, to play again, or STOP, to end the game')
            if final_choice() == 'AGAIN':
                main()
            else: 
                print("Deaeler: Thank you for playing!")
    elif hand > 21:
        if r_hand <= 21:
            print("Dealer: well, since ", g_name, "have more than 21,", r_name, 'WON!' )
            print(r_name, ": Heh, nice game", g_name, "! I hope to play with you again")
            print("Dealer:", g_name, "would you like to play again?")
            final_choice = input('Type AGAIN, to play again, or STOP, to end the game')
            if final_choice() == 'AGAIN':
                main()
            else: 
                print("Deaeler: Thank you for playing!")
        if r_hand > 21: 
            print("Dealer: Since both players have more than 21, NOBODY WON!")
            print(r_name, ": Heh, nice game", g_name, "! I hope to play with you again")
            print("Dealer:", g_name, "would you like to play again?")
            final_choice = input('Type AGAIN, to play again, or STOP, to end the game')
            if final_choice() == 'AGAIN':
                main()
            else: 
                print("Deaeler: Thank you for playing!")

if __name__ == "__main__": #this function intiate our code
    main()