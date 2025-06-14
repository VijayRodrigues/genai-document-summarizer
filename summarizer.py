import tiktoken
from openai import OpenAI

def chunk_text_with_overlap(text, max_tokens=1500, overlap=200):
    tokenizer = tiktoken.get_encoding("cl100k_base")
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + max_tokens
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += max_tokens - overlap
    
    return chunks

def summarize_chunks(chunks, api_key, style="Concise", model="gpt-3.5-turbo"):
    client = OpenAI(api_key=api_key)
    all_summaries = []

    for i, chunk in enumerate(chunks):
        prompt = f"Summarize the following document section in a {style.lower()} style:\n\n{chunk}"
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
            )
            summary = response.choices[0].message.content
        except Exception as e:
            summary = f"❌ Error in Section {i+1}: {str(e)}"
        
        all_summaries.append(summary)

    return all_summaries
