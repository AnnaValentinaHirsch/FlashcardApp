import tkinter as tk
import customtkinter as ctk


class MessageBox:
    def __init__(self, app):
        self.app = app

    def show_message(self, title, message, type="info"): # TODO implement message types properly
        # Clear the main frame
        for widget in self.app.main_frame.winfo_children():
            widget.destroy()

       # Create the message box layout
        header_frame = ctk.CTkFrame(self.app.main_frame, fg_color="#3498db", corner_radius=0)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(header_frame, text=title, font=("Roboto", 24, "bold"), text_color="white").pack(pady=20)

        # Create the message frame
        message_frame = ctk.CTkFrame(self.app.main_frame, fg_color="white", corner_radius=10)
        message_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        ctk.CTkLabel(message_frame, text=message, font=("Roboto", 14), wraplength=300).pack(pady=20)

        # Create the OK button
        ok_button = ctk.CTkButton(
            message_frame,
            text="OK",
            command=self.app.deck_manager.show_deck_manager,
            fg_color="#3498db",
            hover_color="#2980b9",
        )
        ok_button.pack(pady=10)
        ok_button.focus_set()  # Set focus to the OK button
        ok_button.bind("<Return>", lambda event: ok_button.invoke())  # Bind Enter key to OK button

    def show_confirmation(self, title, message, on_yes, on_no):
        """
        Show a confirmation message box with Yes and No buttons. Used across modules to confirm actions.
        """
        for widget in self.app.main_frame.winfo_children():
            widget.destroy()

        header_frame = ctk.CTkFrame(self.app.main_frame, fg_color="#3498db", corner_radius=0)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        ctk.CTkLabel(header_frame, text=title, font=("Roboto", 24, "bold"), text_color="white").pack(pady=20)

        message_frame = ctk.CTkFrame(self.app.main_frame, fg_color="white", corner_radius=10)
        message_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        ctk.CTkLabel(message_frame, text=message, font=("Roboto", 14), wraplength=300).pack(pady=20)

        button_frame = ctk.CTkFrame(message_frame, fg_color="transparent")
        button_frame.pack(pady=10)

        yes_button = ctk.CTkButton(
            button_frame,
            text="Yes",
            command=on_yes,
            fg_color="#2ecc71",
            hover_color="#27ae60",
        )
        yes_button.pack(side=tk.LEFT, padx=10)
        yes_button.focus_set()  # Set focus to the Yes button
        yes_button.bind("<Return>", lambda event: yes_button.invoke())  # Bind Enter key to Yes button

        no_button = ctk.CTkButton(
            button_frame,
            text="No",
            command=on_no,
            fg_color="#e74c3c",
            hover_color="#c0392b",
        )
        no_button.pack(side=tk.LEFT, padx=10)
        no_button.bind("<Return>", lambda event: no_button.invoke())  # Bind Enter key to No button
