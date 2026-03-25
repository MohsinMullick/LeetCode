class Solution(object):
    def toGoatLatin(self, sentence):
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        result = []
        for i, word in enumerate(words):
            # vowel check
            if word[0] in vowels:
                new_word = word + "ma"
            else:
                new_word = word[1:] + word[0] + "ma"
            # add 'a' based on position
            new_word += "a" * (i + 1)
            result.append(new_word)
        return " ".join(result)