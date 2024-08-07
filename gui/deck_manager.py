import tkinter as tk
import customtkinter as ctk
from cards.flashcard_set import FlashCardSet

class DeckManager:
    def __init__(self, app):
        self.new_deck_title_entry = None
        self.app = app

    def show_deck_manager(self):
        """
        Show the deck manager screen. This screen displays all the decks the user has created or imported.
        """
        # Clear the main frame
        for widget in self.app.main_frame.winfo_children():
            widget.destroy()

        # Create the header
        header_frame = ctk.CTkFrame(
            self.app.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text="Your Decks",
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        # Make frame scrollable
        scroll_frame = ctk.CTkScrollableFrame(self.app.main_frame, fg_color="#F0F0F0")
        scroll_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        self.app.bind_mousewheel(scroll_frame)

        for i, deck in enumerate(self.app.flashcard_sets):
            self.create_deck_card(scroll_frame, deck, i)

        # Create buttons
        new_deck_button = ctk.CTkButton(
            self.app.main_frame,
            text="+ Create New Deck",
            command=self.show_new_deck_input,
            fg_color="#2ecc71",
            hover_color="#27ae60",
            height=50,
            corner_radius=10,
        )
        new_deck_button.pack(padx=20, pady=(0, 10), fill=tk.X)

        export_button = ctk.CTkButton(
            self.app.main_frame,
            text="Export Decks",
            command=self.app.file_operations.export_flashcard_sets,
            fg_color="#3498db",
            hover_color="#2980b9",
            height=50,
            corner_radius=10,
        )
        export_button.pack(padx=20, pady=(0, 10), fill=tk.X)

        import_button = ctk.CTkButton(
            self.app.main_frame,
            text="Import Decks",
            command=self.app.file_operations.import_flashcard_sets,
            fg_color="#9b59b6",
            hover_color="#8e44ad",
            height=50,
            corner_radius=10,
        )
        import_button.pack(padx=20, pady=(0, 10), fill=tk.X)

        stats_button = ctk.CTkButton(
            self.app.main_frame,
            text="Statistics",
            command=self.app.statistics.show_statistics,
            fg_color="#f1c40f",
            hover_color="#f39c12",
            height=50,
            corner_radius=10,
        )
        stats_button.pack(padx=20, pady=(0, 10), fill=tk.X)

        help_button = ctk.CTkButton(
            self.app.main_frame,
            text="Help",
            command=self.app.help_screen.show,
            fg_color="#1abc9c",
            hover_color="#16a085",
            height=50,
            corner_radius=10,
        )
        help_button.pack(padx=20, pady=(0, 10), fill=tk.X)

        exit_button = ctk.CTkButton(
            self.app.main_frame,
            text="Exit",
            command=self.app.on_closing,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            height=50,
            corner_radius=10,
        )
        exit_button.pack(padx=20, pady=(0, 20), fill=tk.X)

    def create_deck_card(self, parent, deck, index):
        """
        Create a card that represents a deck. This card displays the deck's title and the number of cards in the deck.
        """
        # Create the card frame
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

        # Start Learning Button
        ctk.CTkButton(
            button_frame,
            text="Study",
            command=lambda: self.app.learning_session.start_learning(index),
            fg_color="#3498db",
            hover_color="#2980b9",
            width=80,
        ).pack(side=tk.LEFT, padx=(0, 10))

        # Edit Button
        ctk.CTkButton(
            button_frame,
            text="Edit",
            command=lambda: self.app.card_editor.edit_set(index),
            fg_color="#f39c12",
            hover_color="#d35400",
            width=80,
        ).pack(side=tk.LEFT, padx=(0, 10))

        # View Stats Button
        ctk.CTkButton(
            button_frame,
            text="Statistics",
            command=lambda: self.app.statistics.show_individual_statistics(index),
            fg_color="#2ecc71",
            hover_color="#27ae60",
            width=80,
        ).pack(side=tk.LEFT, padx=(0, 10))

        # Delete Button
        ctk.CTkButton(
            button_frame,
            text="Delete",
            command=lambda: self.confirm_delete_deck(index),
            fg_color="#e74c3c",
            hover_color="#c0392b",
            width=80,
        ).pack(side=tk.RIGHT)

    def confirm_delete_deck(self, index):
        """
        Show a confirmation dialog before deleting a deck.
        """
        self.app.message_box.show_confirmation(
            "Delete Deck",
            f"Are you sure you want to delete the deck '{self.app.flashcard_sets[index].title}'?",
            on_yes=lambda: self.delete_deck(index),
            on_no=self.show_deck_manager
        )

    def delete_deck(self, index):
        """
        Delete a deck from the list of decks.
        """
        del self.app.flashcard_sets[index]
        self.show_deck_manager()

    def start_learning_or_add_cards(self, set_index):
        """
        Start a learning session or show the "add cards -prompt" based on whether the deck has cards or not.
        """
        if not self.app.flashcard_sets[set_index].cards:
            self.app.message_box.show_message(
                "Empty Deck",
                "This deck has no cards. Would you like to add some cards?",
                on_ok=lambda: self.app.card_editor.show_add_cards_input(set_index)
            )
        else:
            self.app.learning_session.start_learning(set_index)

    def show_new_deck_input(self):
        """
        Show an input field for the user to create a new deck.
        """
        for widget in self.app.main_frame.winfo_children():
            widget.destroy()

        header_frame = ctk.CTkFrame(
            self.app.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text="Create New Deck",
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        # Frame to ask for the deck title
        input_frame = ctk.CTkFrame(self.app.main_frame, fg_color="white", corner_radius=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        ctk.CTkLabel(input_frame, text="Deck Title:", font=("Roboto", 16)).pack(
            anchor="w", padx=15, pady=(10, 5)
        )
        # Entry field for the deck title
        self.new_deck_title_entry = ctk.CTkEntry(input_frame, width=300)
        self.new_deck_title_entry.pack(pady=10)
        self.new_deck_title_entry.bind("<Return>", lambda event: self.create_new_set_from_input())

        # Create Deck Buttom
        create_button = ctk.CTkButton(
            input_frame,
            text="Create Deck",
            command=self.create_new_set_from_input,
            fg_color="#2ecc71",
            hover_color="#27ae60",
        )
        create_button.pack(pady=10)

        # Cancel Button
        cancel_button = ctk.CTkButton(
            input_frame,
            text="Cancel",
            command=self.show_deck_manager,
            fg_color="#95a5a6",
            hover_color="#7f8c8d",
        )
        cancel_button.pack(pady=10)

    def create_new_set_from_input(self):
        """
        Create a new deck based on the input from the user. Add the deck to the list of decks.
        """
        title = self.new_deck_title_entry.get()
        if title:
            new_set = FlashCardSet(title)
            self.app.flashcard_sets.append(new_set)
            self.app.current_set = new_set
            self.app.card_editor.show_add_cards_input()