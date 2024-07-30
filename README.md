# Flashcard App

Run `main.py` to test the app with the interface.

## System Requirements

- Python 3.8 or higher
- Required libraries:
  - `tkinter` (usually comes pre-installed with Python)
  - `customtkinter` (install via pip: `pip install customtkinter`)

## Main Features

### Deck Management

- Create new decks with custom titles
- Edit existing decks, including renaming and modifying cards
- Delete decks with a confirmation prompt
- View deck-specific statistics

### Card Management

- Add new cards to decks with questions and answers
- Edit existing cards within a deck
- Delete individual cards from a deck

### Study Session

- Interactive learning mode with randomized card order
- Option to check the answer or reveal the correct answer
- Progress tracking within each study session
- Ability to end the session early or continue until all cards are reviewed

### Statistics

- Individual deck statistics showing total score and success rate

### Import/Export

- Export decks to JSON format for backup or sharing
- Import decks from JSON files

## User Interface

### Main Screen

The main screen displays a list of all created decks. Each deck is represented by a card showing the deck title and number of cards. Options available on the main screen include:

- Create New Deck
- Export Decks
- Import Decks
- View Overall Statistics
- Access Help
- Exit Application

### Deck Creation and Editing

To create a new deck:

1. Click "Create New Deck" on the main screen
2. Enter a title for the deck
3. Press Enter or click "Create Deck"

To edit a deck:

1. Click "Edit" on the deck card
2. Modify card contents, add new cards, or delete existing cards

### Card Creation and Editing

To add a new card:

1. Enter the question in the "Question" field
2. Press Enter to move to the "Answer" field
3. Enter the answer
4. Press Enter or click "Add Card"

To edit a card:

1. In the deck editing view, select the card to edit
2. Modify the question or answer as needed
3. Save changes

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

