import torch

from dataset_dataloader import create_dataloader_v1

print("Torch version:", torch.__version__)
with open("book/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

dataloader = create_dataloader_v1(
    raw_text, 
    batch_size=8, 
    max_length=4, 
    stride=4, 
    shuffle=False
)

data_iter = iter(dataloader)
inputs, targets = next(data_iter)
print("Inputs:\n", inputs)
print("\nTargets:\n", targets)

# first_batch = next(data_iter)
# print(first_batch)
# second_batch = next(data_iter)
# print("Second batch: ")
# print(second_batch)