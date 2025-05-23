import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10}
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        for _ in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)
        self.calculate_value()

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            card_value = int(card.rank['value'])    
            self.value += card_value  
            if card.rank['rank'] == "A":  
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        return self.get_value() == 21

    def __str__(self):
        hand_representation = f"{'Dealers' if self.dealer else 'Players'} hand:\n"
        hand_representation += "\n".join(str(card) for card in self.cards)
        if not self.dealer:
            hand_representation += f"\nValue: {self.get_value()}"
        return hand_representation
    
    def display_self(self,show_all_dealer_cards=False):
        for index, card in enumerate(self.cards):
            if index and self.dealer == 0 and not show_all_dealer_cards and not self.is_blackjack():
                print("Hidden Card")
            else:
                print(card)

class game:
    def play(self):
        game_number = 0
        
        while True:
            try:
                games_to_play = int(input("How many games would you like to play? ")) 
                if games_to_play > 0:
                    break
                else:
                    print("Please enter a number greater than 0.")
            except ValueError:
                print("You must enter a valid number!")

        while game_number < games_to_play:
            game_number += 1
            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for _ in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print("\n" + "*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display_self()
            dealer_hand.display_self()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Do you want to hit or stand? ").lower().strip()
                print()

                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input('Please enter "hit" or "stand": ').lower().strip()
                    print()

                if choice in ["h", "hit"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display_self()

            if self.check_winner(player_hand, dealer_hand):
                continue

            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(deck.deal(1))

            dealer_hand.display_self(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("\nResults")
            print("Your hand:")
            print(player_hand)
            print("Dealer's hand:")
            print(dealer_hand)

            self.check_winner(player_hand, dealer_hand, game_over=True)

        print("\nThanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("Player busts! Dealer wins. 😪")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busts! Player wins. 😃")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has blackjack! Dealer wins. 😪")
                return True
            elif player_hand.is_blackjack():
                print("Player has blackjack! Player wins. 😃")
                return True
            return False

        player_val = player_hand.get_value()
        dealer_val = dealer_hand.get_value()

        if player_val > dealer_val:
            print("Player wins! 😃")
        elif player_val < dealer_val:
            print("Dealer wins! 😪")
        else:
            print("It's a tie! 😲")
        return True

            


g = game()
g.play()
#_.ibnehassan._