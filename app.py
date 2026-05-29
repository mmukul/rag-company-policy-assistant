# Fix SQLite version issue for ChromaDB
__import__('pysqlite3')
import sys

sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# Import libraries
import chromadb
from sentence_transformers import SentenceTransformer

# Initialize ChromaDB client
client = chromadb.Client()

# Create collection
collection = client.create_collection(
    name="company_policy"
)

# Sample documents
documents = [
    "Employees can work from home two days per week.",
    "Annual leave policy allows 24 paid leave days per year.",
    "Laptop reimbursement limit is 50000 rupees.",
    "Employees must complete security awareness training every quarter."
]

# Load embedding model
model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

# Generate embeddings
embeddings = model.encode(documents)

# Store documents in ChromaDB
collection.add(
    documents=documents,
    embeddings=embeddings.tolist(),
    ids=["doc1", "doc2", "doc3", "doc4"]
)

# User query
query = "How many work from home days are allowed?"

# Convert query into embedding
query_embedding = model.encode([query])

# Retrieve similar documents
results = collection.query(
    query_embeddings=query_embedding.tolist(),
    n_results=2
)

# Print results
print("\nQuery:")
print(query)

print("\nRetrieved Documents:")

for doc in results['documents'][0]:
    print("-", doc)
