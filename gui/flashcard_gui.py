import tkinter as tk
import customtkinter as ctk

from .deck_manager import DeckManager
from .card_editor import CardEditor
from .learning_session import LearningSession
from .statistics import Statistics
from utils.file_operations import FileOperations
from utils.help_screen import HelpScreen
from utils.message_box import MessageBox


class FlashcardGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")
        self.root.geometry("600x800")
        self.root.minsize(600, 800)
        self.message_box = MessageBox(self)
        self.help_screen = HelpScreen(self)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.flashcard_sets = []
        self.current_set = None

        self.init_ui()

    def init_ui(self):
        self.create_main_frame()
        self.deck_manager = DeckManager(self)
        self.card_editor = CardEditor(self)
        self.learning_session = LearningSession(self)
        self.statistics = Statistics(self)
        self.file_operations = FileOperations(self)
        self.help_screen = HelpScreen(self)
        self.deck_manager.show_deck_manager()

    def create_main_frame(self):
        """
        Create the main frame of the application.
        """
        self.main_frame = ctk.CTkFrame(self.root, fg_color="#F0F0F0")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

    def on_closing(self):
        """
        Callback triggered when the user tries to close the application.
        """
        self.message_box.show_confirmation(
            "Quit",
            "Do you want to quit?",
            on_yes=self.root.destroy,
            on_no=self.deck_manager.show_deck_manager
        )

    def _on_mousewheel(self, event):
        """
        Allow scrolling with the mouse wheel.
        """
        widget = event.widget
        while widget.master and not isinstance(widget, ctk.CTkScrollableFrame):
            widget = widget.master
        if isinstance(widget, ctk.CTkScrollableFrame):
            widget._parent_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def bind_mousewheel(self, widget):
        """
        Bind the mousewheel to the widget.
        """
        widget.bind("<MouseWheel>", self._on_mousewheel, "+") # + means that this binding will be called before the default binding
        widget.bind("<Button-4>", self._on_mousewheel, "+")
        widget.bind("<Button-5>", self._on_mousewheel, "+")
        for child in widget.winfo_children():
            self.bind_mousewheel(child)

    def show_help_screen(self):
        """
        Show the help screen.
        """
        self.help_screen.show()
