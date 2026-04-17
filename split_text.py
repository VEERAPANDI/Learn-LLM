import re;
from simple_tokenizer_v1 import SimpleTokenizer

text = "In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available."

with open("book/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

result = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
result = [segment for segment in result if segment.strip() != '']
# print(result[:30])
# print(f"Total segments: {len(result)}")

all_words = sorted(list(set(result)))
all_words.extend(["<|endoftext|>", "<|unk|>"])
vocabulary_size = len(all_words)
print(f"Vocabulary size: {vocabulary_size} unique segments")

vocab = {token:integer for integer, token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    # print(item)
    if i>=50:
        break




tokenizer = SimpleTokenizer(vocab)
encoded = tokenizer.encode(raw_text)
print(encoded)
decoded = tokenizer.decode(encoded)
print(decoded)