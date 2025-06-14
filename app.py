import streamlit as st
from utils import extract_text_from_pdf
from summarizer import chunk_text_with_overlap, summarize_chunks

st.set_page_config(page_title="📄 Document Summarizer", layout="centered")
st.title("📄 ChatGPT-Powered Document Summarizer")

api_key = st.secrets["OPENAI_API_KEY"]

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        full_text = extract_text_from_pdf(uploaded_file)

    st.text_area("Extracted Text (Preview)", full_text[:2000] + "...", height=200)

    style = st.selectbox("Choose summary style", ["Concise", "Detailed", "Bullet Points"])

    if st.button("Summarize Document"):
        with st.spinner("Splitting into chunks..."):
            chunks = chunk_text_with_overlap(full_text)

        st.success(f"📄 PDF split into {len(chunks)} sections.")

        with st.spinner("Summarizing each section..."):
            summaries = []
            progress = st.progress(0)

            for i, summary in enumerate(summarize_chunks(chunks, api_key, style=style)):
                summaries.append(f"### Section {i+1} Summary\n{summary}\n")
                progress.progress((i + 1) / len(chunks))

        full_summary = "\n\n".join(summaries)

        st.subheader("🧠 Final Summary (Expandable Sections)")
        for i, summary in enumerate(summaries):
            with st.expander(f"Section {i+1}"):
                st.markdown(summary)

        st.download_button("📥 Download Summary", full_summary, file_name="summary.txt")
