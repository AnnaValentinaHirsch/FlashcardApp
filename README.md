# Flashcard App

run main.py to test app with interface


# App Functionalities in Detail 

## 2. System Requirements
- Python 3.8 or higher
- Required libraries: 
  - tkinter (usually comes pre-installed with Python)
  - customtkinter (install via pip: `pip install customtkinter`)
- 
## 4. Main Features
### 4.1 Deck Management
- Create new decks with custom titles
- Edit existing decks, including renaming and modifying cards
- Delete decks with confirmation prompt
- View deck-specific statistics

### 4.2 Card Management
- Add new cards to decks with questions and answers
- Edit existing cards within a deck
- Delete individual cards from a deck

### 4.3 Study Session
- Interactive learning mode with randomised card order
- Option to check answer or reveal the correct answer
- Progress tracking within each study session
- Ability to end session early or continue until all cards are reviewed

### 4.4 Statistics
- Individual deck statistics showing total score and success rate

### 4.5 Import/Export
- Export decks to JSON format for backup or sharing
- Import decks from JSON files

## 5. User Interface
### 5.1 Main Screen
The main screen displays a list of all created decks. Each deck is represented by a card showing the deck title and number of cards. Options available on the main screen include:
- Create New Deck
- Export Decks
- Import Decks
- View Overall Statistics
- Access Help
- Exit Application

### 5.2 Deck Creation and Editing
To create a new deck:
1. Click "Create New Deck" on the main screen
2. Enter a title for the deck
3. Press Enter or click "Create Deck"

To edit a deck:
1. Click "Edit" on the deck card
2. Modify card contents, add new cards, or delete existing cards

### 5.3 Card Creation and Editing
To add a new card:
1. Enter the question in the "Question" field
2. Press Enter to move to the "Answer" field
3. Enter the answer
4. Press Enter or click "Add Card"

To edit a card:
1. In the deck editing view, select the card to edit
2. Modify the question or answer as needed
3. Save changes

### 5.4 Study Session Interface
The study session screen shows:
- Current card number and total cards
- Question field
- Answer input field
- "Check Answer" and "Show Answer" buttons
- Navigation buttons (Previous, Next, End Session)

### 5.5 Statistics View
Statistics are displayed for individual decks and overall performance, showing:
- Total cards reviewed
- Correct answers
- Success rate

## 6. Key Components
### 6.1 FlashcardGUI
The main application class that initialises the GUI and manages the overall application flow.

### 6.2 DeckManager
Handles creation, editing, and deletion of decks. Manages the display of decks on the main screen.

### 6.3 CardEditor
Provides functionality for adding, editing, and deleting cards within a deck.

### 6.4 LearningSession
Manages the study session, including card display, answer checking, and session progress tracking.

### 6.5 Statistics
Calculates and displays statistics for individual decks and overall performance.

### 6.6 FileOperations
Handles importing and exporting of deck data in JSON format.

## 7. Data Structure
### 7.1 Flashcard
Represents a single flashcard with attributes:
- front (question)
- back (answer)
- review_count
- correct_count

### 7.2 FlashcardSet
Represents a deck of flashcards with attributes:
- title
- cards (list of Flashcard objects)

## 8. File Management
- Deck data is saved in JSON format
- Each deck is saved as a separate JSON file in the application directory
- Import/export functions use JSON for data interchange

## 9. Error Handling
- Input validation for deck and card creation
- Error messages for invalid actions (e.g., studying an empty deck)
- Exception handling for file operations

## 10. Future Enhancements

- Deploy web and mobile application version
- Implement check to prevent user from uploading the same deck multiple times
- Implement multiple choice question support
- Implement cloud sync for deck sharing and statistics across devices 
- Implement spaced repetition algorithm for optimised learning (e.g., scheduling review intervals)
- Connect to a language model to allow for questions and answers that are not exact matches (e.g. fluent text)

## 11. Known Issues

- The statistics are not saved after closing the UI.
- The UI is not responsive and may not display correctly on all screen sizes.
