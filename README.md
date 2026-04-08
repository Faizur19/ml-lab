import math
from collections import Counter

# Sample documents
documents = [
    "data science is fun and data is powerful",
    "machine learning is part of data science",
    "python is great for data analysis and machine learning"
]

# Step 1: Clean and tokenize
def preprocess(doc):
    return doc.lower().split()

# Step 2: Get top 5 frequent words per document
top_words_per_doc = []
all_selected_words = set()

for doc in documents:
    words = preprocess(doc)
    freq = Counter(words)
    
    # Top 5 words
    top5 = [word for word, count in freq.most_common(5)]
    top_words_per_doc.append(top5)
    
    # Add to global set
    all_selected_words.update(top5)

# Convert to list (columns)
vocab = list(all_selected_words)

print("Selected Vocabulary:", vocab)

# Step 3: Create document-term matrix
matrix = []

for doc in documents:
    words = preprocess(doc)
    freq = Counter(words)
    
    row = []
    for word in vocab:
        row.append(freq[word])  # frequency in doc
    
    matrix.append(row)

print("\nDocument-Term Matrix:")
for row in matrix:
    print(row)

# Step 4: Cosine Similarity Function
def cosine_similarity(v1, v2):
    dot = sum(a*b for a, b in zip(v1, v2))
    
    mag1 = math.sqrt(sum(a*a for a in v1))
    mag2 = math.sqrt(sum(b*b for b in v2))
    
    if mag1 == 0 or mag2 == 0:
        return 0
    
    return dot / (mag1 * mag2)

# Step 5: Cosine Similarity Matrix
print("\nCosine Similarity Matrix:")

for i in range(len(matrix)):
    for j in range(len(matrix)):
        sim = cosine_similarity(matrix[i], matrix[j])
        print(f"{sim:.2f}", end=" ")
    print()

    


