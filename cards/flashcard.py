class FlashCard:
    def __init__(self, front, back):
        self.front = front
        self.back = back
        self.review_count = 0
        self.correct_count = 0

    def mark_correct(self):
        self.review_count += 1
        self.correct_count += 1

    def mark_incorrect(self):
        self.review_count += 1

    def success_rate(self):
        if self.review_count == 0:
            return 0
        return (self.correct_count / self.review_count) * 100