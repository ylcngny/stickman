import os
import nltk
from nltk.corpus import cmudict

# Ensure NLTK data path is set correctly
nltk.data.path.append(os.path.join(os.getcwd(), "nltk_data"))

# Download necessary NLTK data if not already downloaded
nltk.download('cmudict', download_dir=os.path.join(os.getcwd(), "nltk_data"))
nltk.download('punkt', download_dir=os.path.join(os.getcwd(), "nltk_data"))

# Load CMU Pronouncing Dictionary
pronouncing_dict = cmudict.dict()


class PhonemeClusterer:
    def __init__(self):
        self.phoneme_to_cluster = {}
        self.num_clusters = 3

        # Initialize clusters based on basic lip positions
        self.assign_clusters()

    def assign_clusters(self):
        # Define basic lip positions based on common phonetic features
        lip_positions = {
            'O': ['AA', 'AE', 'AH', 'AO', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'UH', 'UW'],
            'C': ['B', 'D', 'G', 'JH', 'L', 'M', 'N', 'NG', 'R', 'V', 'W', 'Y', 'Z'],
            'H': []  # Initialize empty for half-open, will be filled below
        }

        # Assign half-open lip position to remaining phonemes not explicitly listed
        all_phonemes = set().union(*lip_positions.values())
        for phoneme in all_phonemes:
            assigned = False
            for position, phoneme_list in lip_positions.items():
                if phoneme in phoneme_list:
                    self.phoneme_to_cluster[phoneme] = position
                    assigned = True
                    break
            if not assigned:
                self.phoneme_to_cluster[phoneme] = 'H'  # Default to half-open

    def get_cluster(self, phoneme):
        if phoneme in self.phoneme_to_cluster:
            return self.phoneme_to_cluster[phoneme]
        else:
            return None


class LipPositionExtractor:
    def __init__(self):
        self.phoneme_clusterer = PhonemeClusterer()

    def extract_words(self, text):
        return nltk.word_tokenize(text)

    def extract_phonemes(self, word):
        word = word.lower()
        if word in pronouncing_dict:
            # Strip stress numbers from phonemes (e.g., EH1 -> EH)
            return [phoneme.rstrip('012') for phoneme in pronouncing_dict[word][0]]
        else:
            return None  # Return None if word not found

    def extract_lip_positions(self, sentence):
        words = self.extract_words(sentence)
        lip_positions = []

        for word in words:
            phonemes = self.extract_phonemes(word)
            if phonemes:
                print(f"Word: {word} => Phonemes: {' '.join(phonemes)}")
            else:
                print(f"Word: {word} => No phonemes found")

            for phoneme in phonemes:
                pos = self.phoneme_clusterer.get_cluster(phoneme)
                if pos:
                    lip_positions.append(pos)

        return lip_positions


# # Example usage:
# if __name__ == "__main__":
#     sentence = "Lets review the code and see if there are any improvements or adjustments that can be made"
#     lip_positions = LipPositionExtractor().extract_lip_positions(sentence)
#     print("Lip Positions:", lip_positions)
