import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import customtkinter as ctk
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
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")
        self.root.geometry("400x600")
        self.root.minsize(400, 600)

        # Set the theme
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.flashcard_sets = []
        self.current_set = None
        self.current_card_index = 0

        self.init_ui()

    def init_ui(self):
        self.create_main_frame()
        self.show_deck_manager()

    def create_main_frame(self):
        self.main_frame = ctk.CTkFrame(self.root, fg_color="#F0F0F0")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

    def show_deck_manager(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Header
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="#3498db", corner_radius=0)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(header_frame, text="Your Decks", font=("Roboto", 24, "bold"), text_color="white").pack(pady=20)

        # Scrollable frame for decks
        scroll_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color="#F0F0F0")
        scroll_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        # Add deck cards
        for i, deck in enumerate(self.flashcard_sets):
            self.create_deck_card(scroll_frame, deck, i)

        # Add new deck button
        new_deck_button = ctk.CTkButton(self.main_frame, text="+ Create New Deck",
                                        command=self.create_new_set,
                                        fg_color="#2ecc71", hover_color="#27ae60",
                                        height=50, corner_radius=10)
        new_deck_button.pack(padx=20, pady=(0, 20), fill=tk.X)

        # Add Exit button
        exit_button = ctk.CTkButton(self.main_frame, text="Exit", command=self.on_closing,
                                    fg_color="#e74c3c", hover_color="#c0392b",
                                    height=50, corner_radius=10)
        exit_button.pack(padx=20, pady=(0, 20), fill=tk.X)

        # Add Help button
        help_button = ctk.CTkButton(self.main_frame, text="Help", command=self.show_help_screen,
                                    fg_color="#3498db", hover_color="#2980b9",
                                    height=50, corner_radius=10)
        help_button.pack(padx=20, pady=(0, 20), fill=tk.X)


    def create_deck_card(self, parent, deck, index):
        card_frame = ctk.CTkFrame(parent, fg_color="white", corner_radius=10)
        card_frame.pack(fill=tk.X, pady=5)

        ctk.CTkLabel(card_frame, text=deck.title, font=("Roboto", 18, "bold")).pack(anchor="w", padx=15, pady=(10, 5))
        ctk.CTkLabel(card_frame, text=f"{len(deck.cards)} cards", font=("Roboto", 14)).pack(anchor="w", padx=15,
                                                                                            pady=(0, 10))

        button_frame = ctk.CTkFrame(card_frame, fg_color="transparent")
        button_frame.pack(fill=tk.X, padx=15, pady=(0, 10))

        ctk.CTkButton(button_frame, text="Study", command=lambda: self.start_learning(index),
                      fg_color="#3498db", hover_color="#2980b9", width=80).pack(side=tk.LEFT, padx=(0, 10))
        ctk.CTkButton(button_frame, text="Edit", command=lambda: self.edit_set(index),
                      fg_color="#f39c12", hover_color="#d35400", width=80).pack(side=tk.LEFT)


    def create_new_set(self):
        title = simpledialog.askstring("New Deck", "Enter the title of the new deck:")
        if title:
            new_set = FlashCardSet(title)
            self.flashcard_sets.append(new_set)
            self.current_set = new_set
            self.add_cards_to_set()

    def add_cards_to_set(self):
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
        self.show_deck_manager()

    def start_learning(self, set_index):
        self.current_set = self.flashcard_sets[set_index]
        if not self.current_set.cards:
            messagebox.showinfo("Empty Deck", "This deck has no cards. Add some cards first.")
            return

        self.current_card_index = 0
        random.shuffle(self.current_set.cards)
        self.show_flashcard()

    def show_flashcard(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        card = self.current_set.cards[self.current_card_index]

        # Header
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="#3498db", corner_radius=0)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(header_frame, text=self.current_set.title, font=("Roboto", 24, "bold"), text_color="white").pack(
            pady=20)

        # Card frame
        card_frame = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=10)
        card_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        question_label = ctk.CTkLabel(card_frame, text=card.front, font=("Roboto", 18), wraplength=300)
        question_label.pack(pady=(40, 20), padx=20)

        show_answer_btn = ctk.CTkButton(card_frame, text="Show Answer", command=lambda: self.show_answer(answer_label),
                                        fg_color="#3498db", hover_color="#2980b9")
        show_answer_btn.pack(pady=10)

        answer_label = ctk.CTkLabel(card_frame, text="", font=("Roboto", 16), wraplength=300)
        answer_label.pack(pady=20, padx=20)

        # Navigation buttons
        nav_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        nav_frame.pack(fill=tk.X, padx=20, pady=20)

        ctk.CTkButton(nav_frame, text="Previous", command=self.prev_card,
                      fg_color="#95a5a6", hover_color="#7f8c8d", width=100).pack(side=tk.LEFT)
        ctk.CTkButton(nav_frame, text="Next", command=self.next_card,
                      fg_color="#2ecc71", hover_color="#27ae60", width=100).pack(side=tk.RIGHT)
        ctk.CTkButton(self.main_frame, text="End Session", command=self.show_deck_manager,
                      fg_color="#e74c3c", hover_color="#c0392b").pack(pady=10)

    def show_answer(self, answer_label):
        card = self.current_set.cards[self.current_card_index]
        answer_label.configure(text=card.back)

    def prev_card(self):
        self.current_card_index = (self.current_card_index - 1) % len(self.current_set.cards)
        self.show_flashcard()

    def next_card(self):
        self.current_card_index = (self.current_card_index + 1) % len(self.current_set.cards)
        self.show_flashcard()

    def edit_set(self, set_index):
        self.current_set = self.flashcard_sets[set_index]
        self.show_edit_screen()

    def show_edit_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Header
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="#3498db", corner_radius=0)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(header_frame, text=f"Editing: {self.current_set.title}", font=("Roboto", 24, "bold"),
                     text_color="white").pack(pady=20)

        # Scrollable frame for cards
        scroll_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color="#F0F0F0")
        scroll_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        for i, card in enumerate(self.current_set.cards):
            card_frame = ctk.CTkFrame(scroll_frame, fg_color="white", corner_radius=10)
            card_frame.pack(fill=tk.X, pady=5)

            ctk.CTkLabel(card_frame, text=f"Q: {card.front[:30]}...", font=("Roboto", 14, "bold")).pack(anchor="w",
                                                                                                        padx=15,
                                                                                                        pady=(10, 5))
            ctk.CTkLabel(card_frame, text=f"A: {card.back[:30]}...", font=("Roboto", 12)).pack(anchor="w", padx=15,
                                                                                               pady=(0, 10))

            button_frame = ctk.CTkFrame(card_frame, fg_color="transparent")
            button_frame.pack(fill=tk.X, padx=15, pady=(0, 10))

            ctk.CTkButton(button_frame, text="Edit", command=lambda x=i: self.edit_card(x),
                          fg_color="#f39c12", hover_color="#d35400", width=60).pack(side=tk.LEFT, padx=(0, 10))
            ctk.CTkButton(button_frame, text="Delete", command=lambda x=i: self.delete_card(x),
                          fg_color="#e74c3c", hover_color="#c0392b", width=60).pack(side=tk.LEFT)

        # Add new card button
        new_card_button = ctk.CTkButton(self.main_frame, text="+ Add New Card",
                                        command=self.add_card_to_current_set,
                                        fg_color="#2ecc71", hover_color="#27ae60",
                                        height=50, corner_radius=10)
        new_card_button.pack(padx=20, pady=(0, 10), fill=tk.X)

        # Back button
        back_button = ctk.CTkButton(self.main_frame, text="Back to Decks",
                                    command=self.show_deck_manager,
                                    fg_color="#95a5a6", hover_color="#7f8c8d",
                                    height=50, corner_radius=10)
        back_button.pack(padx=20, pady=(0, 20), fill=tk.X)

    def edit_card(self, card_index):
        card = self.current_set.cards[card_index]
        new_front = simpledialog.askstring("Edit Card", "Enter the new question:", initialvalue=card.front)
        new_back = simpledialog.askstring("Edit Card", "Enter the new answer:", initialvalue=card.back)
        if new_front and new_back:
            self.current_set.edit_card(card_index, new_front, new_back)
        self.show_edit_screen()

    def delete_card(self, card_index):
        if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete this card?"):
            self.current_set.delete_card(card_index)
        self.show_edit_screen()

    def add_card_to_current_set(self):
        front = simpledialog.askstring("New Card", "Enter the question:")
        if front:
            back = simpledialog.askstring("New Card", "Enter the answer:")
            if back:
                self.current_set.add_card(front, back)
        self.show_edit_screen()

    def on_closing(self):
        """ Handle the window closing event."""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def show_help_screen(self):
        """Explain how app works"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Header
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="#3498db", corner_radius=0)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(header_frame, text="Help", font=("Roboto", 24, "bold"), text_color="white").pack(pady=20)

        # Help text
        help_text = "help text"
        ctk.CTkLabel(self.main_frame, text=help_text, font=("Roboto", 14)).pack(pady=20)

        # Back button
        back_button = ctk.CTkButton(self.main_frame, text="Back to Decks",
                                    command=self.show_deck_manager,
                                    fg_color="#95a5a6", hover_color="#7f8c8d",
                                    height=50, corner_radius=10)
        back_button.pack(padx=20, pady=(0, 20), fill=tk.X)




if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardGUI(root)
    root.mainloop()
