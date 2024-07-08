import random


class FlashCard:
    """ Class to represent a flashcard. """

    def __init__(self, front, back):
        """ Constructs all the necessary attributes for the flashcard object. """
        self.front = front
        self.back = back


class FlashCardSet:
    """ Class to represent a set of flashcards. """

    def __init__(self, title):
        """ Constructs all the necessary attributes for the flashcard set object. """
        self.title = title
        self.cards = []

    def add_card(self, front, back):
        """ Add a flashcard to the card set. """
        self.cards.append(FlashCard(front, back))

    def edit_card(self, index, new_front, new_back):
        """ Edit the question and answer of the flashcard. """
        self.cards[index].front = new_front
        self.cards[index].back = new_back

    def delete_card(self, index):
        """ Delete existing card """
        self.cards.pop(index)


class FlashCardApp:
    def __init__(self):
        self.flashcard_sets = []
        self.current_set = None

    def run(self):
        while True:
            self.show_welcome_message()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.show_existing_sets()
            elif choice == "2":
                self.create_new_set()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def show_welcome_message(self):
        print("Welcome to Flashcard App!")
        print("1. View Existing Flashcard Sets")
        print("2. Create New Set")
        print("3. Exit")

    def show_existing_sets(self):
        if not self.flashcard_sets:
            print("No flashcard sets found. Create a new set to start learning.")
            return
        print("Available Flashcard Sets:")
        for i, flashcard_set in enumerate(self.flashcard_sets):
            print(f"{i + 1}. {flashcard_set.title}")
        choice = int(input("Enter the set number to see options: ")) - 1
        if 0 <= choice < len(self.flashcard_sets):
            self.show_set_options(self.flashcard_sets[choice])
        else:
            print("Invalid choice. Please try again.")

    def create_new_set(self):
        title = input("Enter the title of the new set: ")
        new_set = FlashCardSet(title)
        while True:
            front = input("Enter the question: ")
            back = input("Enter the answer: ")
            new_set.add_card(front, back)
            choice = input("Do you want to add another card? (y/n): ")
            if choice.lower() != "y":
                break

        self.flashcard_sets.append(new_set)
        print(f"Flashcard set {title} created successfully!")

    def show_set_options(self, flashcard_set):
        while True:
            print(f"Set: {flashcard_set.title}")
            print("1. Start Learning")
            print("2. Edit Set")
            print("3. Delete Set")
            print("4. Back")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.start_learning(flashcard_set)
            elif choice == "2":
                self.edit_set(flashcard_set)
            elif choice == "3":
                self.delete_set(flashcard_set)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def edit_set(self, flashcard_set):
        while True:
            print("\nEdit Options:")
            print("1. Edit Set Title")
            print("2. Add Flashcard")
            print("3. Edit existing Flashcard")
            print("4. Delete Flashcard")
            print("5. Back")
            choice = input("Enter your choice: ")
            if choice == "1":
                new_title = input("Enter the new title: ")
                flashcard_set.title = new_title
                print("Set title updated successfully!")
            elif choice == "2":
                self.add_flashcard(flashcard_set)
            elif choice == "3":
                self.edit_flashcard(flashcard_set)
            elif choice == "4":
                self.delete_flashcard(flashcard_set)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def delete_set(self, flashcard_set):
        confirm = input(f"Are you sure you want to delete the set {flashcard_set.title}? (y/n): ")
        if confirm.lower() == "y":
            self.flashcard_sets.remove(flashcard_set)
            print(f"Set {flashcard_set.title} deleted successfully!")
        else:
            print("Deletion cancelled.")

    def add_flashcard(self, flashcard_set):
        front = input("Enter the question: ")
        back = input("Enter the answer: ")
        flashcard_set.add_card(front, back)
        print(f"Flashcard {front} added successfully!")

    def edit_flashcard(self, flashcard_set):
        for i, card in enumerate(flashcard_set.cards):
            print(f"{i + 1}.Front:  {card.front}\n  Back: {card.back}")
        index = int(input("Enter the card number to edit: ")) - 1
        if 0 <= index < len(flashcard_set.cards):
            card = flashcard_set.cards[index]
            while True:
                print(f"Edit Options for Flashcard {index + 1}:")
                print("1. Edit Question")
                print("2. Edit Answer")
                print("3. Back")
                choice = input("Enter your choice: ")
                if choice == "1":
                    card.front = input("Enter the new question: ")
                    print("Question updated successfully!")
                elif choice == "2":
                    card.back = input("Enter the new answer: ")
                    print("Answer updated successfully!")
                elif choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")

    def delete_flashcard(self, flashcard_set):
        for i, card in enumerate(flashcard_set.cards):
            print(f"{i + 1}. Front: {card.front}\n  Back: {card.back}")
        index = int(input("Enter the card number to delete: ")) - 1
        if 0 <= index < len(flashcard_set.cards):
            # Ask for confirmation
            confirm = input(f"Are you sure you want to delete flashcard {index + 1}? (y/n): ")
            if confirm.lower() != "y":
                print("Deletion cancelled.")
                return
            flashcard_set.delete_card(index)
            print(f"Flashcard {index + 1} deleted successfully!")

        else:
            print("Invalid card number. Please try again.")

    def start_learning(self, flashcard_set):
        random.shuffle(flashcard_set.cards)
        for card in flashcard_set.cards:
            input(f"Question: {card.front}\nPress Enter to reveal the answer.")
            print(f"Answer: {card.back}")
            input("Press Enter for the next question...")
        print("All flashcards completed!")


    def exit_app(self):
        print("Exiting Flashcard App...")
        exit()



if __name__ == "__main__":
    app = FlashCardApp()
    app.run()
