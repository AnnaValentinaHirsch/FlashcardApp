import tkinter as tk
import customtkinter as ctk


class Statistics:
    def __init__(self, app):
        self.app = app

    def show_statistics(self):
        """
        Show the overall statistics of the flashcard sets. This includes the total score and success rate of all the flashcard sets combined.
        """
        for widget in self.app.main_frame.winfo_children():
            widget.destroy()

        header_frame = ctk.CTkFrame(
            self.app.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text="Overall Statistics",
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        stats_frame = ctk.CTkFrame(self.app.main_frame, fg_color="white", corner_radius=10)
        stats_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        total_correct = sum(
            card.correct_count for deck in self.app.flashcard_sets for card in deck.cards
        )
        total_reviews = sum(
            card.review_count for deck in self.app.flashcard_sets for card in deck.cards
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

        for deck in self.app.flashcard_sets:
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

        back_button = ctk.CTkButton(
            self.app.main_frame,
            text="Back to Decks",
            command=self.app.deck_manager.show_deck_manager,
            fg_color="#95a5a6",
            hover_color="#7f8c8d",
            height=50,
            corner_radius=10,
        )
        back_button.pack(padx=20, pady=(0, 20), fill=tk.X, side=tk.BOTTOM)

    def show_individual_statistics(self, set_index):
        """
        Show the statistics of a specific flashcard set. Includes the total score and success rate of the flashcard set.
        """
        self.app.current_set = self.app.flashcard_sets[set_index]
        for widget in self.app.main_frame.winfo_children():
            widget.destroy()

        header_frame = ctk.CTkFrame(
            self.app.main_frame, fg_color="#3498db", corner_radius=0
        )
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(
            header_frame,
            text=f"Statistics: {self.app.current_set.title}",
            font=("Roboto", 24, "bold"),
            text_color="white",
        ).pack(pady=20)

        stats_frame = ctk.CTkFrame(self.app.main_frame, fg_color="white", corner_radius=10)
        stats_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        total_score = self.app.current_set.total_score()
        success_rate = self.app.current_set.success_rate()

        ctk.CTkLabel(
            stats_frame, text=f"Total Score: {total_score}", font=("Roboto", 18)
        ).pack(pady=10)
        ctk.CTkLabel(
            stats_frame, text=f"Success Rate: {success_rate:.2f}%", font=("Roboto", 18)
        ).pack(pady=10)

        stats_scroll_frame = ctk.CTkScrollableFrame(stats_frame, fg_color="white")
        stats_scroll_frame.pack(fill=tk.BOTH, expand=True)

        for i, card in enumerate(self.app.current_set.cards):
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

        back_button = ctk.CTkButton(
            self.app.main_frame,
            text="Back to Decks",
            command=self.app.deck_manager.show_deck_manager,
            fg_color="#95a5a6",
            hover_color="#7f8c8d",
            height=50,
            corner_radius=10,
        )
        back_button.pack(padx=20, pady=(0, 20), fill=tk.X, side=tk.BOTTOM)
