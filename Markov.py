import random
import re

# Sample Bee Movie lines as the corpus
text = """
All thoughtful men must feel the gravest alarm over the growth of lynching in this country, and especially over the peculiarly hideous forms so often taken by mob violence when colored men are the victims—on which occasions the mob seems to lay most weight, not on the crime, but on the color of the criminal. In a certain proportion of these cases the man lynched has been guilty of a crime horrible beyond description; a crime so horrible that as far as he himself is concerned he has forfeited the right to any kind of sympathy whatsoever. The feeling of all good citizens that such a hideous crime shall not be hideously punished by mob violence is due not in the least to sympathy for the criminal, but to a very lively sense of the train of dreadful consequences which follows the course taken by the mob in exacting inhuman vengeance for an inhuman wrong. In such cases, moreover, it is well to remember that the criminal not merely sins against humanity in inexpiable and unpardonable fashion, but sins particularly against his own race, and does them a[525] wrong far greater than any white man can possibly do them. Therefore, in such cases the colored people throughout the land should in every possible way show their belief that they, more than all others in the community, are horrified at the commission of such a crime and are peculiarly concerned in taking every possible measure to prevent its recurrence and to bring the criminal to immediate justice. The slightest lack of vigor either in denunciation of the crime or in bringing the criminal to justice is itself unpardonable.
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
