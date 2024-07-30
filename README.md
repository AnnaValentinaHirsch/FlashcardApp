# Flashcard App

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

| Section               | Description                                                                                              |
|-----------------------|----------------------------------------------------------------------------------------------------------|
| **Main Screen**       | The main screen displays a list of all created decks. Each deck is represented by a card showing the deck title and number of cards. Options available on the main screen include:<br>- Create New Deck<br>- Export Decks<br>- Import Decks<br>- View Overall Statistics<br>- Access Help<br>- Exit Application |
| **Deck Creation and Editing** | **To create a new deck:**<br>1. Click "Create New Deck" on the main screen<br>2. Enter a title for the deck<br>3. Press Enter or click "Create Deck"<br><br>**To edit a deck:**<br>1. Click "Edit" on the deck card<br>2. Modify card contents, add new cards, or delete existing cards |
| **Card Creation and Editing** | **To add a new card:**<br>1. Enter the question in the "Question" field<br>2. Press Enter to move to the "Answer" field<br>3. Enter the answer<br>4. Press Enter or click "Add Card"<br><br>**To edit a card:**<br>1. In the deck editing view, select the card to edit<br>2. Modify the question or answer as needed<br>3. Save changes |
| **Study Session Interface** | The study session screen shows:<br>- Current card number and total cards<br>- Question field<br>- Answer input field<br>- "Check Answer" and "Show Answer" buttons<br>- Navigation buttons (Previous, Next, End Session) |
| **Statistics View**   | Statistics are displayed for individual decks and overall performance, showing:<br>- Total cards reviewed<br>- Correct answers<br>- Success rate |


## Key Components

| Component       | Description                                                      |
|-----------------|------------------------------------------------------------------|
| FlashcardGUI    | Initializes GUI, manages app flow                                |
| DeckManager     | Manages deck creation, editing, deletion                         |
| CardEditor      | Adds, edits, deletes cards                                       |
| LearningSession | Manages study sessions, answer checking, progress tracking       |
| Statistics      | Calculates and displays performance stats                        |
| FileOperations  | Handles JSON import/export                                       |

## Data Structure

### Flashcard

| Attribute      | Description            |
|----------------|------------------------|
| front          | Question               |
| back           | Answer                 |
| review_count   | Number of reviews      |
| correct_count  | Number of correct answers |

### FlashcardSet

| Attribute      | Description              |
|----------------|--------------------------|
| title          | Deck title               |
| cards          | List of Flashcard objects|


## File Management

- Deck data is saved in JSON format
- Each deck is saved as a separate JSON file in the application directory
- Import/export functions use JSON for data interchange

## Error Handling

- **Input Validation** for deck and card creation
- **Error Messages** for invalid actions (e.g., studying an empty deck)
- **Exception Handling** for file operations

## Future Enhancements

- Deploy web and mobile application versions
- Implement a check to prevent the user from uploading the same deck multiple times
- Implement multiple choice question support
- Implement cloud sync for deck sharing and statistics across devices
- Implement a spaced repetition algorithm for optimized learning (e.g., scheduling review intervals)
- Connect to a language model to allow for questions and answers that are not exact matches (e.g., fluent text)

## Known Issues

- The statistics are not saved after closing the UI.
- The UI is not responsive and may not display correctly on all screen sizes.

