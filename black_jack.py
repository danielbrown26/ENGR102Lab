import random

# Deck Setup
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# DECK class
class Deck:
    def __init__(self):
        self.cards = []
        for rank in ranks:
            for suit in suits:
                self.cards.append((rank, suit))

        random.shuffle(self.cards) # Shuffles the deck

    def deal_card(self): # Deals a card from the deck
       if self.cards:
            return self.cards.pop() 
       else:
            return None

# Player class
class Player:
     def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

     def score_hand(self):
        self.score = 0
        aces = 0
        for card in self.hand:
            rank, suit = card
            self.score += values[rank]
            if rank == 'Ace':
                aces += 1
        while self.score > 21 and aces > 0:
            self.score -= 10
            aces -= 1

     def hand_show(self):
        hand_string = ', '.join([f"{rank} of {suit}" for rank, suit in self.hand])
        print(f"{self.name}'s hand: {hand_string} | Score: {self.score}")

# The actual game of Black Jack
def main():
    print("Welcome to Black Jack!")
    deck = Deck()

    # Get the name and number of players
    num_players = (input("Enter the number of players (1-4): "))
    while num_players not in ['1', '2', '3', '4']:
        print("Please enter a valid number of players (1-4).")
        num_players = (input("Enter the number of players (1-4): "))
    num_players = int(num_players)
    players = []
    for i in range(num_players):
        player_name = input(f"What is the name of player #{i + 1}? ")
        players.append(Player(player_name))
    dealer = Player("Dealer")

    # Initial deal
    for player in players + [dealer]:
        player.hand.append(deck.deal_card())
        player.hand.append(deck.deal_card())
        player.score_hand()

    # Player Turns
    for player in players:
        while True:
            if player.score > 21:
                break
            player.hand_show()
            action = input(f"{player.name}, do you want to hit or stand? (h/s): ").lower()
            if action == 'h':
                new_card = deck.deal_card()
                player.hand.append(new_card)
                player.score_hand()
                print(f"{player.name} hits and receives {new_card[0]} of {new_card[1]}.")
                if player.score > 21:
                    print(f"{player.name} busts with a score of {player.score}!")
            elif action == 's':
                print(f"{player.name} stands with a score of {player.score}.")
                break
            else:
                print("Invalid input. Please enter 'h' to hit or 's' to stand.")

    # Dealer's Turn
    print("\nDealer's turn:")
    dealer.hand_show()
    while dealer.score < 17:
        print("Dealer hits.")
        dealer.hand.append(deck.deal_card())
        dealer.score_hand()
        dealer.hand_show()
    if dealer.score > 21:
        print("Dealer busts!")

    # Determine Winners
    print("\nFinal Results:")
    for player in players:
        if player.score > 21:
            print(f"{player.name} busts and loses.")
        elif dealer.score > 21 or player.score > dealer.score:
            print(f"{player.name} wins!")
        elif player.score < dealer.score:
            print(f"{player.name} loses.")
        else:
            print(f"{player.name} ties with the dealer.")

# Runs the game
main()
