# RAG Demo with ChromaDB

This project demonstrates a simple RAG (Retrieval-Augmented Generation) workflow using ChromaDB and Sentence Transformers.

## Features

- Create vector embeddings
- Store embeddings in ChromaDB
- Perform semantic similarity search
- Retrieve relevant documents

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Demo

```bash
python app.py
```

## Example Query

```python
query = "How many work from home days are allowed?"
```

## Expected Output

```text
Query:
How many work from home days are allowed?

Retrieved Documents:
- Employees can work from home two days per week.
- Annual leave policy allows 24 paid leave days per year.
```

## Tech Stack

- Python
- ChromaDB
- Sentence Transformers
