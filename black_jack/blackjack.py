from deck import deck
import questionary

def sumHand(hand):
    ace_count = 0
    sum = 0 
    for i in hand:
        if i.value == 1:
            ace_count += 1
            sum +=1
        elif i.value > 10:
            sum += 10
        else:
            sum += i.value
    for i in range(ace_count):
        if sum + 10 <=21:
            sum += 10
    return sum
def draw(pile):
    try:
        return deck.draw()
    except:
        print("aa"+str(pile))
        print("bb"+str(deck))
def player_turn():
    global player_hand
    global player_busted
    player_hand.append(draw(deck))
    print("you drew: " + str(player_hand[-1]))
    player_hand.append(draw(deck))
    print("you drew: " + str(player_hand[-1]))
    while True:
        if sumHand(player_hand) > 21:
            print("you busted. now i can feed little timmy. thank you ")
            player_busted = True
            break
        print("your hand: " + str(player_hand))
        print("your hand sums to: " + str(sumHand(player_hand)))
        action =  questionary.select(
            "what would you like to do",
            choices=[
                "hit",
                "stay",
                "cheat",
            ],
            ).ask()
        if action == "hit":
            player_hand.append(draw(deck))
            print("you drew: " + str(player_hand[-1]))
        elif action == "cheat":
            print(deck.cheatLook())
        else:
            action =  questionary.select(
            "are you sure you want to stay",
            choices=[
                "no",
                "yes",
            ],
            ).ask()
            if action == "yes":
                action =  questionary.select(
                "are you really sure you want to stay? i have a freind who could've goten 10 million dollars, but she chose to stay",
                choices=[
                    "no",
                    "yes",
                ],
                ).ask()
                if action == "yes":
                    action =  questionary.select(
                    "i need to feed my family, please keep going, i dont have health insurence and the only way i can afford my sons cancer treatment is if you go out",
                    choices=[
                        "no",
                        "yes",
                    ],
                    ).ask()
                    if action == "yes":
                        print("timmy is going to die becouse of you, you monster")
                        break
def dealer_turn():
    global dealer_hand
    global dealer_busted
    while sumHand(dealer_hand) <= sumHand(player_hand) and sumHand(dealer_hand) <21:
        dealer_hand.append(draw(deck))
        print("the dealer drew: " + str(dealer_hand[-1]))
        print("the dealer has:  " + str(dealer_hand))
        if sumHand(dealer_hand) > 21:
            dealer_busted = True
            break
player_hand = []
dealer_hand = []
playing = True
is_player_turn = True
player_busted = False
dealer_busted = False
deck = deck()
deck.shuffle()
player_turn()
if player_busted == True:
    print("you busted. you lost")
elif sumHand(player_hand) == 21:
    print("you got 21 and won")
else:
    dealer_turn()
    if dealer_busted == True:
        print("the dealer busted. you win")
    elif sumHand(dealer_hand) == True:
        print("the dealer got 21. you lose")
    elif sumHand(player_hand) > sumHand(dealer_hand):
        print("you had the higher hand. you win")
    elif sumHand(player_hand) < sumHand(dealer_hand):
        print("you had the lower hand. you lose")
    else:
        print("fix the edge case")
    