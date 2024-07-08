import tkinter as tk
from tkinter import messagebox, simpledialog
import random


class FlashCard:
    """ Class to represent a flashcard."""
    def __init__(self, front, back):
        self.front = front
        self.back = back


class FlashCardSet:
    """ Class to represent a set of flashcards."""
    def __init__(self, title):
        self.title = title
        self.cards = []

    def add_card(self, front, back):
        """
        Add a flashcard to the card set.
        :param front: Front of the flashcard (question)
        :param back: Back of the flashcard (answer)
        :return: None
        """
        self.cards.append(FlashCard(front, back))

    def edit_card(self, index, new_front, new_back):
        """
        Edit the question and answer of the flashcard.
        :param index:
        :param new_front:
        :param new_back:
        :return: None
        """
        self.cards[index].front = new_front
        self.cards[index].back = new_back

    def delete_card(self, index):
        """
        Delete existing card
        :param index: Index of the card to delete
        :return: None
        """
        self.cards.pop(index)


class FlashcardGUI:
    """ Class to represent the Flashcard App GUI"""
    def __init__(self, root):
        self.main_frame = None
        self.root = root
        self.root.title("Flashcard App")
        self.root.geometry("800x600")
        self.root.configure(bg="lightblue")

        self.flashcard_sets = []
        self.current_set = None
        self.current_card_index = 0

        self.init_ui()

    def init_ui(self):
        """ Initialize the GUI components."""
        self.create_menu()
        self.create_main_frame()
        self.show_welcome_screen()

    def create_menu(self):
        """ Create the menu bar."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Set", command=self.create_new_set)
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Edit Current Set", command=self.edit_current_set)

    def create_main_frame(self):
        """ Create the main frame."""
        self.main_frame = tk.Frame(self.root, bg="lightblue")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

    def show_welcome_screen(self):
        """ Show the welcome screen."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="Welcome to Flashcard App!", font=("Arial", 20), bg="lightblue").pack(pady=20)
        tk.Button(self.main_frame, text="View Existing Sets", command=self.show_existing_sets).pack(pady=10)
        tk.Button(self.main_frame, text="Create New Set", command=self.create_new_set).pack(pady=10)
        tk.Button(self.main_frame, text="Exit", command=self.on_closing).pack(pady=10)

    def show_existing_sets(self):
        """ Show the existing flashcard sets."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        if not self.flashcard_sets:
            tk.Label(self.main_frame, text="No flashcard sets found. Create a new set to start learning.",
                     bg="lightblue").pack(pady=20)
        else:
            tk.Label(self.main_frame, text="Available Flashcard Sets:", font=("Arial", 16), bg="lightblue").pack(
                pady=20)
            for i, flashcard_set in enumerate(self.flashcard_sets):
                tk.Button(self.main_frame, text=f"{i + 1}. {flashcard_set.title}",
                          command=lambda x=i: self.show_set_options(x)).pack(pady=5)

        tk.Button(self.main_frame, text="Back", command=self.show_welcome_screen).pack(pady=20)

    def create_new_set(self):
        """ Create a new flashcard set."""
        title = simpledialog.askstring("New Set", "Enter the title of the new set:")
        if title:
            new_set = FlashCardSet(title)
            self.flashcard_sets.append(new_set)
            self.current_set = new_set
            self.add_cards_to_set()

    def add_cards_to_set(self):
        """ Add cards to the current set."""
        while True:
            front = simpledialog.askstring("New Card", "Enter the question:")
            if not front:
                break
            back = simpledialog.askstring("New Card", "Enter the answer:")
            if not back:
                break
            self.current_set.add_card(front, back)
            if not messagebox.askyesno("Add Another", "Do you want to add another card?"):
                break
        self.show_existing_sets()

    def show_set_options(self, set_index):
        """ Show the options for the selected flashcard set."""
        self.current_set = self.flashcard_sets[set_index]
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text=f"Set: {self.current_set.title}", font=("Arial", 16), bg="lightblue").pack(
            pady=20)
        tk.Button(self.main_frame, text="Start Learning", command=self.start_learning).pack(pady=10)
        tk.Button(self.main_frame, text="Edit Set", command=self.edit_current_set).pack(pady=10)
        tk.Button(self.main_frame, text="Delete Set", command=lambda: self.delete_set(set_index)).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.show_existing_sets).pack(pady=20)

    def start_learning(self):
        """ Start the flashcard learning session"""
        if not self.current_set.cards:
            messagebox.showinfo("Empty Set", "This set has no cards. Add some cards first.")
            return

        self.current_card_index = 0
        random.shuffle(self.current_set.cards)
        self.show_flashcard()

    def show_flashcard(self):
        """ Show the flashcard on the screen."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        card = self.current_set.cards[self.current_card_index]
        tk.Label(self.main_frame, text=card.front, font=("Arial", 20), bg="lightblue").pack(pady=50)
        tk.Button(self.main_frame, text="Show Answer", command=self.show_answer).pack(pady=20)
        tk.Button(self.main_frame, text="Next Card", command=self.next_card).pack(pady=20)
        tk.Button(self.main_frame, text="End Session", command=self.on_closing).pack(pady=20)

    def show_answer(self):
        """ Show the answer of the flashcard."""
        card = self.current_set.cards[self.current_card_index]
        messagebox.showinfo("Answer", card.back)

    def next_card(self):
        """ Show the next flashcard."""
        self.current_card_index += 1
        if self.current_card_index >= len(self.current_set.cards):
            messagebox.showinfo("Completed", "You've gone through all the cards!")
            self.show_set_options(self.flashcard_sets.index(self.current_set))
        else:
            self.show_flashcard()

    def edit_current_set(self):
        """ Edit the current flashcard set."""
        if not self.current_set:
            messagebox.showinfo("No Set Selected", "Please select a set first.")
            return

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text=f"Editing Set: {self.current_set.title}", font=("Arial", 16), bg="lightblue").pack(pady=20)
        tk.Button(self.main_frame, text="Edit Title", command=self.edit_set_title).pack(pady=10)
        tk.Button(self.main_frame, text="Add Card", command=self.add_card_to_current_set).pack(pady=10)
        tk.Button(self.main_frame, text="Edit Cards", command=self.edit_card).pack(pady=10)
        tk.Button(self.main_frame, text="Delete Card", command=self.delete_card).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=lambda: self.show_set_options(self.flashcard_sets.index(self.current_set))).pack(pady=20)

        # Display current cards with indexes
        if self.current_set.cards:
            tk.Label(self.main_frame, text="Current Cards:", font=("Arial", 14), bg="lightblue").pack(pady=10)
            for i, card in enumerate(self.current_set.cards):
                tk.Label(self.main_frame, text=f"{i+1}. Q: {card.front[:30]}... A: {card.back[:30]}...", bg="lightblue").pack(pady=2)

    def edit_set_title(self):
        """ Edit the title of the current flashcard set."""
        new_title = simpledialog.askstring("Edit Title", "Enter the new title:", initialvalue=self.current_set.title)
        if new_title:
            self.current_set.title = new_title
            self.edit_current_set()

    def add_card_to_current_set(self):
        """ Add a card to the current flashcard set."""
        front = simpledialog.askstring("New Card", "Enter the question:")
        if front:
            back = simpledialog.askstring("New Card", "Enter the answer:")
            if back:
                self.current_set.add_card(front, back)
        self.edit_current_set()

    def edit_card(self):
        """ Edit the cards in the current flashcard set."""
        if not self.current_set.cards:
            messagebox.showinfo("Empty Set", "This set has no cards to edit.")
            return

        # Display cards with indexes
        card_list = "\n".join([f"{i + 1}. Q: {card.front[:30]}... A: {card.back[:30]}..." for i, card in
                               enumerate(self.current_set.cards)])
        card_index = simpledialog.askinteger("Edit Card",
                                             f"Current cards:\n{card_list}\n\nEnter the card number to edit:",
                                             minvalue=1, maxvalue=len(self.current_set.cards))

        if card_index:
            card = self.current_set.cards[card_index - 1]
            new_front = simpledialog.askstring("Edit Card", "Enter the new question:", initialvalue=card.front)
            new_back = simpledialog.askstring("Edit Card", "Enter the new answer:", initialvalue=card.back)
            if new_front and new_back:
                self.current_set.edit_card(card_index - 1, new_front, new_back)
        self.edit_current_set()

    def delete_card(self):
        """ Delete a card from the current flashcard set."""
        if not self.current_set.cards:
            messagebox.showinfo("Empty Set", "This set has no cards to delete.")
            return

        # Display cards with indexes
        card_list = "\n".join([f"{i + 1}. Q: {card.front[:30]}... A: {card.back[:30]}..." for i, card in
                               enumerate(self.current_set.cards)])
        card_index = simpledialog.askinteger("Delete Card",
                                             f"Current cards:\n{card_list}\n\nEnter the card number to delete:",
                                             minvalue=1, maxvalue=len(self.current_set.cards))

        if card_index:
            if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete card {card_index}?"):
                self.current_set.delete_card(card_index - 1)
        self.edit_current_set()

    def delete_set(self, set_index):
        """ Delete the selected flashcard set."""
        if messagebox.askyesno("Confirm Deletion",
                               f"Are you sure you want to delete the set '{self.flashcard_sets[set_index].title}'?"):
            del self.flashcard_sets[set_index]
            self.show_existing_sets()

    def on_closing(self):
        """ Handle the window closing event."""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardGUI(root)
    root.mainloop()

