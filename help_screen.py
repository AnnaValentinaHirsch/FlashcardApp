import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkfont
import re

class SimpleMarkdownText(tk.Frame):
    """
    A Tkinter Frame that renders a simple Markdown text.

    Attributes:
        markdown_text (str): The markdown text to be rendered.

    Methods:
        create_widgets(): Parses the markdown text and creates corresponding widgets.
        create_heading(line): Creates a heading widget for a given markdown heading line.
        create_bullet_point(line): Creates a bullet point widget for a given markdown bullet point line.
        create_bold_text(line): Creates a text widget with bold formatting for given markdown bold text.
        create_italic_text(line): Creates a text widget with italic formatting for given markdown italic text.
        create_normal_text(line): Creates a normal text widget for a given line of text.
    """
    def __init__(self, parent, markdown_text, *args, **kwargs):
        """
        Initializes the SimpleMarkdownText frame.

        Args:
            parent (tk.Widget): The parent widget.
            markdown_text (str): The markdown text to render.
            *args: Additional positional arguments for the Tkinter Frame.
            **kwargs: Additional keyword arguments for the Tkinter Frame.
        """
        super().__init__(parent, *args, **kwargs)
        self.markdown_text = markdown_text
        self.create_widgets()
        self.configure(bg="#F0F0F0")  # Set background color

    def create_widgets(self):
        """
        Parses the markdown text and creates corresponding widgets for each line.
        """
        lines = self.markdown_text.split('\n')
        for line in lines:
            if line.startswith('#'):
                self.create_heading(line)
            elif line.startswith('* '):
                self.create_bullet_point(line)
            elif re.match(r'\*\*(.*?)\*\*', line):
                self.create_bold_text(line)
            elif re.match(r'\*(.*?)\*', line):
                self.create_italic_text(line)
            else:
                self.create_normal_text(line)

    def create_heading(self, line):
        """
        Creates a heading widget for a given markdown heading line.

        Args:
            line (str): The markdown heading line.
        """
        level = len(line.split(' ')[0])
        text = ' '.join(line.split(' ')[1:])
        font_size = 20 - (level - 1) * 2
        label = tk.Label(self, text=text, font=('Roboto', font_size, 'bold'), anchor='w', bg="#F0F0F0", fg="#45494E", wraplength=350, justify=tk.LEFT)
        label.pack(fill='x', pady=(10, 0))

    def create_bullet_point(self, line):
        """
        Creates a bullet point widget for a given markdown bullet point line.

        Args:
            line (str): The markdown bullet point line.
        """
        text = line[2:]
        label = tk.Label(self, text='• ' + text, font=('Roboto', 12), anchor='w', bg="#F0F0F0", fg="#45494E", wraplength=350, justify=tk.LEFT)
        label.pack(fill='x')

    def create_bold_text(self, line):
        """
        Creates a text widget with bold formatting for given markdown bold text.

        Args:
            line (str): The markdown bold text line.
        """
        parts = re.split(r'(\*\*.*?\*\*)', line)
        frame = tk.Frame(self, bg="#F0F0F0")
        frame.pack(fill='x')
        for part in parts:
            if part.startswith('**') and part.endswith('**'):
                part = part[2:-2]
                label = tk.Label(frame, text=part, font=('Roboto', 12, 'bold'), bg="#F0F0F0", fg="#45494E", wraplength=350, justify=tk.LEFT, anchor='w')
                label.pack(side='left')
            else:
                label = tk.Label(frame, text=part, font=('Roboto', 12), bg="#F0F0F0", fg="#45494E", wraplength=350, justify=tk.LEFT, anchor='w')
                label.pack(side='left')

    def create_italic_text(self, line):
        """
        Creates a text widget with italic formatting for given markdown italic text.

        Args:
            line (str): The markdown italic text line.
        """
        parts = re.split(r'(\*.*?\*)', line)
        frame = tk.Frame(self, bg="#F0F0F0")
        frame.pack(fill='x')
        for part in parts:
            if part.startswith('*') and part.endswith('*'):
                part = part[1:-1]
                label = tk.Label(frame, text=part, font=('Roboto', 12, 'italic'), bg="#F0F0F0", fg="#45494E", wraplength=350, justify=tk.LEFT, anchor='w')
                label.pack(side='left')
            else:
                label = tk.Label(frame, text=part, font=('Roboto', 12), bg="#F0F0F0", fg="#45494E", wraplength=350, justify=tk.LEFT, anchor='w')
                label.pack(side='left')

    def create_normal_text(self, line):
        """
        Creates a normal text widget for a given line of text.

        Args:
            line (str): The line of text.
        """
        label = tk.Label(self, text=line, font=('Roboto', 12), anchor='w', bg="#F0F0F0", fg="#45494E", wraplength=350, justify=tk.LEFT)
        label.pack(fill='x')

class HelpScreen:
    """
    A class to represent the Help screen of the application.

    Attributes:
        parent_frame (tk.Frame): The parent frame in which the help screen is displayed.

    Methods:
        set_default_font(): Sets the default font to Roboto if available.
        show(): Displays the help screen with instructions on how the app works.
        load_help_text(): Loads the help text from a file.
    """
    def __init__(self, parent_frame):
        """
        Initializes the HelpScreen with the given parent frame.

        Args:
            parent_frame (tk.Frame): The parent frame in which the help screen is displayed.
        """
        self.parent_frame = parent_frame

        # Set the default font to Roboto if available
        self.set_default_font()

    def set_default_font(self):
        """
        Sets the default font to Roboto if it is available on the system 
        to make the text look nice.
        If Roboto is not available, it falls back to the default font.
        """
        try:
            tkfont.Font(family="Roboto", size=12)
            tkfont.nametofont("TkDefaultFont").configure(family="Roboto", size=12)
        except tk.TclError:
            print("Roboto font is not available. Using default font.")

    def show(self):
        """
        Displays the help screen, explaining how the application works.
        It clears any existing widgets in the parent frame and creates a new help screen layout.
        """
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
        markdown_widget = SimpleMarkdownText(scroll_frame, help_text, bg="#F0F0F0")
        markdown_widget.pack(fill='both', expand=True)

    def load_help_text(self):
        """
        Loads the help text from a file named 'help_text.txt'.

        Returns:
            str: The content of the help text file. If the file is not found, returns an error message.
        """
        try:
            with open("help_text.txt", "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Help text file not found. Please ensure 'help_text.txt' is in the same directory as the application."