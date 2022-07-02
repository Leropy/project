#import os       # Koristeno prilikom testiranja
from tkinter import *
import random
from tkinter import *
from PIL import Image, ImageTk  # pip install Pillow

#os._exit(00)    # Ukoliko dodje do greske run-ovati kod sa ovom linijom aktivnom da bi se restartovao kernel

global VELICINA_FONTA


VELICINA_FONTA = 13     # PODESAVANJE FONTA <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'Jack', 'Queen', 'King', 'Ace')

values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
          '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

# =======================================================================================================   # KLASE <-------------------

class Card:     # Creates all the cards
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + '_of_' + self.suit
    
class Deck:     # Creates a deck of cards

    def __init__(self):
        self.deck = []      # creates a empty deck first
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    

class Hand:
    def __init__(self):
        self.cards = []
        self.sum = 0
        self.aces = 0       # ace indicator
        
    def add_card(self, card):
        self.cards.append(card)
        self.sum += values[card.rank]
        
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_ace(self):
        while self.sum > 21 and self.aces:
            self.sum -= 10
            self.aces -= 1
            

class Chips:
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
   
    def lose_bet(self):
        self.total -= self.bet
        
    def blackjack_win_bet(self):
        self.bet *= 2
        self.total += self.bet
      

# =======================================================================================================   # FUNKCIJE <-------------------

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def take_bet(chips):
    
    while len(bet_entry.get()) > 0:
        try:
            chips.bet = int(bet_entry.get())
        except ValueError:
            bet_entry.delete(0,END)
            messagebox.showinfo(title="Error_1", message="Enter only whole numbers!")
            bet_entry.delete(0,END)
            continue
            
        else:
            if chips.bet > chips.total:
                bet_entry.delete(0,END)
                messagebox.showinfo(title="Error_2", message="Not enought funds!")
                bet_entry.delete(0,END)
                continue
            
            elif chips.bet <= 0:
                bet_entry.delete(0,END)
                messagebox.showinfo(title="Error_3", message="Use only positive numbers!")
                bet_entry.delete(0,END)
                continue
                
            else:
                break
            
    
def show_some(player, dealer):
    global dealer_image_1
    global dealer_image_2
    dealer_image_1 = resize_card(f'PNG-cards-1.3/{dealer.cards[1]}.png')
    dealer_label_1.config(image=dealer_image_1)
    dealer_image_2 = resize_card(f'PNG-cards-1.3/back.png')
    dealer_label_2.config(image=dealer_image_2)
    
    global player_image_1
    global player_image_2
    global player_image_3
    global player_image_4
    global player_image_5
    player_image_1 = resize_card(f'PNG-cards-1.3/{player.cards[0]}.png')
    player_label_1.config(image=player_image_1)
    if len(player.cards)>1:
        player_image_2 = resize_card(f'PNG-cards-1.3/{player.cards[1]}.png')
        player_label_2.config(image=player_image_2)
    if len(player.cards)>2:
        player_image_3 = resize_card(f'PNG-cards-1.3/{player.cards[2]}.png')
        player_label_3.config(image=player_image_3)
    if len(player.cards)>3:
        player_image_4 = resize_card(f'PNG-cards-1.3/{player.cards[3]}.png')
        player_label_4.config(image=player_image_4)
    if len(player.cards)>4:
        player_image_5 = resize_card(f'PNG-cards-1.3/{player.cards[4]}.png')
        player_label_5.config(image=player_image_5)
        
def show_some_split(player, dealer):
    global dealer_image_1
    global dealer_image_2
    dealer_image_1 = resize_card(f'PNG-cards-1.3/{dealer.cards[1]}.png')
    dealer_label_1.config(image=dealer_image_1)
    dealer_image_2 = resize_card(f'PNG-cards-1.3/back.png')
    dealer_label_2.config(image=dealer_image_2)
    
    global player_image_1_split
    global player_image_2_split
    global player_image_3_split
    global player_image_4_split
    global player_image_5_split
    player_image_1_split = resize_card(f'PNG-cards-1.3/{player.cards[0]}.png')
    player_label_1_split.config(image=player_image_1_split)
    if len(player.cards)>1:
        player_image_2_split = resize_card(f'PNG-cards-1.3/{player.cards[1]}.png')
        player_label_2_split.config(image=player_image_2_split)
    if len(player.cards)>2:
        player_image_3_split = resize_card(f'PNG-cards-1.3/{player.cards[2]}.png')
        player_label_3_split.config(image=player_image_3_split)
    if len(player.cards)>3:
        player_image_4_split = resize_card(f'PNG-cards-1.3/{player.cards[3]}.png')
        player_label_4_split.config(image=player_image_4_split)
    if len(player.cards)>4:
        player_image_5_split = resize_card(f'PNG-cards-1.3/{player.cards[4]}.png')
        player_label_5_split.config(image=player_image_5_split)
    
    
    
    
def show_all(player, dealer):
    global player_image_1
    global player_image_2
    global player_image_3
    global player_image_4
    global player_image_5
    global dealer_image_1
    global dealer_image_2
    global dealer_image_3
    global dealer_image_4
    global dealer_image_5
    dealer_image_1 = resize_card(f'PNG-cards-1.3/{dealer.cards[0]}.png')
    dealer_label_1.config(image=dealer_image_1)
    if len(dealer.cards)>1:
        dealer_image_2 = resize_card(f'PNG-cards-1.3/{dealer.cards[1]}.png')
        dealer_label_2.config(image=dealer_image_2)
    if len(dealer.cards)>2:
        dealer_image_3 = resize_card(f'PNG-cards-1.3/{dealer.cards[2]}.png')
        dealer_label_3.config(image=dealer_image_3)
    if len(dealer.cards)>3:
        dealer_image_4 = resize_card(f'PNG-cards-1.3/{dealer.cards[3]}.png')
        dealer_label_4.config(image=dealer_image_4)
    if len(dealer.cards)>4:
        dealer_image_5 = resize_card(f'PNG-cards-1.3/{dealer.cards[4]}.png')
        dealer_label_5.config(image=dealer_image_5)
        

# GAME OUTCOMES


def player_busts(player, dealer, chips):
    bet_label.configure(text="PLAYER BUSTED!", bg='dark red', padx=25, pady=25)
    chips.lose_bet()
    
def player_wins(player, dealer, chips):
    bet_label.configure(text="PLAYER WON!", bg='blue', padx=25, pady=25)
    chips.win_bet()
    
def dealer_busts(player, dealer, chips):
    bet_label.configure(text="DEALER BUSTED!", bg='blue', padx=25, pady=25)
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    bet_label.configure(text="DEALER WON!", bg='dark red', padx=25, pady=25)
    chips.lose_bet()
    
def push(player, dealer):
    bet_label.configure(text="PUSH (DRAW)!", bg='orange', padx=25, pady=25)

def player_blackjack_win(player, dealer, chips):
    bet_label.configure(text="PLAYER WON WITH BLACKJACK!", bg='purple', padx=25, pady=25)
    chips.blackjack_win_bet()
    

#---------------------------------------------------------------------------------------------------------------------------------------------------

global player_chips, deck, player_hand, player_hand_split, dealer_hand

player_chips = Chips()

root = Tk()
root.title('BlackJack')
#root.geometry("1200x900")
root.configure(background='green')
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())

# Promjena velicine skila
def resize_card(card):
    card_img = Image.open(card)
    card_img_resized = card_img.resize((150,218))
    global card_picture
    card_picture = ImageTk.PhotoImage(card_img_resized)
    return card_picture


# Frejmovi za prikaza karata i opcija

main_frame = Frame(root, bg='green')
main_frame.pack(pady=20)

dealer_frame = LabelFrame(main_frame, text=f'DEALER: ?', bd=0, bg='green', fg='white', font=('Verdana',VELICINA_FONTA,'bold'))
dealer_frame.grid(row=0, column=0, pady=20, columnspan=2)

player_frame = LabelFrame(main_frame, text=f'PLAYER: ?', bd=0, bg='green', fg='white', font=('Verdana',VELICINA_FONTA,'bold'))
player_frame.grid(row=1, column=0)

player_frame_split = LabelFrame(main_frame, text=f'PLAYER: ?', bd=0, bg='green', fg='white', font=('Verdana',VELICINA_FONTA,'bold'))

choice_frame = Frame(root, bg='dark green', highlightbackground='white', highlightthickness=2)
choice_frame.pack(side=BOTTOM, pady=(10,30))

# Tasteri za opcije----------------------------------------------------------------------------- BUTTONS AND ENTERIES------------------------

def deal_button():
    
    global player_chips,deck,player_hand,player_hand_split,dealer_hand

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand_split = Hand()
    dealer_hand = Hand()
    
    player_hand_split.sum = 22
    
    take_bet(player_chips)
    
    if len(bet_entry.get()) > 0:
    
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        
        ############################################################################################  ZONA ZA TESTIRANJE!!!!!!!!!!!!!!!<<<<<<<<<<<<<
        #player_hand.cards[0].rank='2'
        #player_hand.cards[0].suit='spades'
       
        #player_hand.cards[1].rank='2'
        #player_hand.cards[1].value='hearts'
        
        #player_hand.sum = 4
        ############################################################################################  ZONA ZA TESTIRANJE!!!!!!!!!!!!!!! <<<<<<<<<<<<
        
        player_hand.adjust_for_ace()
        
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
       
        show_some(player_hand, dealer_hand)
        
        if values[player_hand.cards[0].rank] == values[player_hand.cards[1].rank]:
            split_button.grid(row=0,column=2, padx=10, rowspan=2)
        
        if player_hand.sum < 21:
            hit_button.configure(state=NORMAL)
            hit_button.grid(row=0,column=0, pady=10, padx=(20,0))
            stand_button.grid(row=0,column=1, padx=20)
            double_down_button.grid(row=1,column=0,columnspan=2,pady=7,padx=20)
            deal_button.grid_forget() 
            bet_entry.grid_forget()  
            bet_label.grid_forget()
            
        player_frame.configure(text=f'PLAYER: {player_hand.sum}')
        gold_label.configure(text=f'CURRENT GOLD:  {player_chips.total} ({player_chips.bet})')
 
            
        if player_hand.sum == 21:
            stand_button_f()
            if dealer_hand.sum != player_hand.sum:
                player_blackjack_win(player_hand, dealer_hand, player_chips)
                gold_label.configure(text=f'CURRENT GOLD:  {int(player_chips.total-3/2*(player_chips.bet))} + {player_chips.bet}')
                player_chips.total -=  int(1/2*player_chips.bet)
                
            

def split_button():
    
    global  player_frame_split

    player_frame_split.grid(row=1, column=1, padx=(40,0))
    
    global player_label_1_split,player_label_2_split,player_label_3_split,player_label_4_split,player_label_5_split

    player_label_1_split.grid(row=0, column=0, pady=20, padx=20)

    player_label_2_split.grid(row=0, column=1, pady=20, padx=20)

    player_label_3_split.grid(row=0, column=2, pady=20, padx=20)

    player_label_4_split.grid(row=0, column=3, pady=20, padx=20)

    player_label_5_split.grid(row=0, column=4, pady=20, padx=20) 
    
    global player_hand_split
    player_hand_split = Hand()
    player_hand_split.add_card(deck.deal())
    
    player_hand_split.sum = int(player_hand.sum / 2)
    player_hand.sum = int(player_hand.sum / 2)
    player_hand_split.cards[0] = player_hand.cards[1]
    player_hand.cards.remove(player_hand.cards[1])
 
    if player_hand.cards[0].rank == 'Ace':
        player_hand.aces = 1
        player_hand_split.aces = 1
        player_hand.sum = 11
        player_hand_split.sum = 11
        player_hand_split.adjust_for_ace()
    
    player_label_2.config(image='')
    
    player_frame_split.configure(text=f'PLAYER: {player_hand_split.sum}')
    player_frame.configure(text=f'PLAYER: {player_hand.sum}')
    
    split_button.grid_forget()
    hit_button.configure(text='HIT LEFT', width=10, state=NORMAL)
    hit_button_split.grid(row=0,column=1, padx=10)
    hit_button_split.configure(state=NORMAL)
    stand_button.grid(row=1,column=0,columnspan=2, pady=10)
    double_down_button.grid_forget()
    
    show_some_split(player_hand_split, dealer_hand)
    show_some(player_hand, dealer_hand)



def hit_button_split():
    
    global player_hand_split
    hit(deck, player_hand_split)
    player_hand_split.adjust_for_ace()
    show_some_split(player_hand_split, dealer_hand)
    player_frame_split.configure(text=f'PLAYER: {player_hand_split.sum}')
    
    if player_hand_split.sum >= 21:
        hit_button_split.configure(state=DISABLED)
        
    check_for_player_bust()



        
def hit_button():
    
    split_button.grid_forget()

    hit(deck, player_hand)
    player_hand.adjust_for_ace()
    show_some(player_hand, dealer_hand)
    
    check_for_player_bust()
    
    if player_hand.sum >= 21:
        hit_button.configure(state=DISABLED)
        
   
    player_frame.configure(text=f'PLAYER: {player_hand.sum}')


def stand_button_f():
    
    if player_hand.sum <= player_hand_split.sum and player_hand_split.sum <= 21:
        player_hand.sum = player_hand_split.sum
        player_frame.grid_forget()
        player_frame_split.grid(row=1,column=0)
        
    
    while dealer_hand.sum <17:
        hit(deck, dealer_hand)

    show_all(player_hand, dealer_hand)
        
    if dealer_hand.sum >21:
        gold_label.configure(text=f'CURRENT GOLD:  {player_chips.total} + {player_chips.bet}')
        dealer_busts(player_hand, dealer_hand, player_chips)

    elif dealer_hand.sum > player_hand.sum:
        gold_label.configure(text=f'CURRENT GOLD:  {player_chips.total} - {player_chips.bet}')
        dealer_wins(player_hand, dealer_hand, player_chips)
            
    elif dealer_hand.sum < player_hand.sum:
        gold_label.configure(text=f'CURRENT GOLD:  {player_chips.total} + {player_chips.bet}')
        player_wins(player_hand, dealer_hand, player_chips)
            
    if player_hand.sum > 21:
        gold_label.configure(text=f'CURRENT GOLD:  {player_chips.total} - {player_chips.bet}')
        player_busts(player_hand, dealer_hand, player_chips)
        
    if player_hand.sum == dealer_hand.sum:
        gold_label.configure(text=f'CURRENT GOLD:  {player_chips.total} + 0')
        push(player_hand, dealer_hand)
    
    dealer_frame.configure(text=f'DEALER: {dealer_hand.sum}')
    player_frame.configure(text=f'PLAYER: {player_hand.sum}')

    hit_button.grid_forget()
    stand_button.grid_forget()
    bet_entry.grid_forget()
    deal_button.grid_forget()
    double_down_button.grid_forget()  
    split_button.grid_forget()
    hit_button_split.grid_forget()
    
    bet_label.grid(row=0,column=2,rowspan=2, padx=(20,0), pady=20)
    play_again_button.grid(row=0,column=4, rowspan=2, padx=20)
    

def play_again():
    
    bet_label.configure(text='Enter your bet:', bg='dark green', font=('Verdana',VELICINA_FONTA,'bold'))
    bet_label.grid(row=0,column=2,rowspan=2, padx=(20,0), pady=20)
    bet_entry.configure(state = NORMAL)
    bet_entry.delete(0,END)
    bet_entry.grid(row=0,column=3,rowspan=2, pady=25)
    play_again_button.grid_forget()
    deal_button.grid(row=0,column=4, rowspan=2, padx=20)
    deal_button.configure(state = NORMAL)
    dealer_frame.configure(text=f'DEALER: ?')
    player_frame.configure(text=f'DEALER: ?')
    
    dealer_label_1.config(image='')
    dealer_label_2.config(image='')
    dealer_label_3.config(image='')
    dealer_label_4.config(image='')
    dealer_label_5.config(image='')
    
    player_label_1.config(image='')
    player_label_2.config(image='')
    player_label_3.config(image='')
    player_label_4.config(image='')
    player_label_5.config(image='')
    
    player_label_1_split.config(image='')
    player_label_2_split.config(image='')
    player_label_3_split.config(image='')
    player_label_4_split.config(image='')
    player_label_5_split.config(image='')
    
    player_frame_split.grid_forget()
    player_frame.grid(row=1,column=0)
    hit_button.configure(text='HIT', width=5)
    
    global player_chips,deck,player_hand,dealer_hand
    
    del player_hand
    del dealer_hand
    
    
    gold_label.configure(text='CURRENT GOLD: {}'.format(player_chips.total))
    

def double_down_button():
        
    player_chips.bet *= 2
    bet_label.configure(text=f'Your bet is: {player_chips.bet}')
    hit(deck, player_hand)
    #player_hand.adjust_for_ace()
    show_some(player_hand, dealer_hand)
    
    check_for_player_bust()
    stand_button_f()
    
def check_for_player_bust():
    if player_hand.sum > 21 and player_hand_split.sum > 21:
        gold_label.configure(text=f'CURRENT GOLD:  {player_chips.total} - {player_chips.bet}')
        player_busts(player_hand, dealer_hand, player_chips)
        
        hit_button.grid_forget()
        stand_button.grid_forget()
        bet_entry.grid_forget()
        deal_button.grid_forget()
        double_down_button.grid_forget()
        hit_button_split.grid_forget()
        
        bet_label.grid(row=0,column=0, padx=10, pady=20)
        play_again_button.grid(row=0,column=3, padx=10)
        
        
        

gold_label = Label(text='CURRENT GOLD: {}'.format(player_chips.total), bg='green', fg='white', font=('Verdana',VELICINA_FONTA,'bold',))
gold_label.pack(side=BOTTOM)

hit_button = Button(choice_frame, text='HIT', width=5, command=hit_button, font=('Verdana',VELICINA_FONTA,'bold'))

stand_button = Button(choice_frame, text='STAND', width=7, command=stand_button_f, font=('Verdana',VELICINA_FONTA,'bold'))

double_down_button = Button(choice_frame, text='DOUBLE DOWN', width=13, command=double_down_button, font=('Verdana',VELICINA_FONTA,'bold'))

bet_label = Label(choice_frame, text='Enter your bet:', bg='dark green', fg='white', font=('Verdana',VELICINA_FONTA,'bold'), padx=25, pady=25)
bet_label.grid(row=0,column=2,rowspan=2, padx=(20,0), pady=20)
bet_entry = Entry(choice_frame, width=10, font=('Verdana',VELICINA_FONTA,'bold'))
bet_entry.grid(row=0,column=3,rowspan=2, pady=25)
        
deal_button = Button(choice_frame, text='DEAL', command=deal_button, font=('Verdana',VELICINA_FONTA,'bold'))
deal_button.grid(row=0,column=4, rowspan=2, padx=20)

split_button = Button(choice_frame, text='SPLIT', command=split_button, font=('Verdana',VELICINA_FONTA,'bold'))
hit_button_split = Button(choice_frame, text='HIT RIGHT', width=11, command=hit_button_split, font=('Verdana',VELICINA_FONTA,'bold'))

play_again_button = Button(choice_frame, text='PLAY AGAIN', command=play_again, font=('Verdana',VELICINA_FONTA,'bold'))

# Postavljanje karata u frejmove----------------------------------------------------------------------------------------------------------------

dealer_label_1 = Label(dealer_frame, text='', bg='green')
dealer_label_1.grid(row=0, column=0, pady=20, padx=20)

dealer_label_2 = Label(dealer_frame, text='', bg='green')
dealer_label_2.grid(row=0, column=1, pady=20, padx=20)

dealer_label_3 = Label(dealer_frame, text='', bg='green')
dealer_label_3.grid(row=0, column=2, pady=20, padx=20)

dealer_label_4 = Label(dealer_frame, text='', bg='green')
dealer_label_4.grid(row=0, column=3, pady=20, padx=20)

dealer_label_5 = Label(dealer_frame, text='', bg='green')
dealer_label_5.grid(row=0, column=4, pady=20, padx=20)

player_label_1_split = Label(player_frame_split, text='', bg='green')

player_label_2_split = Label(player_frame_split, text='', bg='green')

player_label_3_split = Label(player_frame_split, text='', bg='green')

player_label_4_split = Label(player_frame_split, text='', bg='green')

player_label_5_split = Label(player_frame_split, text='', bg='green')

player_label_1 = Label(player_frame, text='', bg='green')
player_label_1.grid(row=0, column=0, pady=20, padx=20)

player_label_2 = Label(player_frame, text='', bg='green')
player_label_2.grid(row=0, column=1, pady=20, padx=20)

player_label_3 = Label(player_frame, text='', bg='green')
player_label_3.grid(row=0, column=2, pady=20, padx=20)

player_label_4 = Label(player_frame, text='', bg='green')
player_label_4.grid(row=0, column=3, pady=20, padx=20)

player_label_5 = Label(player_frame, text='', bg='green')
player_label_5.grid(row=0, column=4, pady=20, padx=20) 



mainloop()