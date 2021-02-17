import os
import random
import pathlib
import json


# TODO:
#   - Fix displaying cards in a list
#   - Add shuffling feature
#   - Maybe allow hints?
#   - Clean up user input section for guessing

# FEATURE IDEAS:
#   - Planning to add a gui of some sort
#   - Algorithm for smart learning to see less of what you definitely know and
#       more of what you are struggling with. Maybe mix the things you're 
#       struggling with to cause "reinforced learning"
#   - Some sort of DB for saving card sets and maybe learning statistics
#   - Would be awesome to compare learning sessions to see the improvement.
#   - Easy plug and play card sets

class Card:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        self.guessed_status = False

    def check_answer(self, user_answer):
        """
        Checks the user's answer to the card's 'answer'
        :param user_answer:
        """
        if self.answer == user_answer:
            self.guessed_status = True
        return self.guessed_status

    def study(self):
        """
        Lets you study the card
        """
        attempts = 4
        guesses = 0
        while guesses < attempts:
            user_input = input(f'{self.prompt}\n> ')
            if self.check_answer(user_input):
                print('You have guessed correctly!')
                break
            else:
                print('You are wrong. Try again.')
                guesses += 1
        return 100 - (guesses * 25)

    def convert_to_json(self, indent_level=None, sep=(', ', ': ')):
        return json.dumps(self.__dict__, indent=indent_level, separators=sep)


class CardSet:
    def __init__(self, name, cards=None):
        self.name = name
        self.score = 0
        if cards:
            self.cards = cards
        else:
            self.cards = []

    def shuffle(self):
        """
        Shuffles the cards for randomized studying
        """
        for f_index, f_value in enumerate(self.cards):
            s_index = random.randrange(len(self.cards))
            s_value = self.cards[s_index]

            self.cards[s_index] = f_value
            self.cards[f_index] = s_value

    def add_card(self, card):
        """
        Adds a card to the set
        :param card:
        """
        self.cards.append(card)

    def save_json_file(self):
        """
        Saves the current set as a json file
        """
        json_file = open(f'{self.name}.json', 'w')
        cards = [{
            card.prompt: {
                'answer': card.answer,
                'guessed_status': card.guessed_status,
            }
        } for card in self.cards]
        json.dump(cards, json_file, indent=4)
        json_file.close()

    def load_json_file(self):
        """
        Loads a json file of a set
        """
        if self.file_exists():
            with open(f'{self.name}.json', 'r') as file:
                json_data = json.load(file)

            imported_cards = []
            for card in json_data:
                prompt = [x for x in card][0]
                answer = [x['answer'] for x in card.values()][0]
                imported_cards.append(Card(prompt, answer))
            self.cards = imported_cards
        else:
            self.save_json_file()

    def file_exists(self):
        """
        Checks if the json file exists
        """
        return pathlib.Path(f'{self.name}.json').exists()

    def display(self, side=None):
        """
        Displays the set
        :param side:
        """
        if not side:
            print(
                [
                    {
                        'prompt': card.prompt,
                        'answer': card.answer,
                        'status': card.guessed_status
                    }
                    for card in self.cards
                ]
            )

        if side == 'prompt':
            print(
                [
                    {
                        card.prompt
                    }
                    for card in self.cards
                ]
            )

        if side == 'answer':
            print(
                [
                    {
                        card.answer
                    }
                    for card in self.cards
                ]
            )

    def study(self):
        """
        Starts a study session
        """
        if self.cards:
            for card in self.cards:
                score = card.study()
                if score > 0:
                    self.score += 1
                else:
                    continue
        else:
            self.load_json_file()
