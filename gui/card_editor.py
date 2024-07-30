import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

import tkinter as tk
import customtkinter as ctk

class CardEditor:
    def __init__(self, app):
        self.app = app

    def show_add_cards_input(self):
        """
        Show the input fields for adding new cards to the current set.

        UI Specifications:
            - Create a header frame with a title that includes the current set's title.
            - Create an input frame with two input fields for the question and answer of the card.
            - Create a feedback label to display messages to the user.
            - Create an "Add Card" button that calls the add_card_from_input method.
            - Create a "Finish Adding Cards" button that calls the finish_adding_cards method.

        Keyboard Bindings:
            - Pressing the Enter key on the question input field should focus on the answer input field.
            - Pressing the Enter key on the answer input field should call the add_card_from_input method.
        """
        # Clear the main frame
        for widget in self.app.main_frame.winfo_children():
            widget.destroy()

        # Create the header frame
        header_frame = ctk.CTkFrame(
            self.app.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text=f"Add Cards to {self.app.current_set.title}",
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        # Create the input frame
        input_frame = ctk.CTkFrame(self.app.main_frame, fg_color="white", corner_radius=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Question Entry
        ctk.CTkLabel(input_frame, text="Question:", font=("Roboto", 16)).pack(
            anchor="w", padx=15, pady=(10, 5)
        )
        self.card_question_entry = ctk.CTkEntry(input_frame, width=300)
        self.card_question_entry.pack(pady=10)
        self.card_question_entry.bind("<Return>", lambda event: self.card_answer_entry.focus_set())

        # Answer Entry
        ctk.CTkLabel(input_frame, text="Answer:", font=("Roboto", 16)).pack(
            anchor="w", padx=15, pady=(10, 5)
        )

        self.card_answer_entry = ctk.CTkEntry(input_frame, width=300)
        self.card_answer_entry.pack(pady=10)
        self.card_answer_entry.bind("<Return>", lambda event: self.add_card_from_input())

        # Feedback Label
        self.feedback_label = ctk.CTkLabel(input_frame, text="", font=("Roboto", 14))
        self.feedback_label.pack(pady=10)

        # Add Card Button
        add_button = ctk.CTkButton(
            input_frame,
            text="Add Card",
            command=self.add_card_from_input,
            fg_color="#2ecc71",
            hover_color="#27ae60",
        )
        add_button.pack(pady=10)

        # Finish Adding Cards Button
        finish_button = ctk.CTkButton(
            input_frame,
            text="Finish Adding Cards",
            command=self.finish_adding_cards,
            fg_color="#3498db",
            hover_color="#2980b9",
        )
        finish_button.pack(pady=10)

    def add_card_from_input(self):
        """
        Add a card to the current set using the input fields. Checks if both fields are filled.
        """
        # Retrieve question and answer from the input fields
        front = self.card_question_entry.get()
        back = self.card_answer_entry.get()

        # Check if both fields (Question & Answer) are filled
        if front and back:
            self.app.current_set.add_card(front, back)
            self.card_question_entry.delete(0, tk.END)
            self.card_answer_entry.delete(0, tk.END)
            self.feedback_label.configure(text="Card added successfully!", text_color="green")
            self.card_question_entry.focus_set()
        else:
            self.feedback_label.configure(text="Please fill in both question and answer.", text_color="red")


    def finish_adding_cards(self):
        """
        Finish adding cards to the current set and return to the deck manager screen.
        The last added content is automatically saved if the input fields are filled.
        """
        front = self.card_question_entry.get()
        back = self.card_answer_entry.get()
        if front and back:
            self.app.current_set.add_card(front, back)
        self.app.deck_manager.show_deck_manager()

    def edit_set(self, set_index):
        """
        Set the current set to the set at the given index and show the edit screen.
        """
        self.app.current_set = self.app.flashcard_sets[set_index]
        self.show_edit_screen()

    def show_edit_screen(self):
        """
        Show the edit screen for the current set.
        """
        # Clear the main frame
        for widget in self.app.main_frame.winfo_children():
            widget.destroy()

        # Create the header frame
        header_frame = ctk.CTkFrame(
            self.app.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text=f"Editing: {self.app.current_set.title}",
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        # Make the frame scrollable
        scroll_frame = ctk.CTkScrollableFrame(self.app.main_frame, fg_color="#F0F0F0")
        scroll_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        # Display each card in the set with edit and delete buttons
        for i, card in enumerate(self.app.current_set.cards):
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

        # Add New Card Button
        new_card_button = ctk.CTkButton(
            self.app.main_frame,
            text="+ Add New Card",
            command=self.show_add_cards_input,
            fg_color="#2ecc71",
            hover_color="#27ae60",
            height=50,
            corner_radius=10,
        )
        new_card_button.pack(padx=20, pady=(0, 10), fill=tk.X)

        # Delete Deck Button
        delete_deck_button = ctk.CTkButton(
            self.app.main_frame,
            text="Delete Deck",
            command=self.delete_current_deck,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            height=50,
            corner_radius=10,
        )
        delete_deck_button.pack(padx=20, pady=(0, 10), fill=tk.X)

        # Back Button
        back_button = ctk.CTkButton(
            self.app.main_frame,
            text="Back to Decks",
            command=self.app.deck_manager.show_deck_manager,
            fg_color="#95a5a6",
            hover_color="#7f8c8d",
            height=50,
            corner_radius=10,
        )
        back_button.pack(padx=20, pady=(0, 20), fill=tk.X)

    def show_edit_card_input(self, card_index):
        """
        Show the input fields to edit the card at the given index.
        """
        # Get the card index to edit
        card = self.app.current_set.cards[card_index]
        # Clear the main frame
        for widget in self.app.main_frame.winfo_children():
            widget.destroy()

        # Create the header frame
        header_frame = ctk.CTkFrame(
            self.app.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text=f"Edit Card in {self.app.current_set.title}",
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        # Create the input frame
        input_frame = ctk.CTkFrame(self.app.main_frame, fg_color="white", corner_radius=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        ctk.CTkLabel(input_frame, text="Question:", font=("Roboto", 16)).pack(
            anchor="w", padx=15, pady=(10, 5)
        )
        # Question Entry
        self.edit_card_question_entry = ctk.CTkEntry(input_frame, width=300)
        self.edit_card_question_entry.insert(0, card.front)
        self.edit_card_question_entry.pack(pady=10)

        ctk.CTkLabel(input_frame, text="Answer:", font=("Roboto", 16)).pack(
            anchor="w", padx=15, pady=(10, 5)
        )
        # Answer Entry
        self.edit_card_answer_entry = ctk.CTkEntry(input_frame, width=300)
        self.edit_card_answer_entry.insert(0, card.back)
        self.edit_card_answer_entry.pack(pady=10)

        # Save Changes Button
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
        """
        Save the changes made to the card.
        """
        new_front = self.edit_card_question_entry.get()
        new_back = self.edit_card_answer_entry.get()
        if new_front and new_back:
            self.app.current_set.edit_card(card_index, new_front, new_back)
        self.show_edit_screen()

    def delete_current_deck(self):
        """
        Delete the current deck from the app's flashcard_sets list. Ask for confirmation before deleting.
        """
        if messagebox.askyesno(
                "Confirm Deletion",
                f"Are you sure you want to delete the deck '{self.app.current_set.title}'?",
        ):
            self.app.flashcard_sets.remove(self.app.current_set)
            self.app.deck_manager.show_deck_manager()

    def delete_card(self, card_index):
        """
        Delete the card from the current set. Ask for confirmation before deleting.
        """
        if messagebox.askyesno(
                "Confirm Deletion", f"Are you sure you want to delete this card?"
        ):
            self.app.current_set.delete_card(card_index)
        self.show_edit_screen()