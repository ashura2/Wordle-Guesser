import click

def get_feedback(guess, target):
    """
    Simulates Wordle feedback for a guess against a target word.
    Returns a string with 'g' (green), 'y' (yellow), 'b' (gray/black).
    """
    feedback = ['b'] * 5
    target_count = {}
    for c in target:
        target_count[c] = target_count.get(c, 0) + 1
    
    # First, check green letters
    for i in range(5):
        if guess[i] == target[i]:
            feedback[i] = 'g'
            target_count[guess[i]] -= 1
    
    # Then, check yellow letters
    for i in range(5):
        if feedback[i] == 'b' and guess[i] in target_count and target_count[guess[i]] > 0:
            feedback[i] = 'y'
            target_count[guess[i]] -= 1
    
    return ''.join(feedback)

def filter_words(words, guesses_results):
    """
    Filters words, checking if they match all previous guesses and results.
    """
    candidates = []
    for word in words:
        valid = True
        for guess, result in guesses_results:
            if get_feedback(guess, word) != result:
                valid = False
                break
        if valid:
            candidates.append(word)
    
    return candidates

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-w', '--wordlist', required=True, type=click.Path(exists=True), help='Path to the wordlist file (combinations or real words)')
@click.option('--guess', required=True, help='Previous guesses and results, comma-separated, format: word:result, e.g., coder:bybyy,round:yybbb')
@click.option('-nw', '--no-write', is_flag=True, help='Do not write results to variants.txt')
def main(wordlist, guess, no_write):
    # Read the wordlist
    with open(wordlist) as f:
        words = [w.strip().lower() for w in f if len(w.strip()) == 5]
    
    # Check if the wordlist is empty
    if not words:
        print("Error: The wordlist is empty or contains no 5-letter words.")
        return
    
    # Process guesses
    guesses_results = []
    guess_list = guess.split(',')
    for g in guess_list:
        parts = g.strip().split(':')
        if len(parts) != 2:
            print(f"Error: Invalid format for guess '{g}'. Use word:result (e.g., coder:bybyy).")
            return
        gw, res = parts
        if len(gw) != 5 or len(res) != 5 or not all(c in 'gyb' for c in res):
            print(f"Error: Word '{gw}' or result '{res}' must be 5 characters, and result must contain only g, y, b.")
            return
        guesses_results.append((gw.lower(), res.lower()))
    
    # Filter words
    candidates = filter_words(words, guesses_results)
    
    # Write results to variants.txt unless --no-write is specified
    if not no_write:
        with open('variants.txt', 'w') as f:
            for candidate in candidates:
                f.write(f"{candidate}\n")
    
    # Output results to terminal
    if candidates:
        print(f"Possible words ({len(candidates)}):")
        print(candidates[:50])  # Limit output to first 50 words
        if len(candidates) > 50:
            print(f"...and {len(candidates) - 50} more words")
        if not no_write:
            print("Results written to variants.txt")
    else:
        print("No words match the conditions. Check guesses or wordlist.")
        if not no_write:
            print("File variants.txt created, but it is empty.")

if __name__ == '__main__':
    main()
