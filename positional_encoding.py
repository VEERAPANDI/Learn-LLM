import torch
from dataset_dataloader import create_dataloader_v1

vacab_size = 50257  # GPT-2 vocabulary size
output_dim = 256  # Embedding dimension
max_length = 4

with open("book/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

token_embedding_layer = torch.nn.Embedding(vacab_size, output_dim)
# print(token_embedding_layer)
dataloader = create_dataloader_v1(
    raw_text,
    batch_size=8,
    max_length=max_length,
    stride=max_length,
    shuffle=False
)
data_iter = iter(dataloader)
inputs, targets = next(data_iter)

# print("Token IDs:\n", inputs)
# print("\nInput shape:", inputs.shape)

token_embedding = token_embedding_layer(inputs)
# print("Token embeddings:\n", token_embedding)
# print("\nToken embedding shape:", token_embedding.shape)  # Should be (batch_size, max_length, output_dim)

context_length = max_length
pos_embedding_layer = torch.nn.Embedding(context_length, output_dim)
pos_embedding = pos_embedding_layer(torch.arange(max_length))
# print("Positional embeddings:\n", pos_embedding)
print("\nPositional embedding shape:", pos_embedding.shape)

input_embeddings = token_embedding + pos_embedding
# print("Input embeddings:\n", input_embeddings)
print("\nInput embedding shape:", input_embeddings.shape)  # Should be (batch_size, max_length, output_dim)