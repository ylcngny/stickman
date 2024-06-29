import re


class LipHandler:
    # Define phoneme to mouth position mapping
    phoneme_map = {
        'A': 'O', 'E': 'H', 'I': 'O', 'O': 'O', 'U': 'H',
        'B': 'C', 'M': 'C', 'P': 'C',
        'L': 'H', 'N': 'H', 'D': 'H', 'T': 'H',
        'S': 'H', 'Z': 'H', 'F': 'H', 'V': 'H',
        # Add more mappings as needed
    }
    def __init__(self):
        pass

    def getMap(self, text):
        # Convert text to uppercase and remove non-alphabetic characters
        text = re.sub(r'[^A-Z]', '', text.upper())

        # Map each character to a mouth position
        mouth_positions = [self.phoneme_map.get(char, 'C') for char in text]  # Default to 'C' if phoneme is not mapped
        return mouth_positions



