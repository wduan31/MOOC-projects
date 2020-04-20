# http://www.codeskulptor.org/#user31_Pzsnb0YwKJ_2.py

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ["",""]
score = 0


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
    
    def __str__(self):
        s = "Hand contains"
        for i in self.cards:
            s += " " + str(i.suit) + str(i.rank)
        return s
    def add_card(self,card):
        self.cards.append(card)
    def remove_card(self,index):
        if index < (len(self.cards) - 1):
            self.cards.remove(index)
    def get_value(self):
        v = 0
        a = 0
        for i in self.cards:
            v += int(VALUES.get(i.rank))
            if i.rank == "A":
                a += 1
        if (a > 0) and ((v + 10) <= 21):
            v += 10
        return v 
    def draw(self,canvas,pos):
        for i in range(len(self.cards)):
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.cards[i].rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.cards[i].suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0]*2*i, pos[1] + CARD_CENTER[1]], CARD_SIZE)
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for i in SUITS:
            for j in RANKS:
                self.cards.append(Card(i,j))
    def shuffle(self):
        random.shuffle(self.cards)
    def __str__(self):
        s = "Deck contains"
        for i in self.cards:
            s += " " + str(i.suit) + str(i.rank)
        return s
    def deal_card(self):
        return self.cards.pop()

p_hand = Hand()
d_hand = Hand()
deck = Deck()
    
#define event handlers for buttons

def deal():
    global outcome, in_play, score, p_hand, d_hand, deck
    p_hand = Hand()
    d_hand = Hand()
    deck = Deck()
    # your code goes here
    if (in_play):
        score -= 1
    outcome[0] = ""
    outcome[1] = "Hit or Stand?"
    in_play = True
    deck.shuffle()
    d_hand.add_card(deck.deal_card())
    p_hand.add_card(deck.deal_card())
    d_hand.add_card(deck.deal_card())
    p_hand.add_card(deck.deal_card())

def new_game():
    global outcome, in_play, score, p_hand, d_hand, deck
    in_play = False
    outcome = ["",""]
    score = 0
    deal()
        
def hit():
    # replace with your code below
    global outcome, in_play, score, p_hand, deck
    # if the hand is in play, hit the player
    if (in_play):
        p_hand.add_card(deck.deal_card())
    # if busted, assign a message to outcome, update in_play and score
        if (p_hand.get_value() > 21):
            outcome = ["You went bust and lose","New deal?"]
            in_play = False
            score -= 1
    else:
        outcome[0] = "A New Deal?"   
def stand():
    # replace with your code below
    global outcome, in_play, score, p_hand, d_hand, deck
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if (in_play):
        while (d_hand.get_value() < 17):
            d_hand.add_card(deck.deal_card())
        if (d_hand.get_value() > 21):
            outcome = ["Dealer went bust","New deal?"]
            in_play = False
            score += 1
        elif (p_hand.get_value() <= d_hand.get_value()):
            outcome = ["You lose","New deal?"]
            in_play = False
            score -= 1
        else:
            outcome = ["You win","New deal?"]
            in_play = False
            score += 1  
# assign a message to outcome, update in_play and score
    else:
        outcome[0] = "A New Deal?" 
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", [120,100],50,"Aqua")
    s = "Score "+str(score) 
    canvas.draw_text(s, [400,100],30,"Black")
    canvas.draw_text("Dealer", [100,170],30,"Black")
    canvas.draw_text("Player", [100,370],30,"Black")
    canvas.draw_text(outcome[0], [250,170],30,"Black")
    canvas.draw_text(outcome[1], [250,370],30,"Black")
    d_hand.draw(canvas,[150,200])
    p_hand.draw(canvas,[150,400])
    if (in_play):
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [150,(200+CARD_BACK_CENTER[1])],CARD_BACK_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Reset", new_game, 200)
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
new_game()
frame.start()


# remember to review the gradic rubric
