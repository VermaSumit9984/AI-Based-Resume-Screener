from sentence_transformers import SentenceTransformer, util

# Pretrained AI model for semantic embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_resumes(job_description, resumes):
    """Rank resumes by semantic similarity to job description."""
    jd_embedding = model.encode(job_description, convert_to_tensor=True)
    results = []

    for filename, text in resumes:
        if not text.strip():
            continue
        res_embedding = model.encode(text, convert_to_tensor=True)
        similarity = util.cos_sim(jd_embedding, res_embedding).item()
        results.append((filename, round(similarity * 100, 2)))

    results.sort(key=lambda x: x[1], reverse=True)
    return results[:10]
