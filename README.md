# Wordle-Guesser

Wordle Guesser
Wordle Guesser is a command-line Python tool designed to assist players in solving Wordle puzzles through a brute-force approach. It filters a provided wordlist—either a list of real 5-letter words or all possible 5-letter letter combinations—based on user guesses and their corresponding Wordle feedback. The tool accurately simulates Wordle’s rules, including handling duplicate letters, to identify all possible words that match the given constraints. Results are displayed in the terminal and optionally saved to a file for further analysis.


# Features

- Flexible Wordlist Support: Works with any 5-letter wordlist, whether it contains real words (e.g., house, smile) or exhaustive combinations (e.g., aaaaa to zzzzz).
- Accurate Wordle Simulation: Implements Wordle’s feedback logic for green (g), yellow (y), and gray (b) results, correctly handling duplicate letters.
- Comma-Separated Guess Input: Accepts multiple guesses in a single --guess argument, formatted as word:result (e.g., coder:bybyy,round:yybbb).
- Output Options:
	- Displays up to 50 candidate words in the terminal to avoid clutter.
	- Saves all candidates to variants.txt (one word per line) by default.
	- Includes a -nw/--no-write flag to skip writing to the file.


# Installation

## Prerequisites

Python 3.6 or higher
The click library for command-line interface support

## Steps

1. Clone the Repository:
```bash
git clone https://github.com/ashura2/wordle_guesser.git
cd wordle_guesser
```

2. Install Dependencies:Install the required click library using pip:
```bash
pip install click
```

3. Prepare a Wordlist:
Use a file containing 5-letter words (e.g., sgb-words-5-letters.txt for real English words or you can use your custon wordlists, including for all possible 5-letter combinations).



# Usage

Run the tool using the ==python3 wordle_brute.py== command with the required options.

## Command Syntax

```bash
python3 wordle_brute.py -w WORDLIST --guess GUESSES [-nw]
```

## Options

- -w, --wordlist PATH: Path to the wordlist file (required). Can be real words or combinations.
- --guess TEXT: Comma-separated list of guesses and their Wordle results, formatted as word:result (required). Each word and result must be 5 characters; result uses g (green), y (yellow), b (gray/black).
- -nw, --no-write: Flag to prevent writing results to variants.txt (optional).
- -h, --help: Show the help message and exit.

## Examples

1. **Filter Words with a Real-Words Wordlist**:Using a wordlist of real English words (sgb-words-5-letters.txt) and two guesses:
```bash
python3 wordle_guesser.py -w sgb-words-5-letters.txt --guess crane:bybyy,round:ygbyb
```


2. **Filter Without Writing to File**: Using the -nw flag to skip writing to variants.txt:
```bash
python3 wordle_brute.py -w sgb-words-5-letters.txt --guess crane:bybyy,round:ygbyb -nw
```


# How It Works

## Input Processing:

Reads a wordlist from the specified file, filtering for 5-letter words.
Parses guesses in the format word:result (e.g., crane:bybyy), splitting them by commas.
Validates that each word and result is 5 characters and that results contain only g, y, or b.


## Wordle Logic:

Simulates Wordle’s feedback mechanism:
Green (g): Letter is correct and in the correct position.
Yellow (y): Letter is in the word but in a different position.
Gray/Black (b): Letter is not in the word.

