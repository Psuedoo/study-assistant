from cards import *

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

# c = tagalog.cards[0].convert_to_json()
# print(c)

tagalog.save_json_file('tagalog')