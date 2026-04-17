from importlib import metadata
import tiktoken

print ("tiktoken Version: ", metadata.version("tiktoken"))

tokenizer = tiktoken.get_encoding("gpt2")

# Example text with special token and unknown words

# text = (
#     "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
#     "of someunknownPleace."
# )

# integer = tokenizer.encode(text, allowed_special={"<|endoftext|>"})

# print(integer)

# string = tokenizer.decode(integer)

# print(string)

with open("book/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

enc_text = tokenizer.encode(raw_text)
print(len(enc_text))

enc_sample = enc_text[50:] # Which just removes the first 50 tokens [50:]

context_size = 4 #length of the input context
#To context_size of 4 means that the model is trained to look at a sequence of 4 words (or tokens)
#to predict the next word in the sequence.
#The input x is the first 4 tokens [1,2,3,4], and the target y is the next 4 tokens [2,3,4,5]

x = enc_sample[:context_size]
y = enc_sample[1:context_size+1]

# print(f"X: {x}")
# print(f"Y:   {y}")

for i in range(1, context_size + 1):
    context = enc_sample[:i]
    desired = enc_sample[i]

    # print(context, " ---> ", desired)
    print( tokenizer.decode(context), " ---> ", tokenizer.decode([desired]) )
