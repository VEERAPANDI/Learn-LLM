with open("book/the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

print(f"Length of text: {len(raw_text)} characters")
print(raw_text[:99])