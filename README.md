<img width="1536" height="1024" alt="26e48543-9403-4a15-96ee-b2625b07d6ef" src="https://github.com/user-attachments/assets/8836915c-c20d-4766-aa26-1a042e14b292" />

# Simple 21: Blackjack :spades: :diamonds: :clubs: :hearts:

## Game Description

This project is a simple Blackjack game written in Python. The goal is to get a hand as close to 21 as possible without going over. The program uses a Hand class to keep track of cards, calculate the total value, and check things like busts or blackjack. There are also additional functions that help with basic game logic.

## File Descriptions

### hand.py  
This file contains the `Hand` class. It handles storing the cards, adding new cards, calculating the total value of a hand, checking if the hand is bust, and displaying the cards.

### main.py  
Runs the Blackjack game and controls the main gameplay loop using the `Hand` and `Deck` classes.

### check_bust.py  
This file contains a function that checks if a hand has gone over 21 by using the calculate_value method from the `Hand` class.

### deck.py
Contains the `Deck` class used to create, shuffle, and deal cards for the Blackjack game.

## Attribution Table

| Method/Function | Primary Author | Technique Claimed |
|---|---|---|
| `main()` | Kerwin/William | 11. Composition of two custom classes |
| `Hand.__init__()` | Kerwin | N/A |
| `Hand.add_card()` | Kerwin | N/A |
| `Hand.calculate_value()` | Kerwin | 6. Sequence unpacking |
| `Hand.is_bust()` | Kerwin | N/A |
| `Hand.display_hand()` | Kerwin | 3. F-strings containing expressions |
| `Hand.has_blackjack()` | William | N/A |
| `Deck.__init__()` | William | N/A |
| `Deck.shuffle()` | William | N/A |
| `Deck.deal_card()` | William | N/A |
| `check_bust()` | Devante | 1. Conditional expressions, 2. Optional parameters and/or keyword arguments |

## Annotated Bibliography

### Bicycle Cards – How to Play Blackjack (https://bicyclecards.com/how-to-play/blackjack/)  
Used to understand the basic rules of Blackjack and how the game works.

### Python Documentation (https://docs.python.org/3/)  
Used as a reference for Python syntax and how functions and classes work.

### W3Schools Python Tutorial (https://www.w3schools.com/python/)  
Used to review basic Python concepts like loops, conditionals, and functions.

### GitHub Docs (https://docs.github.com/en)  
Used to understand how to upload files, make commits, and manage the repository.
