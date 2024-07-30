from .flashcard import FlashCard

class FlashCardSet:
    def __init__(self, title):
        self.title = title
        self.cards = []

    def add_card(self, front, back):
        self.cards.append(FlashCard(front, back))

    def edit_card(self, index, new_front, new_back):
        self.cards[index].front = new_front
        self.cards[index].back = new_back

    def delete_card(self, index):
        self.cards.pop(index)

    def to_dict(self):
        return {
            "title": self.title,
            "cards": [{"front": card.front, "back": card.back, "review_count": card.review_count, "correct_count": card.correct_count} for card in self.cards],
        }

    @classmethod
    def from_dict(cls, data):
        set_instance = cls(data["title"])
        for card_data in data["cards"]:
            card = FlashCard(card_data["front"], card_data["back"])
            card.review_count = card_data.get("review_count", 0)
            card.correct_count = card_data.get("correct_count", 0)
            set_instance.cards.append(card)
        return set_instance

    def total_score(self):
        return sum(card.correct_count for card in self.cards)

    def success_rate(self):
        total_reviews = sum(card.review_count for card in self.cards)
        total_correct = sum(card.correct_count for card in self.cards)
        if total_reviews == 0:
            return 0
        return (total_correct / total_reviews) * 100