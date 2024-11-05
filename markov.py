import random
import re

# Sample Bee Movie lines as the corpus
text = """
According to all known laws of aviation, there is no way a bee should be able to fly.
Its wings are too small to get its fat little body off the ground.
The bee, of course, flies anyway because bees don't care what humans think is impossible.
Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little.
Barry, breakfast is ready! Hang on a second. Hello? - Barry? - Adam?
Can you believe this is happening? I cant. I'll pick you up.
Looking sharp. Use the stairs. Your father paid good money for those.
Sorry, I'm excited. Here's the graduate. We're very proud of you, son.
A perfect report card, all B's.
"""

# Initialize the transitions dictionary
transitions = {}

# Tokenize text, separating words and punctuation as distinct tokens
tokens = re.findall(r"\w+|[.,!?;]", text.lower())  # Keeps words and punctuation as separate tokens

# Build the Markov Chain with punctuation-aware transitions
for i in range(len(tokens) - 1):
    current_word = tokens[i]
    next_word = tokens[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)

# Function to capitalize the first word after a period or at the start
def capitalize_text(tokens):
    result = []
    capitalize_next = True  # To capitalize the first word

    for token in tokens:
        if capitalize_next and token.isalpha():
            result.append(token.capitalize())
            capitalize_next = False
        else:
            result.append(token)
        
        if token in ".!?":  # Capitalize the next word after these tokens
            capitalize_next = True

    return result

# Generate text using the Markov Chain with enhanced formatting
def generate_text(start_word, num_words):
    current_word = start_word.lower()
    result = [current_word]
    
    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            break
    
    # Capitalize and format the result
    result = capitalize_text(result)
    formatted_text = " ".join(result)
    
    # Fix spacing around punctuation
    formatted_text = re.sub(r" ([.,!?;])", r"\1", formatted_text)  # Remove space before punctuation
    return formatted_text

# Prompt user for input instead of command-line arguments
start_word = input("Enter a starting word: ").strip()
num_words = int(input("Enter the number of words to generate: ").strip())

# Generate and print the result
print(generate_text(start_word, num_words))
