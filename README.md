# 📄 genai-document-summarizer

A Streamlit app powered by OpenAI GPT models that summarizes long PDF documents into clean, human-readable insights.  
Upload any PDF and get section-wise summaries with customizable styles like bullet points, concise, or detailed output.

---

## 🚀 Live Demo

🌐 [Try it on Streamlit Cloud](https://genai-document-summarizer.streamlit.app/)  

---

## 🧠 Features

- ✅ Upload any PDF document
- ✂️ Intelligent text chunking with overlap
- 🧾 Summarizes each section separately using OpenAI GPT
- 📋 Style customization: Concise, Detailed, or Bullet Points
- 🧩 Expandable section-wise summaries in UI
- 📥 Download full summary as `.txt`
- 📈 Real-time progress bar while summarizing
- ❌ Robust error handling for failed chunks

---

## 🛠️ Tech Stack

| Tool        | Purpose                          |
|-------------|----------------------------------|
| [Streamlit](https://streamlit.io) | UI and deployment |
| [OpenAI GPT-3.5 / GPT-4](https://platform.openai.com/) | Summarization logic |
| [PyMuPDF](https://pymupdf.readthedocs.io/) | PDF text extraction |
| [tiktoken](https://github.com/openai/tiktoken) | Token-aware chunking |
| [Streamlit Secrets](https://docs.streamlit.io/library/advanced-features/secrets-management) | API key management |

---

## 🧾 Example Use Cases

- 📚 Academic paper summarization  
- 📄 Legal document overview  
- 📝 Contract/Policy simplification  
- 📊 Report breakdown for executives  
- 🧠 Reading support for long technical PDFs

---

