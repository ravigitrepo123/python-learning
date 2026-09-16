

"""
    yield : Keyword that turns a function into a generator: 
    each yield produces a value and pauses the function, 
    preserving local state.
    example 
    def gen():
    yield "first"
    print("Processing after first yield")
    yield "second"
    print("Processing after second yield")

# as there are 2 yields,iteration is twice. 
# in each iteration, the code will run until the next yield is reached in a function
for v in gen():
    print(v)

o/p
first
Processing after first yield
second
Processing after second yield    

The enumerate object yields pairs containing a count (from start, which
defaults to zero) and a value yielded by the iterable argument.
for i, v in enumerate(["a","b"], start=1):
    print(i, v)
IN above i is the count starts it 1 and v is the value yielded by the iterable argument.    

"""
def read_large_file(file_path, chunk_size=100):
    """Streams a large file line-by-line and yields chunks of lines."""
    with open(file_path, 'r', encoding='utf-8') as file:
        chunk = []
        for line in file:
            chunk.append(line)
            if len(chunk) == chunk_size:
                yield chunk
                chunk = []  # Reset the chunk buffer
        
        # Yield any remaining lines if file length isn't perfectly divisible by chunk_size
        if chunk:
            yield chunk

# Processing the file chunk by chunk
file_path = 'd:/large_dataset.txt'

for chunk_index, chunk in enumerate(read_large_file(file_path, chunk_size=100), start=1):
    # chunk_index starts with 1 and increments with each chunk
    #chunk is a list of lines read from the file, with a maximum length of chunk_size 100 here
    
    # Process the chunk of lines (e.g., parse, clean, or aggregate data)
    print(f"Processing Chunk #{chunk_index} with {len(chunk)} lines")
    # Example memory-efficient processing (per-chunk summary):
    # - Strip and skip empty lines
    # - Count words in the chunk
    # - Detect lines containing a keyword (case-insensitive)
    keyword = 'error'  # change as needed
    chunk_word_count = 0
    chunk_keyword_count = 0

    for line in chunk:
        clean = line.strip()
        if not clean:
            continue

        # simple word count for the cleaned line
        chunk_word_count += len(clean.split())

        # detect keyword occurrences
        if keyword in clean.lower():
            chunk_keyword_count += 1

    print(f"  Chunk summary: words={chunk_word_count}, '{keyword}' occurrences={chunk_keyword_count}")

# If you want an overall summary across all chunks, aggregate counters outside the loop.
"""
o/p : .txt contains 250 lines, chunk_size=100, so we have 3 chunks:
error occurrences are counted in each chunk, and the word count is also calculated for each chunk. The output will look like this:
Processing Chunk #1 with 100 lines
  Chunk summary: words=202, 'error' occurrences=2
Processing Chunk #2 with 100 lines
  Chunk summary: words=200, 'error' occurrences=0
Processing Chunk #3 with 50 lines
  Chunk summary: words=101, 'error' occurrences=1
"""
