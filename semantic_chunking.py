from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_chunk(sentences, threshold=0.8,min_sentences=20):
    embeddings = model.encode(sentences, normalize_embeddings=True)
    
    chunks = []
    current_chunk = [sentences[0]]
    current_embs = [embeddings[0]]

    for i in range(1, len(sentences)):
        sim = cosine_similarity(
            [embeddings[i - 1]],
            [embeddings[i]]
        )[0][0]

        if sim < threshold and len(current_chunk) >= min_sentences:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentences[i]]
            current_embs = [embeddings[i]]
        else:
            current_chunk.append(sentences[i])
            current_embs.append(embeddings[i])

    chunks.append(" ".join(current_chunk))
    return chunks


def merge_small_chunks(chunks, min_tokens, tokenizer):
    merged = []
    buffer = ""

    for chunk in chunks:
        if len(tokenizer.encode(buffer)) < min_tokens:
            buffer += " " + chunk
        else:
            merged.append(buffer.strip())
            buffer = chunk

    if buffer:
        merged.append(buffer.strip())

    return merged