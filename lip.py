import re

# Define phoneme to mouth position mapping
phoneme_map = {
    'A': 'O', 'E': 'H', 'I': 'O', 'O': 'O', 'U': 'H',
    'B': 'C', 'M': 'C', 'P': 'C',
    'L': 'H', 'N': 'H', 'D': 'H', 'T': 'H',
    'S': 'H', 'Z': 'H', 'F': 'H', 'V': 'H',
    # Add more mappings as needed
}


# Function to map text to mouth positions
def text_to_mouth_positions(text):
    # Convert text to uppercase and remove non-alphabetic characters
    text = re.sub(r'[^A-Z]', '', text.upper())

    # Map each character to a mouth position
    mouth_positions = [phoneme_map.get(char, 'C') for char in text]  # Default to 'C' if phoneme is not mapped
    return mouth_positions


def extract_phonemes(text):
    return re.findall(r'[A-Za-z]+', text.upper())


# Example usage
text = "Let's review the code and see if there are any improvements or adjustments that can be made."
mouth_positions = text_to_mouth_positions(text)
print(text, "\n", extract_phonemes(text), "\n", mouth_positions)
