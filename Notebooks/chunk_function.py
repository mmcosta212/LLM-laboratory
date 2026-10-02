# Chunk function
def chunk_text(text: str, chunk_size: int = 4):
    """Divide the text in chunks."""
    for i in range(0, len(text), chunk_size):
        yield text[i:i + chunk_size]


s = chunk_text(text="Today is a beautiful sunny day!", chunk_size = 4)

# Testing
for piece in s:
    print(repr(piece))