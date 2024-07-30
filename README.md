# Flashcard App - Description

Run `main.py` to test the app with the interface.

## System Requirements

- Python 3.8 or higher
- Required libraries:
  - `tkinter` (usually comes pre-installed with Python)
  - `customtkinter` (install via pip: `pip install customtkinter`)

## Main Features

| Feature          | Options                                                                                 |
|------------------|-----------------------------------------------------------------------------------------|
| **Deck Management** | - Create new decks with custom titles <br> - Edit existing decks (rename, modify cards) <br> - Delete decks with confirmation prompt <br> - View deck-specific statistics  |
| **Card Management** | - Add new cards with questions and answers <br> - Edit existing cards <br> - Delete individual cards  |
| **Study Session**   | - Interactive learning with randomized card order <br> - Check answer or reveal correct answer <br> - Track progress within session <br> - End session early or continue until all cards are reviewed  |
| **Statistics**      | - View individual deck statistics <br> - Total score <br> - Success rate  |
| **Import/Export**   | - Export decks to JSON format <br> - Import decks from JSON files  |


## User Interface

### Deck Creation and Editing

| Action                    | Steps                                                                                                                   |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **Create new deck:**      | 1. Click "Create New Deck" on the main screen<br>2. Enter a title for the deck<br>3. Press Enter or click "Create Deck" |
| **Edit deck:**   | 1. Click "Edit" on the "your decks" menu<br>2. Modify card contents, add new cards, or delete existing cards            |
| **Delete deck:** | 1. Click "Delete" on the "your decks" menu<br>2. Confirm Deletion.                                                      |


### Card Creation and Editing

| Action                 | Steps                                                                 |
|------------------------|-----------------------------------------------------------------------|
| **Add card:**   | 1. Enter the question in the "Question" field<br>2. Press Enter to move to the "Answer" field<br>3. Enter the answer<br>4. Press Enter or click "Add Card" |
| **Edit card:** | 1. In the deck editing view, select the card to edit<br>2. Modify the question or answer as needed<br>3. Save changes |


### Study Session Interface

The study session screen shows:

- Current card number and total cards
- Question field
- Answer input field
- "Check Answer" and "Show Answer" buttons
- Navigation buttons (Previous, Next, End Session)

### Statistics View

Statistics are displayed for individual decks and overall performance, showing:

- Total cards reviewed
- Correct answers
- Success rate

## File Management

- Deck data is saved in JSON format
- Each deck is saved as a separate JSON file in the application directory
- Import/export functions use JSON for data interchange

## Error Handling

- **Input Validation** for deck and card creation
- **Error Messages** for invalid actions (e.g., studying an empty deck)
- **Exception Handling** for file operations

## Known Issues

- The statistics are not saved after closing the UI.
- The UI is not responsive and may not display correctly on all screen sizes.

