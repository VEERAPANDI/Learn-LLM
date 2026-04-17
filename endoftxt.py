import simple_tokenizer_v2 as SimpleTokenizerV2



text1 = "This is a test sentence with unknownword."
text2 = "This is another test sentence with unknownword."

text = "<|endoftext|>".join([text1, text2])
tokenizer = SimpleTokenizerV2.SimpleTokenizerV2(text)
encoded = tokenizer.encode(text)
print(encoded)
decoded = tokenizer.decode(encoded)
print(decoded)