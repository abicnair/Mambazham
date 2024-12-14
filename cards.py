import random


class Cards:
    def __init__(self):
        # Green cards (adjectives/descriptions in Malayalam)
        self.green_cards = [
            # Basic qualities
            {"id": 1, "text": "എളുപ്പമുള്ള", "translation": "Easy", "category": "quality"},
            {"id": 2, "text": "വേഗം", "translation": "Fast", "category": "speed"},
            {"id": 3, "text": "മധുരം", "translation": "Sweet", "category": "taste"},
            {"id": 4, "text": "സുഖം", "translation": "Comfortable", "category": "feeling"},
            {"id": 5, "text": "എരിവ്", "translation": "Spicy", "category": "taste"},
            
            # Emotions/Feelings
            {"id": 6, "text": "സന്തോഷം", "translation": "Happy", "category": "emotion"},
            {"id": 7, "text": "ദുഃഖം", "translation": "Sad", "category": "emotion"},
            {"id": 8, "text": "സ്നേഹം", "translation": "Loving", "category": "emotion"},
            
            # Physical qualities
            {"id": 9, "text": "വലുത്", "translation": "Big", "category": "size"},
            {"id": 10, "text": "ചെറുത്", "translation": "Small", "category": "size"},
            {"id": 11, "text": "ഉയരം", "translation": "Tall", "category": "size"},
            
            # Time-related
            {"id": 12, "text": "പഴയ", "translation": "Old", "category": "time"},
            {"id": 13, "text": "പുതിയ", "translation": "New", "category": "time"},
            
            # Character traits
            {"id": 14, "text": "മടിയൻ", "translation": "Lazy", "category": "character"},
            {"id": 15, "text": "ബുദ്ധിമാൻ", "translation": "Intelligent", "category": "character"}
        ]

        self.red_cards = [
            # Animals
            {"id": 1, "text": "കാക്ക", "translation": "Crow", "category": "animal"},
            {"id": 2, "text": "പൂച്ച", "translation": "Cat", "category": "animal"},
            {"id": 3, "text": "ആമ", "translation": "Turtle", "category": "animal"},
            {"id": 4, "text": "പല്ലി", "translation": "Lizard", "category": "animal"},
            {"id": 5, "text": "പറവ", "translation": "Bird", "category": "animal"},
            
            # Body Parts
            {"id": 6, "text": "നാക്ക്", "translation": "Tongue", "category": "body"},
            {"id": 7, "text": "കണ്ണ്", "translation": "Eye", "category": "body"},
            {"id": 8, "text": "മെയ്യ്", "translation": "Body", "category": "body"},
            {"id": 9, "text": "പല്ല്", "translation": "Tooth", "category": "body"},
            
            # Nature
            {"id": 10, "text": "തെക്കു", "translation": "South", "category": "nature"},
            {"id": 11, "text": "മഞ്ഞള്‍", "translation": "Turmeric", "category": "nature"},
            {"id": 12, "text": "വെള്ളം", "translation": "Water", "category": "nature"},
            {"id": 13, "text": "പാട്ട്", "translation": "Song", "category": "nature"},
            {"id": 14, "text": "മരത്തന്‍", "translation": "Tree", "category": "nature"},
            {"id": 15, "text": "തെങ്ങ്", "translation": "Coconut Tree", "category": "nature"},
            {"id": 16, "text": "പർവതം", "translation": "Mountain", "category": "nature"},
            {"id": 17, "text": "മുറ്റം", "translation": "Courtyard", "category": "nature"},
            {"id": 18, "text": "തുള്ളി", "translation": "Drop", "category": "nature"},
            
            # Food
            {"id": 19, "text": "അപ്ലം", "translation": "Appam", "category": "food"},
            {"id": 20, "text": "മാങ്ങ", "translation": "Mango", "category": "food"},
            {"id": 21, "text": "തേങ്ങ", "translation": "Coconut", "category": "food"},
            {"id": 22, "text": "നെയ്യ്", "translation": "Ghee", "category": "food"},
            {"id": 23, "text": "നെയ്", "translation": "Ghee", "category": "food"},
            {"id": 24, "text": "നെയ്യപ്പം", "translation": "Ghee Cake", "category": "food"},
            {"id": 25, "text": "മല്ലി", "translation": "Coriander", "category": "food"},
            
            # Family
            {"id": 26, "text": "അമ്മാവന്‍", "translation": "Uncle", "category": "family"},
            {"id": 27, "text": "അമ്മ", "translation": "Mother", "category": "family"},
            {"id": 28, "text": "മുത്തശ്ശി", "translation": "Grandmother", "category": "family"},
            {"id": 29, "text": "പെണ്ണ്", "translation": "Girl/Woman", "category": "family"},
            {"id": 30, "text": "മുത്തശ്ശൻ", "translation": "Grandfather", "category": "family"},
            {"id": 31, "text": "പയ്യൻ", "translation": "Young Man/Boy", "category": "family"},
            
            # Objects
            {"id": 32, "text": "ചാക്ക്", "translation": "Sack", "category": "object"},
            {"id": 33, "text": "വീച്ചി", "translation": "Fan", "category": "object"},
            {"id": 34, "text": "കത്തി", "translation": "Knife", "category": "object"},
            {"id": 35, "text": "കണ്ണാടി", "translation": "Mirror", "category": "object"},
            {"id": 36, "text": "കല്ല്", "translation": "Stone", "category": "object"},
            {"id": 37, "text": "വള്ളം", "translation": "Boat", "category": "object"},
            {"id": 38, "text": "ചുറ്റിക", "translation": "Hammer", "category": "object"},
            {"id": 39, "text": "പട്ടം", "translation": "Kite", "category": "object"},
            
            # Places
            {"id": 40, "text": "പള്ളിക്കൂടം", "translation": "School", "category": "place"},
            {"id": 41, "text": "കുള", "translation": "Pond", "category": "place"},
            
            # Abstract
            {"id": 42, "text": "സംസാരം", "translation": "Speech/Talk", "category": "abstract"},
            {"id": 43, "text": "മനസ്", "translation": "Mind", "category": "abstract"},
            {"id": 44, "text": "വയസ്", "translation": "Age", "category": "abstract"},
            {"id": 45, "text": "തമസ്സു", "translation": "Darkness", "category": "abstract"},
            {"id": 46, "text": "ദയസ്സ്", "translation": "Mercy", "category": "abstract"},
            {"id": 47, "text": "തടസ്സം", "translation": "Obstacle", "category": "abstract"},
            
            # Miscellaneous
            {"id": 48, "text": "പുഷ്പം", "translation": "Flower", "category": "misc"},
            {"id": 49, "text": "തെയ്യല്‍", "translation": "Sewing", "category": "misc"},
            {"id": 50, "text": "ചോല", "translation": "Stream", "category": "misc"},
            {"id": 51, "text": "കൂട്ടിശ്ശിക", "translation": "Balance Amount", "category": "misc"},
            {"id": 52, "text": "മല്ലു", "translation": "Wrestling", "category": "misc"},
            {"id": 53, "text": "ചോദ്യമിഴ്", "translation": "Question", "category": "misc"},
            {"id": 54, "text": "പരോ", "translation": "Is It Enough", "category": "misc"},
            {"id": 55, "text": "രവുസ്സ്", "translation": "Blouse", "category": "misc"},
            {"id": 56, "text": "വെള്ളി", "translation": "Silver", "category": "misc"}
        ]

        # Red cards (nouns in Malayalam)
        self.red_cards_2 = [
            # Animals
            {"id": 1, "text": "എരുമ", "translation": "Buffalo", "category": "animal"},
            {"id": 2, "text": "എലി", "translation": "Mouse", "category": "animal"},
            {"id": 3, "text": "കുതിര", "translation": "Horse", "category": "animal"},
            {"id": 4, "text": "സിംഹം", "translation": "Lion", "category": "animal"},
            {"id": 5, "text": "പൂച്ച", "translation": "Cat", "category": "animal"},
            {"id": 6, "text": "പട്ടി", "translation": "Dog", "category": "animal"},
            {"id": 7, "text": "മയിൽ", "translation": "Peacock", "category": "animal"},
            {"id": 8, "text": "കാക്ക", "translation": "Crow", "category": "animal"},
            {"id": 9, "text": "മുയൽ", "translation": "Rabbit", "category": "animal"},
            
            # Nature
            {"id": 10, "text": "മേഘം", "translation": "Cloud", "category": "nature"},
            {"id": 11, "text": "മഴ", "translation": "Rain", "category": "nature"},
            {"id": 12, "text": "സൂര്യൻ", "translation": "Sun", "category": "nature"},
            {"id": 13, "text": "ഭൂമി", "translation": "Earth", "category": "nature"},
            {"id": 14, "text": "നക്ഷത്രം", "translation": "Star", "category": "nature"},
            
            # Plants
            {"id": 15, "text": "വാഴ", "translation": "Banana plant", "category": "plant"},
            {"id": 16, "text": "ചെടി", "translation": "Plant", "category": "plant"},
            {"id": 17, "text": "തേങ്ങ", "translation": "Coconut", "category": "plant"},
            {"id": 18, "text": "പുല്ല്", "translation": "Grass", "category": "plant"},
            
            # Household items
            {"id": 19, "text": "മേശ", "translation": "Table", "category": "furniture"},
            {"id": 20, "text": "കസേര", "translation": "Chair", "category": "furniture"},
            {"id": 21, "text": "ജനാല", "translation": "Window", "category": "house"},
            {"id": 22, "text": "വിളക്ക്", "translation": "Lamp", "category": "house"},
            
            # Transportation
            {"id": 23, "text": "വിമാനം", "translation": "Airplane", "category": "transport"},
            {"id": 24, "text": "കപ്പൽ", "translation": "Ship", "category": "transport"},
            {"id": 25, "text": "വള്ളം", "translation": "Boat", "category": "transport"},
            
            # People
            {"id": 26, "text": "അമ്മ", "translation": "Mother", "category": "family"},
            {"id": 27, "text": "അച്ഛൻ", "translation": "Father", "category": "family"},
            {"id": 28, "text": "മുത്തശ്ശി", "translation": "Grandmother", "category": "family"},
            {"id": 29, "text": "മുത്തശ്ശൻ", "translation": "Grandfather", "category": "family"},
            
            # Food
            {"id": 30, "text": "അപ്പം", "translation": "Bread", "category": "food"},
            {"id": 31, "text": "പപ്പടം", "translation": "Papadam", "category": "food"},
            {"id": 32, "text": "കഞ്ഞി", "translation": "Rice porridge", "category": "food"},
            
            # Body parts
            {"id": 33, "text": "കണ്ണ്", "translation": "Eye", "category": "body"},
            {"id": 34, "text": "മുഖം", "translation": "Face", "category": "body"},
            {"id": 35, "text": "നാക്ക്", "translation": "Tongue", "category": "body"},
            
            # Nature features
            {"id": 36, "text": "പാലം", "translation": "Bridge", "category": "structure"},
            {"id": 37, "text": "നദി", "translation": "River", "category": "nature"},
            {"id": 38, "text": "കിണർ", "translation": "Well", "category": "structure"},
            
            # Abstract concepts
            {"id": 39, "text": "സമയം", "translation": "Time", "category": "abstract"},
            {"id": 40, "text": "സ്നേഹം", "translation": "Love", "category": "abstract"},
            {"id": 41, "text": "സഹായം", "translation": "Help", "category": "abstract"},
            
            # Cultural items
            {"id": 42, "text": "വീണ", "translation": "Veena (instrument)", "category": "culture"},
            {"id": 43, "text": "ചിത്രം", "translation": "Picture", "category": "art"},
            {"id": 44, "text": "പട്ടം", "translation": "Kite", "category": "toy"},
            
            # Tools
            {"id": 45, "text": "ആണി", "translation": "Nail", "category": "tool"},
            {"id": 46, "text": "കത്തി", "translation": "Knife", "category": "tool"},
            {"id": 47, "text": "ഏണി", "translation": "Ladder", "category": "tool"},
            
            # Materials
            {"id": 48, "text": "മണ്ണ്", "translation": "Soil", "category": "material"},
            {"id": 49, "text": "വെള്ളം", "translation": "Water", "category": "material"},
            {"id": 50, "text": "കല്ല്", "translation": "Stone", "category": "material"},

                        {"id": 1, "text": "ചായ", "translation": "Tea"},
            {"id": 2, "text": "സിനിമ", "translation": "Movie"},
            {"id": 3, "text": "പൂച്ച", "translation": "Cat"},
            {"id": 4, "text": "നായ", "translation": "Dog"},
            {"id": 5, "text": "വീട്", "translation": "House"},
            {"id": 6, "text": "കാർ", "translation": "Car"},
            {"id": 7, "text": "പൂവ്", "translation": "Flower"},
            {"id": 8, "text": "മരം", "translation": "Tree"},
            {"id": 9, "text": "കടൽ", "translation": "Sea"},
            {"id": 10, "text": "മല", "translation": "Mountain"},
            {"id": 13, "text": "പുസ്തകം", "translation": "Book"},
            {"id": 15, "text": "കളി", "translation": "Game"},
            {"id": 20, "text": "വിമാനം", "translation": "Airplane"},
            {"id": 21, "text": "കുട", "translation": "Umbrella"},
            {"id": 22, "text": "പാമ്പ്", "translation": "Snake"},
            {"id": 23, "text": "ആന", "translation": "Elephant"},
            {"id": 24, "text": "കോഴി", "translation": "Chicken"},
            {"id": 25, "text": "മീൻ", "translation": "Fish"}

        ]

    def get_cards_by_category(self, category):
        """Get all cards of a specific category"""
        return [card for card in self.red_cards if card["category"] == category]

    def get_green_cards_by_category(self, category):
        """Get all green cards of a specific category"""
        return [card for card in self.green_cards if card["category"] == category]

class Card:
    def __init__(self, text, translation, card_id):
        self.text = text
        self.translation = translation
        self.id = card_id

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'translation': self.translation
        }

class Deck:
    def __init__(self):
        self.cards = []
        self.load_cards()
        random.shuffle(self.cards)

    def load_cards(self):
        # White cards (responses)
        cards_data = [
            # Animals
            {"id": 1, "text": "എരുമ", "translation": "Buffalo", "category": "animal"},
            {"id": 2, "text": "എലി", "translation": "Mouse", "category": "animal"},
            {"id": 3, "text": "കുതിര", "translation": "Horse", "category": "animal"},
            {"id": 4, "text": "സിംഹം", "translation": "Lion", "category": "animal"},
            {"id": 5, "text": "പൂച്ച", "translation": "Cat", "category": "animal"},
            {"id": 6, "text": "പട്ടി", "translation": "Dog", "category": "animal"},
            {"id": 7, "text": "മയിൽ", "translation": "Peacock", "category": "animal"},
            {"id": 8, "text": "കാക്ക", "translation": "Crow", "category": "animal"},
            {"id": 9, "text": "മുയൽ", "translation": "Rabbit", "category": "animal"},
            
            # Nature
            {"id": 10, "text": "മേഘം", "translation": "Cloud", "category": "nature"},
            {"id": 11, "text": "മഴ", "translation": "Rain", "category": "nature"},
            {"id": 12, "text": "സൂര്യൻ", "translation": "Sun", "category": "nature"},
            {"id": 13, "text": "ഭൂമി", "translation": "Earth", "category": "nature"},
            {"id": 14, "text": "നക്ഷത്രം", "translation": "Star", "category": "nature"},
            
            # Plants
            {"id": 15, "text": "വാഴ", "translation": "Banana plant", "category": "plant"},
            {"id": 16, "text": "ചെടി", "translation": "Plant", "category": "plant"},
            {"id": 17, "text": "തേങ്ങ", "translation": "Coconut", "category": "plant"},
            {"id": 18, "text": "പുല്ല്", "translation": "Grass", "category": "plant"},
            
            # Household items
            {"id": 19, "text": "മേശ", "translation": "Table", "category": "furniture"},
            {"id": 20, "text": "കസേര", "translation": "Chair", "category": "furniture"},
            {"id": 21, "text": "ജനാല", "translation": "Window", "category": "house"},
            {"id": 22, "text": "വിളക്ക്", "translation": "Lamp", "category": "house"},
            
            # Transportation
            {"id": 23, "text": "വിമാനം", "translation": "Airplane", "category": "transport"},
            {"id": 24, "text": "കപ്പൽ", "translation": "Ship", "category": "transport"},
            {"id": 25, "text": "വള്ളം", "translation": "Boat", "category": "transport"},
            
            # People
            {"id": 26, "text": "അമ്മ", "translation": "Mother", "category": "family"},
            {"id": 27, "text": "അച്ഛൻ", "translation": "Father", "category": "family"},
            {"id": 28, "text": "മുത്തശ്ശി", "translation": "Grandmother", "category": "family"},
            {"id": 29, "text": "മുത്തശ്ശൻ", "translation": "Grandfather", "category": "family"},
            
            # Food
            {"id": 30, "text": "അപ്പം", "translation": "Bread", "category": "food"},
            {"id": 31, "text": "പപ്പടം", "translation": "Papadam", "category": "food"},
            {"id": 32, "text": "കഞ്ഞി", "translation": "Rice porridge", "category": "food"},
            
            # Body parts
            {"id": 33, "text": "കണ്ണ്", "translation": "Eye", "category": "body"},
            {"id": 34, "text": "മുഖം", "translation": "Face", "category": "body"},
            {"id": 35, "text": "നാക്ക്", "translation": "Tongue", "category": "body"},
            
            # Nature features
            {"id": 36, "text": "പാലം", "translation": "Bridge", "category": "structure"},
            {"id": 37, "text": "നദി", "translation": "River", "category": "nature"},
            {"id": 38, "text": "കിണർ", "translation": "Well", "category": "structure"},
            
            # Abstract concepts
            {"id": 39, "text": "സമയം", "translation": "Time", "category": "abstract"},
            {"id": 40, "text": "സ്നേഹം", "translation": "Love", "category": "abstract"},
            {"id": 41, "text": "സഹായം", "translation": "Help", "category": "abstract"},
            
            # Cultural items
            {"id": 42, "text": "വീണ", "translation": "Veena (instrument)", "category": "culture"},
            {"id": 43, "text": "ചിത്രം", "translation": "Picture", "category": "art"},
            {"id": 44, "text": "പട്ടം", "translation": "Kite", "category": "toy"},
            
            # Tools
            {"id": 45, "text": "ആണി", "translation": "Nail", "category": "tool"},
            {"id": 46, "text": "കത്തി", "translation": "Knife", "category": "tool"},
            {"id": 47, "text": "ഏണി", "translation": "Ladder", "category": "tool"},
            
            # Materials
            {"id": 48, "text": "മണ്ണ്", "translation": "Soil", "category": "material"},
            {"id": 49, "text": "വെള്ളം", "translation": "Water", "category": "material"},
            {"id": 50, "text": "കല്ല്", "translation": "Stone", "category": "material"},

                        {"id": 1, "text": "ചായ", "translation": "Tea"},
            {"id": 2, "text": "സിനിമ", "translation": "Movie"},
            {"id": 3, "text": "പൂച്ച", "translation": "Cat"},
            {"id": 4, "text": "നായ", "translation": "Dog"},
            {"id": 5, "text": "വീട്", "translation": "House"},
            {"id": 6, "text": "കാർ", "translation": "Car"},
            {"id": 7, "text": "പൂവ്", "translation": "Flower"},
            {"id": 8, "text": "മരം", "translation": "Tree"},
            {"id": 9, "text": "കടൽ", "translation": "Sea"},
            {"id": 10, "text": "മല", "translation": "Mountain"},
            {"id": 13, "text": "പുസ്തകം", "translation": "Book"},
            {"id": 15, "text": "കളി", "translation": "Game"},
            {"id": 20, "text": "വിമാനം", "translation": "Airplane"},
            {"id": 21, "text": "കുട", "translation": "Umbrella"},
            {"id": 22, "text": "പാമ്പ്", "translation": "Snake"},
            {"id": 23, "text": "ആന", "translation": "Elephant"},
            {"id": 24, "text": "കോഴി", "translation": "Chicken"},
            {"id": 25, "text": "മീൻ", "translation": "Fish"}
        ]
        
        self.cards = [Card(card['text'], card['translation'], card['id']) 
                     for card in cards_data]

    def draw(self):
        if not self.cards:
            self.load_cards()
            random.shuffle(self.cards)
        return self.cards.pop()

class GreenDeck(Deck):
    def load_cards(self):
        # Green cards (situations/prompts)
        cards_data = [
            {"id": 1, "text": "എളുപ്പമുള്ള", "translation": "Easy", "category": "quality"},
            {"id": 2, "text": "വേഗം", "translation": "Fast", "category": "speed"},
            {"id": 3, "text": "മധുരം", "translation": "Sweet", "category": "taste"},
            {"id": 4, "text": "സുഖം", "translation": "Comfortable", "category": "feeling"},
            {"id": 5, "text": "എരിവ്", "translation": "Spicy", "category": "taste"},
            
            # Emotions/Feelings
            {"id": 6, "text": "സന്തോഷം", "translation": "Happy", "category": "emotion"},
            {"id": 7, "text": "ദുഃഖം", "translation": "Sad", "category": "emotion"},
            {"id": 8, "text": "സ്നേഹം", "translation": "Loving", "category": "emotion"},
            
            # Physical qualities
            {"id": 9, "text": "വലുത്", "translation": "Big", "category": "size"},
            {"id": 10, "text": "ചെറുത്", "translation": "Small", "category": "size"},
            {"id": 11, "text": "ഉയരം", "translation": "Tall", "category": "size"},
            
            # Time-related
            {"id": 12, "text": "പഴയ", "translation": "Old", "category": "time"},
            {"id": 13, "text": "പുതിയ", "translation": "New", "category": "time"},
            
            # Character traits
            {"id": 14, "text": "മടിയൻ", "translation": "Lazy", "category": "character"},
            {"id": 15, "text": "ബുദ്ധിമാൻ", "translation": "Intelligent", "category": "character"}
        ]
        
        self.cards = [Card(card['text'], card['translation'], card['id']) 
                     for card in cards_data]
