# help_screen.py
import customtkinter as ctk
import tkinter as tk

class HelpScreen:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame

    def show(self):
        """Explain how app works"""
        for widget in self.parent_frame.winfo_children():
            widget.destroy()

        # Header
        header_frame = ctk.CTkFrame(self.parent_frame, fg_color="#3498db", corner_radius=0)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(header_frame, text="Help", font=("Roboto", 24, "bold"), text_color="white").pack(pady=20)

        # Scrollable frame for help
        scroll_frame = ctk.CTkScrollableFrame(self.parent_frame, fg_color="#F0F0F0")
        scroll_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        # Help text
        help_text = self.load_help_text()

        ctk.CTkLabel(scroll_frame, text=help_text, justify="left", font=("Roboto", 14), wraplength=300).pack(pady=20, padx=20, anchor='w')

    def load_help_text(self):
        try:
            with open("help_text.txt", "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Help text file not found. Please ensure 'help_text.txt' is in the same directory as the application."