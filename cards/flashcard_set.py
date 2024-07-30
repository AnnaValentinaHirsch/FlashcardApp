from .flashcard import FlashCard

class FlashCardSet:
    def __init__(self, title):
        self.title = title
        self.cards = []

    def add_card(self, front, back):
        """
        Add a card to the set with the given front and back text.
        """
        self.cards.append(FlashCard(front, back))

    def edit_card(self, index, new_front, new_back):
        """
        Edit a card in the set by its index.
        """
        self.cards[index].front = new_front
        self.cards[index].back = new_back

    def delete_card(self, index):
        """
        Delete a card from the set by its index.
        """
        self.cards.pop(index)

    def to_dict(self):
        """
        Convert the FlashCardSet instance to a dictionary. The dictionary will have a "title" key with the title of
        the set, and a "cards" key with a list of dictionaries representing the cards in the set. Each card
        dictionary will have a "front" key with the front of the card, a "back" key with the back of the card,
        and "review_count" and "correct_count" keys with the review and correct counts for the card.
        """
        return {
            "title": self.title,
            "cards": [{"front": card.front, "back": card.back, "review_count": card.review_count, "correct_count": card.correct_count} for card in self.cards],
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a FlashCardSet instance from a dictionary. The dictionary should have a "title" key with the title of
        the set, and a "cards" key with a list of dictionaries representing the cards in the set. Each card
        dictionary should have a "front" key with the front of the card, a "back" key with the back of the card,
        and optional "review_count" and "correct_count" keys with the review and correct counts for the card.
        """
        set_instance = cls(data["title"])
        for card_data in data["cards"]:
            card = FlashCard(card_data["front"], card_data["back"])
            card.review_count = card_data.get("review_count", 0)
            card.correct_count = card_data.get("correct_count", 0)
            set_instance.cards.append(card)
        return set_instance

    def total_score(self):
        """
        Calculate the total score for the set, which is the sum of the correct counts for all cards.
        """
        return sum(card.correct_count for card in self.cards)

    def success_rate(self):
        """
        Calculate the success rate for the set, which is the total correct count divided by the total review count.
        """
        total_reviews = sum(card.review_count for card in self.cards)
        total_correct = sum(card.correct_count for card in self.cards)
        if total_reviews == 0:
            return 0
        return (total_correct / total_reviews) * 100