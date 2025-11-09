# 📘 Assignment: Hangman Game Challenge

---
slug: games-in-python
id: games-in-python
difficulty: Beginner
estimated_time: 45–75 minutes
prerequisites:
  - Python 3.8+
  - Basic syntax: variables, lists, conditionals, loops, functions
  - Familiarity with the random module (recommended)
due_date: 2025-10-10
attachments:
  - name: Starter Code
    file: starter-code.py
    type: python
---

Short description: Implement the classic "Hangman" game in Python — players guess a hidden word letter by letter until they either win or run out of attempts.

## 🎯 Objective
Learn to build an interactive console application in Python, handle user input, string processing, loops, and testable game logic.

## 🎓 Learning Goals
After completing this assignment, you should be able to:
- Implement game logic as modular, testable functions/classes.
- Use strings and collections to represent game progress and validate guesses.
- Handle invalid or repeated user inputs gracefully and determine win/loss conditions.

## ℹ️ Information
- Difficulty: Beginner  
- Estimated Time: 45–75 minutes  
- Prerequisites: Basic Python, pytest knowledge  
- Submission Format: Folder `assignments/games-in-python/` as described below  

## 📝 Tasks

### 🛠️ Task 1 — Implement Hangman Core
#### Description
Build the main game logic for “Hangman”: word selection, player guesses, progress display, and remaining attempts tracking.

#### Steps
1. Create or update folder `assignments/games-in-python/`
2. Implement main module `assignments/games-in-python/src/hangman.py` with:
   - `choose_word(word_list) -> str`
   - `mask_word(word, guesses) -> str`
   - `apply_guess(state, guess) -> (updated_state, correct: bool)`
   - `run_game()` — main game loop (can be in `src/main.py`)
3. Add tests in `assignments/games-in-python/tests/test_hangman.py`
4. Update this README with run instructions

#### Acceptance Criteria
- Random or deterministic word selection.
- Proper masked word display (e.g., `_ a _ _ m _ n`).
- Handles single-letter guesses; ignores invalid or repeated inputs with a message.
- Tracks remaining attempts and correctly determines win/lose.
- Unit tests cover all main cases (correct guess, wrong guess, repeat, edge cases).
- Code is readable and documented with docstrings.

#### Files to Modify / Create
- `assignments/games-in-python/README.md`
- `assignments/games-in-python/src/hangman.py`
- `assignments/games-in-python/src/main.py` (optional entry point)
- `assignments/games-in-python/tests/test_hangman.py`
- `assignments/games-in-python/assets/` (optional — e.g., for words list)

#### Tips
- Keep logic in small, testable functions.
- Use lowercase for input comparison.
- Use a deterministic seed for word choice in tests.

---

### 🛠️ Task 2 — Optional Extensions
#### Description
Add optional features to enhance the gameplay.

#### Steps
1. Support loading words from `assets/words.txt`
2. Add ASCII-art to visualize hangman progress
3. Add score tracking or multiplayer mode

#### Acceptance Criteria
- Extensions work without breaking base game logic.
- Extra features have their own tests.
- Updated README includes usage instructions.

#### Tips
- Use command-line flags to enable optional features.
- Test ASCII-art rendering and file parsing.

## ✅ Evaluation Criteria
- Functionality: 60%
- Code Quality & Style: 20%
- Documentation (README): 10%
- Tests/Coverage: 10%

## 💾 Run and Test Locally
Commands for Debian GNU/Linux 13 (devcontainer):

```bash
# Install dependencies
pip3 install -r requirements.txt

# Run the game
cd assignments/games-in-python
python3 src/main.py

# Run tests
pytest
