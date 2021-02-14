import random

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
        if self.answer == user_answer:
            self.guessed_status = True
        return self.guessed_status

    def study(self):
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


class CardSet:
    def __init__(self, cards=None):
        self.score = 0
        if cards:
            self.cards = cards
        else:
            self.cards = []

    def shuffle(self):
        for f_index, f_value in enumerate(self.cards):
            s_index = random.randrange(len(self.cards))
            s_value = self.cards[s_index]

            self.cards[s_index] = f_value
            self.cards[f_index] = s_value


    def add_card(self, card):
        self.cards.append(card)

    def display(self):
        print([{
            'prompt': card.prompt,
            'answer': card.answer,
            'status': card.guessed_status,
        } for card in self.cards])

    def display_prompts(self):
        print([
            {
                
            } for card in self.cards])
    
    def study(self):
        for card in self.cards:
            score = card.study()
            if score > 0:
                self.score += 1
            else:
                continue




tagalog = CardSet([
    Card('Good Morning', 'Magandang umaga'),
    Card('Good Noon', 'Magandang tanghali'),
    Card('Good Afternoon', 'Magandang hapon'),
    Card('Goodnight', 'Magandang gabi'),
    Card('Goodbye', 'Paalam'),
    Card('Thank You', 'Salamat'),
    Card('You are welcome', 'Walang anuman'),
    Card('Yes', 'Oo'),
    Card('No', 'Hindi'),
    Card('I', 'Ako'),
    Card('You', 'Ikaw'),
    Card('And', 'At'),
    Card('He/She', 'Siya'),
    Card('They', 'Sila'),
    Card('Sugar', 'Asukal'),
    Card('Fruits', 'Mga prutas'),
    Card('Egg', 'Ilog')
])

tagalog.display()
print('Shuffling...')
tagalog.shuffle()
tagalog.display()