import tkinter as tk
from tkinter import messagebox, simpledialog, ttk, filedialog
import customtkinter as ctk
import random
import json
from help_screen import HelpScreen  # Import the HelpScreen class from help_screen.py


class FlashCard:
    """Class to represent a flashcard."""

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


class FlashCardSet:
    """Class to represent a set of flashcards."""

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
            "cards": [{"front": card.front, "back": card.back} for card in self.cards],
        }

    @classmethod
    def from_dict(cls, data):
        set_instance = cls(data["title"])
        for card_data in data["cards"]:
            set_instance.add_card(card_data["front"], card_data["back"])
        return set_instance

    def total_score(self):
        return sum(card.correct_count for card in self.cards)

    def success_rate(self):
        total_reviews = sum(card.review_count for card in self.cards)
        total_correct = sum(card.correct_count for card in self.cards)
        if total_reviews == 0:
            return 0
        return (total_correct / total_reviews) * 100


class FlashcardGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")
        self.root.geometry("400x600")
        self.root.minsize(400, 600)

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

        header_frame = ctk.CTkFrame(
            self.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text="Your Decks",
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        scroll_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color="#F0F0F0")
        scroll_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        for i, deck in enumerate(self.flashcard_sets):
            self.create_deck_card(scroll_frame, deck, i)

        new_deck_button = ctk.CTkButton(
            self.main_frame,
            text="+ Create New Deck",
            command=self.show_new_deck_input,
            fg_color="#2ecc71",
            hover_color="#27ae60",
            height=50,
            corner_radius=10,
        )
        new_deck_button.pack(padx=20, pady=(0, 20), fill=tk.X)

        export_button = ctk.CTkButton(
            self.main_frame,
            text="Export Decks",
            command=self.export_flashcard_sets,
            fg_color="#3498db",
            hover_color="#2980b9",
            height=50,
            corner_radius=10,
        )
        export_button.pack(padx=20, pady=(0, 10), fill=tk.X)

        import_button = ctk.CTkButton(
            self.main_frame,
            text="Import Decks",
            command=self.import_flashcard_sets,
            fg_color="#3498db",
            hover_color="#2980b9",
            height=50,
            corner_radius=10,
        )
        import_button.pack(padx=20, pady=(0, 10), fill=tk.X)

        stats_button = ctk.CTkButton(
            self.main_frame,
            text="Statistics",
            command=self.show_statistics,
            fg_color="#3498db",
            hover_color="#2980b9",
            height=50,
            corner_radius=10,
        )
        stats_button.pack(padx=20, pady=(0, 10), fill=tk.X)

        exit_button = ctk.CTkButton(
            self.main_frame,
            text="Exit",
            command=self.on_closing,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            height=50,
            corner_radius=10,
        )
        exit_button.pack(padx=20, pady=(0, 20), fill=tk.X)

        help_button = ctk.CTkButton(
            self.main_frame,
            text="Help",
            command=self.show_help_screen,
            fg_color="#3498db",
            hover_color="#2980b9",
            height=50,
            corner_radius=10,
        )
        help_button.pack(padx=20, pady=(0, 20), fill=tk.X)

    def create_deck_card(self, parent, deck, index):
        card_frame = ctk.CTkFrame(parent, fg_color="white", corner_radius=10)
        card_frame.pack(fill=tk.X, pady=5)

        ctk.CTkLabel(card_frame, text=deck.title, font=("Roboto", 18, "bold")).pack(
            anchor="w", padx=15, pady=(10, 5)
        )
        ctk.CTkLabel(
            card_frame, text=f"{len(deck.cards)} cards", font=("Roboto", 14)
        ).pack(anchor="w", padx=15, pady=(0, 10))

        button_frame = ctk.CTkFrame(card_frame, fg_color="transparent")
        button_frame.pack(fill=tk.X, padx=15, pady=(0, 10))

        ctk.CTkButton(
            button_frame,
            text="Study",
            command=lambda: self.start_learning(index),
            fg_color="#3498db",
            hover_color="#2980b9",
            width=80,
        ).pack(side=tk.LEFT, padx=(0, 10))
        ctk.CTkButton(
            button_frame,
            text="Edit",
            command=lambda: self.edit_set(index),
            fg_color="#f39c12",
            hover_color="#d35400",
            width=80,
        ).pack(side=tk.LEFT)
        ctk.CTkButton(
            button_frame,
            text="Statistics",
            command=lambda: self.show_individual_statistics(index),
            fg_color="#3498db",
            hover_color="#2980b9",
            width=80,
        ).pack(side=tk.LEFT)

    def show_new_deck_input(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        header_frame = ctk.CTkFrame(
            self.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text="Create New Deck",
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        input_frame = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        ctk.CTkLabel(input_frame, text="Deck Title:", font=("Roboto", 16)).pack(
            anchor="w", padx=15, pady=(10, 5)
        )
        self.new_deck_title_entry = ctk.CTkEntry(input_frame, width=300)
        self.new_deck_title_entry.pack(pady=10)

        ctk.CTkButton(
            input_frame,
            text="Create Deck",
            command=self.create_new_set_from_input,
            fg_color="#2ecc71",
            hover_color="#27ae60",
        ).pack(pady=10)
        ctk.CTkButton(
            input_frame,
            text="Cancel",
            command=self.show_deck_manager,
            fg_color="#95a5a6",
            hover_color="#7f8c8d",
        ).pack(pady=10)

    def create_new_set_from_input(self):
        title = self.new_deck_title_entry.get()
        if title:
            new_set = FlashCardSet(title)
            self.flashcard_sets.append(new_set)
            self.current_set = new_set
            self.show_add_cards_input()

    def show_add_cards_input(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        header_frame = ctk.CTkFrame(
            self.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text=f"Add Cards to {self.current_set.title}",
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        input_frame = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        ctk.CTkLabel(input_frame, text="Question:", font=("Roboto", 16)).pack(
            anchor="w", padx=15, pady=(10, 5)
        )
        self.card_question_entry = ctk.CTkEntry(input_frame, width=300)
        self.card_question_entry.pack(pady=10)

        ctk.CTkLabel(input_frame, text="Answer:", font=("Roboto", 16)).pack(
            anchor="w", padx=15, pady=(10, 5)
        )
        self.card_answer_entry = ctk.CTkEntry(input_frame, width=300)
        self.card_answer_entry.pack(pady=10)

        ctk.CTkButton(
            input_frame,
            text="Add Card",
            command=self.add_card_from_input,
            fg_color="#2ecc71",
            hover_color="#27ae60",
        ).pack(pady=10)
        ctk.CTkButton(
            input_frame,
            text="Finish Adding Cards",
            command=self.show_deck_manager,
            fg_color="#3498db",
            hover_color="#2980b9",
        ).pack(pady=10)

    def add_card_from_input(self):
        front = self.card_question_entry.get()
        back = self.card_answer_entry.get()
        if front and back:
            self.current_set.add_card(front, back)
            self.card_question_entry.delete(0, tk.END)
            self.card_answer_entry.delete(0, tk.END)

    def start_learning(self, set_index):
        self.current_set = self.flashcard_sets[set_index]
        if not self.current_set.cards:
            messagebox.showinfo(
                "Empty Deck", "This deck has no cards. Add some cards first."
            )
            return

        self.current_card_index = 0
        random.shuffle(self.current_set.cards)
        self.show_flashcard()

    def show_flashcard(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        card = self.current_set.cards[self.current_card_index]

        header_frame = ctk.CTkFrame(
            self.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text=self.current_set.title,
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        card_frame = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=10)
        card_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        question_label = ctk.CTkLabel(
            card_frame, text=card.front, font=("Roboto", 18), wraplength=300
        )
        question_label.pack(pady=(40, 20), padx=20)

        self.user_answer_entry = ctk.CTkEntry(card_frame, width=300)
        self.user_answer_entry.pack(pady=10)

        self.answer_message_label = ctk.CTkLabel(
            card_frame, text="", font=("Roboto", 16), wraplength=300
        )
        self.answer_message_label.pack(pady=10, padx=20)

        self.user_answer_entry.bind(
            "<Return>", lambda event: self.check_answer(self.user_answer_entry.get())
        )

        check_answer_btn = ctk.CTkButton(
            card_frame,
            text="Check Answer",
            command=lambda: self.check_answer(self.user_answer_entry.get()),
            fg_color="#3498db",
            hover_color="#2980b9",
        )
        check_answer_btn.pack(pady=10)

        nav_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        nav_frame.pack(fill=tk.X, padx=20, pady=20)

        ctk.CTkButton(
            nav_frame,
            text="Previous",
            command=self.prev_card,
            fg_color="#95a5a6",
            hover_color="#7f8c8d",
            width=100,
        ).pack(side=tk.LEFT)
        ctk.CTkButton(
            nav_frame,
            text="Next",
            command=self.next_card,
            fg_color="#2ecc71",
            hover_color="#27ae60",
            width=100,
        ).pack(side=tk.RIGHT)
        ctk.CTkButton(
            self.main_frame,
            text="End Session",
            command=self.show_deck_manager,
            fg_color="#e74c3c",
            hover_color="#c0392b",
        ).pack(pady=10)

    def check_answer(self, user_answer):
        card = self.current_set.cards[self.current_card_index]
        if user_answer.strip().lower() == card.back.strip().lower():
            card.mark_correct()
            self.answer_message_label.configure(text="Correct!", text_color="green")
            self.user_answer_entry.configure(border_color="green")
        else:
            card.mark_incorrect()
            self.answer_message_label.configure(
                text=f"Incorrect! The correct answer was: {card.back}", text_color="red"
            )
            self.user_answer_entry.configure(border_color="red")

    def show_answer(self, answer_label):
        card = self.current_set.cards[self.current_card_index]
        answer_label.configure(text=card.back)

    def prev_card(self):
        self.current_card_index = (self.current_card_index - 1) % len(
            self.current_set.cards
        )
        self.show_flashcard()

    def next_card(self):
        self.current_card_index = (self.current_card_index + 1) % len(
            self.current_set.cards
        )
        self.show_flashcard()

    def edit_set(self, set_index):
        self.current_set = self.flashcard_sets[set_index]
        self.show_edit_screen()

    def show_edit_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        header_frame = ctk.CTkFrame(
            self.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text=f"Editing: {self.current_set.title}",
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        scroll_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color="#F0F0F0")
        scroll_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        for i, card in enumerate(self.current_set.cards):
            card_frame = ctk.CTkFrame(scroll_frame, fg_color="white", corner_radius=10)
            card_frame.pack(fill=tk.X, pady=5)

            ctk.CTkLabel(
                card_frame, text=f"Q: {card.front[:30]}...", font=("Roboto", 14, "bold")
            ).pack(anchor="w", padx=15, pady=(10, 5))
            ctk.CTkLabel(
                card_frame, text=f"A: {card.back[:30]}...", font=("Roboto", 12)
            ).pack(anchor="w", padx=15, pady=(0, 10))

            button_frame = ctk.CTkFrame(card_frame, fg_color="transparent")
            button_frame.pack(fill=tk.X, padx=15, pady=(0, 10))

            ctk.CTkButton(
                button_frame,
                text="Edit",
                command=lambda x=i: self.show_edit_card_input(x),
                fg_color="#f39c12",
                hover_color="#d35400",
                width=60,
            ).pack(side=tk.LEFT, padx=(0, 10))
            ctk.CTkButton(
                button_frame,
                text="Delete",
                command=lambda x=i: self.delete_card(x),
                fg_color="#e74c3c",
                hover_color="#c0392b",
                width=60,
            ).pack(side=tk.LEFT)

        new_card_button = ctk.CTkButton(
            self.main_frame,
            text="+ Add New Card",
            command=self.show_add_cards_input,
            fg_color="#2ecc71",
            hover_color="#27ae60",
            height=50,
            corner_radius=10,
        )
        new_card_button.pack(padx=20, pady=(0, 10), fill=tk.X)

        delete_deck_button = ctk.CTkButton(
            self.main_frame,
            text="Delete Deck",
            command=self.delete_current_deck,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            height=50,
            corner_radius=10,
        )
        delete_deck_button.pack(padx=20, pady=(0, 10), fill=tk.X)

        back_button = ctk.CTkButton(
            self.main_frame,
            text="Back to Decks",
            command=self.show_deck_manager,
            fg_color="#95a5a6",
            hover_color="#7f8c8d",
            height=50,
            corner_radius=10,
        )
        back_button.pack(padx=20, pady=(0, 20), fill=tk.X)

    def show_edit_card_input(self, card_index):
        card = self.current_set.cards[card_index]
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        header_frame = ctk.CTkFrame(
            self.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text=f"Edit Card in {self.current_set.title}",
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        input_frame = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        ctk.CTkLabel(input_frame, text="Question:", font=("Roboto", 16)).pack(
            anchor="w", padx=15, pady=(10, 5)
        )
        self.edit_card_question_entry = ctk.CTkEntry(input_frame, width=300)
        self.edit_card_question_entry.insert(0, card.front)
        self.edit_card_question_entry.pack(pady=10)

        ctk.CTkLabel(input_frame, text="Answer:", font=("Roboto", 16)).pack(
            anchor="w", padx=15, pady=(10, 5)
        )
        self.edit_card_answer_entry = ctk.CTkEntry(input_frame, width=300)
        self.edit_card_answer_entry.insert(0, card.back)
        self.edit_card_answer_entry.pack(pady=10)

        ctk.CTkButton(
            input_frame,
            text="Save Changes",
            command=lambda: self.save_card_edit(card_index),
            fg_color="#2ecc71",
            hover_color="#27ae60",
        ).pack(pady=10)
        ctk.CTkButton(
            input_frame,
            text="Cancel",
            command=self.show_edit_screen,
            fg_color="#95a5a6",
            hover_color="#7f8c8d",
        ).pack(pady=10)

    def save_card_edit(self, card_index):
        new_front = self.edit_card_question_entry.get()
        new_back = self.edit_card_answer_entry.get()
        if new_front and new_back:
            self.current_set.edit_card(card_index, new_front, new_back)
        self.show_edit_screen()

    def delete_current_deck(self):
        if messagebox.askyesno(
            "Confirm Deletion",
            f"Are you sure you want to delete the deck '{self.current_set.title}'?",
        ):
            self.flashcard_sets.remove(self.current_set)
            self.show_deck_manager()

    def delete_card(self, card_index):
        if messagebox.askyesno(
            "Confirm Deletion", f"Are you sure you want to delete this card?"
        ):
            self.current_set.delete_card(card_index)
        self.show_edit_screen()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def show_help_screen(self):
        help_screen = HelpScreen(self.main_frame)
        help_screen.show()

        back_button = ctk.CTkButton(
            self.main_frame,
            text="Back to Decks",
            command=self.show_deck_manager,
            fg_color="#95a5a6",
            hover_color="#7f8c8d",
            height=50,
            corner_radius=10,
        )
        back_button.pack(padx=20, pady=(0, 20), fill=tk.X)

    def export_flashcard_sets(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
        )
        if file_path:
            data = [flashcard_set.to_dict() for flashcard_set in self.flashcard_sets]
            with open(file_path, "w") as file:
                json.dump(data, file)
            messagebox.showinfo(
                "Export Successful", f"Flashcard sets have been exported to {file_path}"
            )

    def import_flashcard_sets(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
        )
        if file_path:
            with open(file_path, "r") as file:
                data = json.load(file)
            imported_sets = [FlashCardSet.from_dict(set_data) for set_data in data]
            self.flashcard_sets.extend(imported_sets)
            self.show_deck_manager()
            messagebox.showinfo(
                "Import Successful",
                f"Flashcard sets have been imported from {file_path}",
            )

    def show_statistics(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        header_frame = ctk.CTkFrame(
            self.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text="Overall Statistics",
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        stats_frame = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=10)
        stats_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        total_correct = sum(
            card.correct_count for deck in self.flashcard_sets for card in deck.cards
        )
        total_reviews = sum(
            card.review_count for deck in self.flashcard_sets for card in deck.cards
        )

        if total_reviews == 0:
            success_rate = 0
        else:
            success_rate = (total_correct / total_reviews) * 100

        ctk.CTkLabel(
            stats_frame, text=f"Total Score: {total_correct}", font=("Roboto", 18)
        ).pack(pady=10)
        ctk.CTkLabel(
            stats_frame, text=f"Success Rate: {success_rate:.2f}%", font=("Roboto", 18)
        ).pack(pady=10)

        individual_stats_frame = ctk.CTkScrollableFrame(stats_frame, fg_color="white")
        individual_stats_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(10, 20))

        for deck in self.flashcard_sets:
            deck_frame = ctk.CTkFrame(
                individual_stats_frame, fg_color="white", corner_radius=10
            )
            deck_frame.pack(fill=tk.X, pady=5)

            deck_score = deck.total_score()
            deck_success_rate = deck.success_rate()

            ctk.CTkLabel(
                deck_frame, text=f"Deck: {deck.title}", font=("Roboto", 14, "bold")
            ).pack(anchor="w", padx=15, pady=(10, 5))
            ctk.CTkLabel(
                deck_frame, text=f"Score: {deck_score}", font=("Roboto", 12)
            ).pack(anchor="w", padx=15, pady=(0, 5))
            ctk.CTkLabel(
                deck_frame,
                text=f"Success Rate: {deck_success_rate:.2f}%",
                font=("Roboto", 12),
            ).pack(anchor="w", padx=15, pady=(0, 10))

        # Back button
        back_button = ctk.CTkButton(
            self.main_frame,
            text="Back to Decks",
            command=self.show_deck_manager,
            fg_color="#95a5a6",
            hover_color="#7f8c8d",
            height=50,
            corner_radius=10,
        )
        back_button.pack(padx=20, pady=(0, 20), fill=tk.X, side=tk.BOTTOM)

    def show_individual_statistics(self, set_index):
        self.current_set = self.flashcard_sets[set_index]
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        header_frame = ctk.CTkFrame(
            self.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text=f"Statistics: {self.current_set.title}",
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        stats_frame = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=10)
        stats_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        total_score = self.current_set.total_score()
        success_rate = self.current_set.success_rate()

        ctk.CTkLabel(
            stats_frame, text=f"Total Score: {total_score}", font=("Roboto", 18)
        ).pack(pady=10)
        ctk.CTkLabel(
            stats_frame, text=f"Success Rate: {success_rate:.2f}%", font=("Roboto", 18)
        ).pack(pady=10)

        stats_scroll_frame = ctk.CTkScrollableFrame(stats_frame, fg_color="white")
        stats_scroll_frame.pack(fill=tk.BOTH, expand=True)

        for i, card in enumerate(self.current_set.cards):
            card_frame = ctk.CTkFrame(
                stats_scroll_frame, fg_color="white", corner_radius=10
            )
            card_frame.pack(fill=tk.X, pady=5)

            ctk.CTkLabel(
                card_frame, text=f"Q: {card.front}", font=("Roboto", 14, "bold")
            ).pack(anchor="w", padx=15, pady=(10, 5))
            ctk.CTkLabel(card_frame, text=f"A: {card.back}", font=("Roboto", 12)).pack(
                anchor="w", padx=15, pady=(0, 10)
            )
            ctk.CTkLabel(
                card_frame,
                text=f"Reviewed: {card.review_count} times",
                font=("Roboto", 12),
            ).pack(anchor="w", padx=15, pady=(0, 10))
            ctk.CTkLabel(
                card_frame,
                text=f"Correct: {card.correct_count} times",
                font=("Roboto", 12),
            ).pack(anchor="w", padx=15, pady=(0, 10))
            ctk.CTkLabel(
                card_frame,
                text=f"Success Rate: {card.success_rate():.2f}%",
                font=("Roboto", 12),
            ).pack(anchor="w", padx=15, pady=(0, 10))

        # Back button
        back_button = ctk.CTkButton(
            self.main_frame,
            text="Back to Decks",
            command=self.show_deck_manager,
            fg_color="#95a5a6",
            hover_color="#7f8c8d",
            height=50,
            corner_radius=10,
        )
        back_button.pack(padx=20, pady=(0, 20), fill=tk.X, side=tk.BOTTOM)


if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardGUI(root)
    root.mainloop()
