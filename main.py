############### Blackjack Project #####################
from art import logo
import random

## Import os isnt working for clear TODO: fix
import os
############### Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


## TODO clean up the function of the code now that it's working
## Separate some functionality into different functions? 

def play_game():
    os.system('clear')
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    ## cards_face is to be used to print the card name instead of the number.
    cards_face = [
        "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen",
        "King"
    ]

    player_indices = [random.randint(0, 12), random.randint(0, 12)]
    player_hand = [cards[player_indices[0]], cards[player_indices[1]]]
    player_hand_faces = [
        cards_face[player_indices[0]], cards_face[player_indices[1]]
    ]
    player_sum = sum(player_hand)

    computer_indices = [random.randint(0, 12), random.randint(0, 12)]
    computer_hand = [cards[computer_indices[0]], cards[computer_indices[1]]]
    computer_hand_faces = [
        cards_face[computer_indices[0]], cards_face[computer_indices[1]]
    ]

    print(
        f"Your hand is {player_hand_faces[0]} and {player_hand_faces[1]} for a total of {player_sum}"
    )
    print(f"The face-up card for the dealer is {computer_hand_faces[0]}")

    if player_sum == 21:
        play_again = input(
            "Blackjack! You win! Press any key to play again. Press 'q' to quit "
        )
        if play_again != 'q':
            play_game()
        else:
            print("Thanks for playing!")

    def check_winner(playerSum, computerSum):
        if computerSum > playerSum:
            play_again = input(
                "Dealer wins! Press any key to play again. Press 'q' to quit ")
            if play_again != 'q':
                play_game()
            else:
                print("Thanks for playing!")

        elif playerSum > computerSum:
            play_again = input(
                "You win! Press any key to play again. Press 'q' to quit ")
            if play_again != 'q':
                play_game()
            else:
                print("Thanks for playing!")

        elif playerSum == computerSum:
            play_again = input(
                "It's a draw! Press any key to play again. Press 'q' to quit ")

    def computer_turn(hand):
        print(f"Dealer's hand is {computer_hand_faces}")
        computer_sum = sum(computer_hand)

        while computer_sum < 17:
            print("Dealer's total is under 17, dealer takes another card")
            computer_indices.append(random.randint(0, 12))
            computer_hand.append(cards[computer_indices[-1]])
            computer_hand_faces.append(cards_face[computer_indices[-1]])
            computer_sum = sum(computer_hand)
            print(f"Dealer hand is {computer_hand_faces}")

        if computer_sum > 21:
            if 11 in computer_hand:
                computer_hand[computer_hand.index(11)] = 1
                computer_sum = sum(computer_hand)
            else:
                play_again = input(
                    f"The dealer's hand is {computer_hand_faces} for a total of {computer_sum}. The Dealer busts. You win! Press any key to play again. Press 'q' to quit "
                )
                if play_again != 'q':
                    play_game()

        elif computer_sum == 21:
            if len(computer_hand) == 2:
                play_again = input(
                    "Dealer Blackjack. Press any key to play again. Press 'q' to quit "
                )
            else:

                play_again = input(
                    "Dealer Wins. Press any key to play again. Press 'q' to quit "
                )
            if play_again != 'q':
                play_game()

        else:
            print(
                f"The computer's hand is {computer_hand_faces} for a total of {computer_sum}."
            )
        return computer_sum

    def player_turn(hand):
        player_choice = input(
            "Would you like to hit or pass? Type 'h' or 'p' ")

        if player_choice == 'h':
            player_indices.append(random.randint(0, 12))
            player_hand.append(cards[player_indices[-1]])
            player_hand_faces.append(cards_face[player_indices[-1]])
            player_sum = sum(player_hand)
            print(
                f"Your hand is {player_hand_faces[0]}, {player_hand_faces[1]}, {player_hand_faces[2]} for a total of {player_sum}"
            )

            if player_sum > 21:
                if 11 in player_hand:
                    player_hand[player_hand.index(11)] = 1
                    player_sum = sum(player_hand)
                else:
                    print(f"Bust! Computer hand: {computer_hand_faces}")
                    play_again = input(
                        "Press any key to play again. Press 'q' to quit ")
                    if play_again != 'q':
                        play_game()

            elif player_sum == 21:
                play_again = input(
                    "Blackjack! You win! Press any key to play again. Press 'q' to quit "
                )
                if play_again != 'q':
                    play_game()

            elif player_sum < 21:
                return player_turn(player_hand)

        elif player_choice == 'p':
            player_sum = sum(player_hand)
            check_winner(player_sum, computer_turn(computer_hand))

    player_sum = player_turn(player_hand)


play_game()
