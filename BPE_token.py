import tiktoken

# Intialize encodfing for GPT-2, GPT-3 and GPT-4
encodings ={
    "gpt2": tiktoken.get_encoding("gpt2"),
    "gpt3": tiktoken.get_encoding("p50k_base"),
    "gpt4": tiktoken.get_encoding("cl100k_base"),
}

vocab_sizes = { model: encoding.n_vocab for model, encoding in encodings.items() }

for model, size in vocab_sizes.items():
    print(f"Vocabulary size for {model.upper()}: {size} tokens")