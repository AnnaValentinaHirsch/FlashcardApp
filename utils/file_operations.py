import json
from tkinter import filedialog
from cards.flashcard_set import FlashCardSet

class FileOperations:
    def __init__(self, app):
        self.app = app

    def export_flashcard_sets(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
        )
        if file_path:
            data = [flashcard_set.to_dict() for flashcard_set in self.app.flashcard_sets]
            with open(file_path, "w") as file:
                json.dump(data, file)
            self.app.message_box.show_message(
                "Export Successful", f"Flashcard sets have been exported to {file_path}"
            )

    def import_flashcard_sets(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
        )
        if file_path:
            try:
                with open(file_path, "r") as file:
                    data = json.load(file)
                imported_sets = [FlashCardSet.from_dict(set_data) for set_data in data]
                self.app.flashcard_sets.extend(imported_sets)
                self.app.deck_manager.show_deck_manager()
            except json.JSONDecodeError:
                self.app.message_box.show_message("Import Error", "The selected file is not a valid JSON file.")
            except KeyError as e:
                self.app.message_box.show_message("Import Error", f"The JSON file is missing required data: {str(e)}")
            except Exception as e:
                self.app.message_box.show_message("Import Error", f"An error occurred while importing: {str(e)}")