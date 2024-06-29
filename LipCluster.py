from nltk.corpus import cmudict


class PhonemeClusterer:
    def __init__(self):
        self.phoneme_to_cluster = {}
        self.num_clusters = 3

        # Initialize clusters based on lip positions
        self.assign_clusters()

    def assign_clusters(self):
        # Get all phonemes from CMU Pronouncing Dictionary
        dictionary = cmudict.dict()
        all_phonemes = set()
        for word, pronunciations in dictionary.items():
            all_phonemes.update(pronunciations[0])

        all_phonemes = list(all_phonemes)

        # Assign clusters based on lip positions
        for i, phoneme in enumerate(all_phonemes):
            if phoneme.startswith(('AA', 'AE', 'AH', 'AO', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'UH', 'UW')):
                self.phoneme_to_cluster[phoneme] = 'O'  # Open lip position
            elif phoneme.startswith(('B', 'D', 'G', 'JH', 'L', 'M', 'N', 'NG', 'R', 'V', 'W', 'Y', 'Z')):
                self.phoneme_to_cluster[phoneme] = 'C'  # Closed lip position
            else:
                self.phoneme_to_cluster[phoneme] = 'H'  # Half-open lip position

    def get_cluster(self, phoneme):
        if phoneme in self.phoneme_to_cluster:
            return self.phoneme_to_cluster[phoneme]
        else:
            return None


# # Example usage:
# clusterer = PhonemeClusterer()
#
# # Get cluster for a specific phoneme
# phoneme = "DH"
# cluster = clusterer.get_cluster(phoneme)
# print(f"Cluster for phoneme '{phoneme}' is '{cluster}'")
