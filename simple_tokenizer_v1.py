import re;


class SimpleTokenizer:
    def __init__(self, vocab):
        self.str_into_int = vocab
        self.int_into_str = {i:s for s,i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)

        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_into_int[s] for s in preprocessed]
        return ids
    
    def decode(self, ids):
        text = " ".join([self.int_into_str[i] for i in ids])
        # Remove space before the spefic punctuation marks
        text = re.sub(r'\s([,.:;?_!"()\'])', r'\1', text)
        return text