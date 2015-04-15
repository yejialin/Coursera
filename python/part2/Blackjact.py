# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
score = 0
go = 0
state = 0
outcome = ["", "You lose", "You went bust and lose", "You win"]
choice = ["Hit or Stand", "New deal?"]
explored = True
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
        
    def draw_dark(self, canvas, pos):
        card_loc = (CARD_CENTER[0], CARD_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
 
# define hand class
class Hand:
    def __init__(self):
        self.card1 = []
        self.card2 = []
        
    def __str__(self):
        self.str = ""
        for i in range(len(self.card1)):
            for j in range(2):
                self.str += self.card1[i][j]
            self.str += " "
        return "Hand contains " + self.str
        
    def add_card(self, card):
        self.card1.append((card.suit, card.rank))
        self.card2.append(card) 
        
    def get_value(self):
        i = 0
        value_list = []
        value = 0
        for i in range(len(self.card1)):
            value_list.append(self.card1[i][1])
            value += VALUES[value_list[i]]
        if not("A" in value_list):
            return value
        else:
            if value + 10 <= 21:
                return value + 10
            else:
                return value
            
    def draw(self, canvas, pos):
        for i in range(len(self.card2)):
            self.card2[i].draw(canvas, [pos[0] + i*80, pos[1]])
            
        
# define deck class 
class Deck:
    def __init__(self):
        self.card = []
        i = 0
        j = 0
        while i < len(SUITS):
            while j < len(RANKS):
                self.card.append((SUITS[i], RANKS[j]))
                j += 1
            j = 0
            i += 1
                
    def shuffle(self):
        random.shuffle(self.card) 

    def deal_card(self):
        temp = self.card.pop()
        return Card(temp[0], temp[1])
            
    def __str__(self):
        self.str = ""
        for i in range(len(self.card)):
            for j in range(2):
                self.str += self.card[i][j]
            self.str += " "
        return "Dect contains " + self.str
        
#define event handlers for buttons
def deal():
    global state, go, score, index1, index2, explored
    if (state == 0 and
        go == 0):
        init()
        deck.shuffle()
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        state = 1
    elif (state == 1 and 
          go == 1):
        player.add_card(deck.deal_card())
        go = 0
        if player.get_value() > 21:
            score -= 1
            state = 0
            index1 = 2
            index2 = 1
            explored = False
    elif state == 2:               
        go = 0
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if (dealer.get_value() > 21 or
            dealer.get_value() < player.get_value()):
            score += 1
            index1 = 3
            index2 = 1
        else:
            score -= 1
            index1 = 1
            index2 = 1
        state = 0

def hit():
    global go
    if state != 0:
        go = 1
        deal()
    
def stand():
    global state, explored
    if state == 1:
        state = 2
        deal()
    explored = False
           
def draw(canvas):
    canvas.draw_text("Blackjact", (100, 90), 45, "Aqua")
    canvas.draw_text("Score "+str(score), (400, 90), 30, "Black")
    canvas.draw_text("Dealer", (80, 150), 30, "Black")
    canvas.draw_text("Player", (80, 400), 30, "Black")
    canvas.draw_text(outcome[index1], (220, 150), 30, "Black")
    canvas.draw_text(choice[index2], (220,400), 30, "Black")       
    dealer.draw(canvas, [80, 205])
    player.draw(canvas, [80, 425])
    if explored:
        dealer.card2[0].draw_dark(canvas, [80, 205])
    
def init():
    global deck, dealer, player, index1, index2, explored
    index1 = 0
    index2 = 0
    deck = Deck()
    dealer = Hand()
    player = Hand()
    explored = True
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
init()
deal()
frame.start()
