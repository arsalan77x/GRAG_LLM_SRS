import os
import openai
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
openai.api_key = OPENAI_API_KEY

EMBEDDING_MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'
LLM_MODEL = 'gpt-4o'
TOP_K = 5



def build_index(docs, embedding_model):
  
    texts = [d["text"] for d in docs]
    doc_embeddings = embedding_model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
    dimension = doc_embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)  
    index.add(doc_embeddings)
    id_map = {i: docs[i] for i in range(len(docs))}
    
    return index, id_map




def retrieve(query, k=TOP_K):
    q_emb = embedding_model.encode([query], convert_to_numpy=True, normalize_embeddings=True)
    scores, indices = index.search(q_emb, k)
    results = [id_map[i] for i in indices[0]]
    return results


def generate_answer(query, retrieved_docs):

    context_str = "\n\n".join([f"{doc['id']}: {doc['text']}" for doc in retrieved_docs])
    system_prompt = (
        "You are a helpful assistant. "
        "You have access to the following documents:\n\n"
        f"{context_str}\n\n"
        "Use these documents as context to answer the user's query. "
        "If the documents do not contain relevant information, say that you don't know."
    )
    
    response = openai.ChatCompletion.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ],
        temperature=0.2
    )
    return response.choices[0].message['content'].strip()


if __name__ == "__main__":
    #document = ""
    embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    index, id_map = build_index(documents, embedding_model)
    user_query = "What is RAG and how does it differ from graph-based retrieval methods?"
    retrieved = retrieve(user_query)
    answer = generate_answer(user_query, retrieved)
    print("User Query:", user_query)
    print("Retrieved Docs:", [doc["id"] for doc in retrieved])
    print("Answer:\n", answer)
