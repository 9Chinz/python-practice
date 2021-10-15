
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
computer_hand = []


def deal_card(player_hand):
    """ deal 2 card for player if player not have any card in hand"""
    amount_of_cards_to_deal = 2 if not player_hand else 1
    for _ in range(amount_of_cards_to_deal):
        random_card = random.choice(cards)
        player_hand.append(random_card)


def calculate_score(card_list):
    """ calculate score by card in list"""
    score_of_list = 0
    for card in card_list:
        score_of_list += card
    return score_of_list


def does_player_have_blackjack(player_hand):
    """ check player has blackjack"""
    return True if 11 in player_hand and 10 in player_hand and len(
        player_hand) == 2 else False


def is_score_over_twenty_one(player_hand, player_score):
    """ check if card over 21 then check if have ace in deck change to 1 then if over 21 or not found ace then return True"""
    if player_score > 21:
        found_ace_card = False
        for idx, card in enumerate(player_hand):
            if card == 11:
                player_hand[idx] = 1
                found_ace_card = True
                break
        player_score = calculate_score(player_hand)
        if not found_ace_card or player_score > 21:
            return True
    return False


def compare(user_score, computer_score):
    """compare score to other"""
    if user_score > computer_score:
        print("You win 😃")
    elif user_score < computer_score:
        print("You lose 😤")
    elif user_score == computer_score:
        print("Draw 🙃")


def reveal_all_card():
    """reavel all card"""
    print(
        f"Your final hand: {user_hand}, final score: {calculate_score(user_hand)}")
    print(
        f"Computer's final hand: {computer_hand}, final score: {calculate_score(computer_hand)}")


is_enough_cards = False
is_game_finished = True
is_start = True

while is_start:
    while not is_game_finished:
        computer_score = calculate_score(computer_hand)
        while not is_enough_cards:
            user_score = calculate_score(user_hand)
            if does_player_have_blackjack(computer_hand):
                reveal_all_card()
                print("Lose, opponent has Blackjack 😱")
                is_game_finished = True
                break
            elif does_player_have_blackjack(user_hand):
                reveal_all_card()
                print("Win with a Blackjack 😎")
                is_game_finished = True
                break
            if is_score_over_twenty_one(user_hand, user_score):
                reveal_all_card()
                print("You went over. You lose 😭")
                is_game_finished = True
                break
            if user_score == 21:
                reveal_all_card()
                print("Win 😎")
                is_game_finished = True
                break
            print(f"Your cards: {user_hand}, {calculate_score(user_hand)}")
            print(f"Computer's first card: {computer_hand[0]}")
            while True:
                get_another_card = input(
                    "Type 'y' to get another card, type 'n' to pass: ")
                if get_another_card.lower() in ("y", "n"):
                    break
                else:
                    print("please enter 'Y'|'N' !")
            if get_another_card.lower() == 'y':
                deal_card(user_hand)
            elif get_another_card.lower() == 'n':
                is_enough_cards = True
                break
        if is_game_finished:
            break
        while computer_score < 17:
            deal_card(computer_hand)
            computer_score = calculate_score(computer_hand)

        if is_score_over_twenty_one(computer_hand, computer_score):
            reveal_all_card()
            print("Opponent went over. You win 😁")
            is_game_finished = True
        else:
            user_score = calculate_score(user_hand)
            computer_score = calculate_score(computer_hand)
            reveal_all_card()
            compare(user_score, computer_score)
            is_game_finished = True
    want_to_play = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_to_play.lower() == 'y':
        is_start = True
        is_game_finished = False
        is_enough_cards = False
        user_hand.clear()
        computer_hand.clear()
        deal_card(user_hand)
        deal_card(computer_hand)
    else:
        is_start = False
