import sys
import time

def typewriter_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        for _ in range(10000):  # Adjust the delay
            pass

def progress_bar(percent, spinner):
    bar_length = 20
    num_hashes = int(percent / 100 * bar_length)
    progress = '\033[94m\033[1m[' + '=' * num_hashes + '>' + '.' * (bar_length - num_hashes) + ']\033[0m'
    return progress + ' ' + '\033[94m\033[1m[' + str(percent) + '%]\033[0m ' + spinner

# Define a list of spinning characters
spinners = ['-', '\\', '|', '/']
spinner_index = 0

# Example usage:
for i in range(101):
    # Get the next spinner character
    spinner = spinners[spinner_index]
    # Update the spinner index
    spinner_index = (spinner_index + 1) % len(spinners)

    sys.stdout.write('\r' + progress_bar(i, spinner) + '  ')
    sys.stdout.flush()

    # Simulate a delay
    for _ in range(100000):
        pass

typewriter_effect('\nProgress complete!\n')

