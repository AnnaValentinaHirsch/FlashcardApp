import tkinter as tk
import customtkinter as ctk
import random

class LearningSession:
    def __init__(self, app):
        self.app = app
        self.current_card_index = 0
        self.cards_to_review = []
        self.reviewed_cards = 0

    def start_learning(self, set_index):
        self.app.current_set = self.app.flashcard_sets[set_index]
        if not self.app.current_set.cards:
            self.show_empty_deck_message(set_index)
        else:
            self.initialize_session()
            self.show_flashcard()

    def initialize_session(self):
        self.current_card_index = 0
        self.cards_to_review = self.app.current_set.cards.copy()
        random.shuffle(self.cards_to_review)
        self.reviewed_cards = 0

    def show_flashcard(self):
        for widget in self.app.main_frame.winfo_children():
            widget.destroy()

        if self.reviewed_cards >= len(self.cards_to_review):
            self.end_learning_session(completed=True)
            return

        card = self.cards_to_review[self.current_card_index]

        header_frame = ctk.CTkFrame(
            self.app.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text=f"{self.app.current_set.title} - Card {self.reviewed_cards + 1}/{len(self.cards_to_review)}",
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        card_frame = ctk.CTkFrame(self.app.main_frame, fg_color="white", corner_radius=10)
        card_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        question_label = ctk.CTkLabel(
            card_frame, text=card.front, font=("Roboto", 18), wraplength=300
        )
        question_label.pack(pady=(40, 20), padx=20)

        self.user_answer_entry = ctk.CTkEntry(card_frame, width=300)
        self.user_answer_entry.pack(pady=10)
        self.user_answer_entry.bind("<Return>", lambda event: self.check_answer())

        self.answer_message_label = ctk.CTkLabel(
            card_frame, text="", font=("Roboto", 16), wraplength=300
        )
        self.answer_message_label.pack(pady=10, padx=20)

        self.button_frame = ctk.CTkFrame(card_frame, fg_color="transparent")
        self.button_frame.pack(pady=10)

        self.check_answer_btn = ctk.CTkButton(
            self.button_frame,
            text="Check Answer",
            command=self.check_answer,
            fg_color="#3498db",
            hover_color="#2980b9",
        )
        self.check_answer_btn.pack(side=tk.LEFT, padx=5)

        self.show_answer_btn = ctk.CTkButton(
            self.button_frame,
            text="Show Answer",
            command=self.show_answer,
            fg_color="#95a5a6",
            hover_color="#7f8c8d",
        )
        self.show_answer_btn.pack(side=tk.LEFT, padx=5)

        self.create_navigation_buttons()

    def create_navigation_buttons(self):
        nav_frame = ctk.CTkFrame(self.app.main_frame, fg_color="transparent")
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
            self.app.main_frame,
            text="End Session",
            command=lambda: self.end_learning_session(completed=False),
            fg_color="#e74c3c",
            hover_color="#c0392b",
        ).pack(pady=10)

    def check_answer(self):
        user_answer = self.user_answer_entry.get()
        card = self.cards_to_review[self.current_card_index]
        if user_answer.strip().lower() == card.back.strip().lower():
            card.mark_correct()
            self.answer_message_label.configure(text="Correct!", text_color="green")
            self.show_continue_button()
        else:
            card.mark_incorrect()
            self.answer_message_label.configure(text="Incorrect. Try again or show the answer.", text_color="red")

    def show_answer(self):
        card = self.cards_to_review[self.current_card_index]
        self.answer_message_label.configure(text=f"The correct answer is: {card.back}", text_color="blue")
        self.show_continue_button()

    def show_continue_button(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        continue_button = ctk.CTkButton(
            self.button_frame,
            text="Continue",
            command=self.next_card,
            fg_color="#2ecc71",
            hover_color="#27ae60",
        )
        continue_button.pack(pady=10)
        continue_button.focus_set()
        continue_button.bind("<Return>", lambda event: continue_button.invoke())

    def prev_card(self):
        if self.current_card_index > 0:
            self.current_card_index -= 1
            self.reviewed_cards = max(0, self.reviewed_cards - 1)
        self.show_flashcard()

    def next_card(self):
        self.reviewed_cards += 1
        if self.current_card_index < len(self.cards_to_review) - 1:
            self.current_card_index += 1
        else:
            self.current_card_index = 0
        self.show_flashcard()

    def end_learning_session(self, completed=False):
        for widget in self.app.main_frame.winfo_children():
            widget.destroy()

        header_frame = ctk.CTkFrame(self.app.main_frame, fg_color="#3498db", corner_radius=0)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(header_frame, text="Session Ended", font=("Roboto", 24, "bold"), text_color="white").pack(pady=20)

        message_frame = ctk.CTkFrame(self.app.main_frame, fg_color="white", corner_radius=10)
        message_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        if completed:
            message = "Congratulations! You have reviewed all cards in this deck!"
            ctk.CTkLabel(message_frame, text=message, font=("Roboto", 18, "bold"), wraplength=300).pack(pady=20)

            return_button = ctk.CTkButton(
                message_frame,
                text="Return to Main Menu",
                command=self.app.deck_manager.show_deck_manager,
                fg_color="#2ecc71",
                hover_color="#27ae60",
            )
            return_button.pack(pady=20)
            return_button.focus_set()
            return_button.bind("<Return>", lambda event: return_button.invoke())
        else:
            cards_left = len(self.cards_to_review) - self.reviewed_cards
            message = f"You have reviewed {self.reviewed_cards} out of {len(self.cards_to_review)} cards. There are {cards_left} cards left to review."
            ctk.CTkLabel(message_frame, text=message, font=("Roboto", 14), wraplength=300).pack(pady=20)

            button_frame = ctk.CTkFrame(message_frame, fg_color="transparent")
            button_frame.pack(pady=10)

            quit_button = ctk.CTkButton(
                button_frame,
                text="Quit Anyways",
                command=self.app.deck_manager.show_deck_manager,
                fg_color="#e74c3c",
                hover_color="#c0392b",
            )
            quit_button.pack(side=tk.LEFT, padx=10)
            quit_button.focus_set()
            quit_button.bind("<Return>", lambda event: quit_button.invoke())

            continue_button = ctk.CTkButton(
                button_frame,
                text="Continue Learning",
                command=self.show_flashcard,
                fg_color="#2ecc71",
                hover_color="#27ae60",
            )
            continue_button.pack(side=tk.LEFT, padx=10)

    def show_empty_deck_message(self, set_index):
        for widget in self.app.main_frame.winfo_children():
            widget.destroy()

        header_frame = ctk.CTkFrame(self.app.main_frame, fg_color="#3498db", corner_radius=0)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(header_frame, text="Empty Deck", font=("Roboto", 24, "bold"), text_color="white").pack(pady=20)

        message_frame = ctk.CTkFrame(self.app.main_frame, fg_color="white", corner_radius=10)
        message_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        ctk.CTkLabel(message_frame, text="This deck has no cards. Would you like to add some cards?", font=("Roboto", 14), wraplength=300).pack(pady=20)

        button_frame = ctk.CTkFrame(message_frame, fg_color="transparent")
        button_frame.pack(pady=10)

        ctk.CTkButton(
            button_frame,
            text="Add Cards",
            command=lambda: self.app.card_editor.show_add_cards_input(),
            fg_color="#2ecc71",
            hover_color="#27ae60",
        ).pack(side=tk.LEFT, padx=10)

        ctk.CTkButton(
            button_frame,
            text="Back to Decks",
            command=self.app.deck_manager.show_deck_manager,
            fg_color="#3498db",
            hover_color="#2980b9",
        ).pack(side=tk.LEFT, padx=10)
