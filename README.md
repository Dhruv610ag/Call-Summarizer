# 📞 AI-Powered Call Summarization using RAG

## 📌 Overview

This repository contains an **end-to-end AI-based Call Summarization system** built using a **Retrieval-Augmented Generation (RAG)** pipeline. The system converts recorded customer calls into structured, accurate, and actionable summaries by combining **speech-to-text**, **vector-based retrieval**, **large language models**, and **sentiment analysis**.

The project is designed for real-world applications such as **customer support analytics, CRM automation, quality assurance, and executive reporting**.

---

## 🧠 Key Features

- 🎙️ Speech-to-text conversion from call recordings  
- 📄 Context-aware call summarization  
- 🧠 Retrieval-Augmented Generation (RAG)  
- 📦 Vector storage and semantic search using Pinecone  
- 😊 Customer sentiment analysis  
- 📋 Action item and risk identification  
- 🔒 Hallucination-controlled summaries  
- 🚀 Scalable and modular pipeline  

---

## 🏗️ System Architecture

┌──────────────────────────────┐
│        Audio Input            │
│        (.wav / .mp3)          │
└───────────────┬──────────────┘
                │
                ▼
┌──────────────────────────────┐
│     Speech-to-Text            │
│        (Whisper)              │
└───────────────┬──────────────┘
                │
                ▼
┌──────────────────────────────┐
│     Call Transcript           │
└───────────────┬──────────────┘
                │
                ▼
┌──────────────────────────────┐
│    Transcript Chunking        │
└───────────────┬──────────────┘
                │
                ▼
┌──────────────────────────────┐
│  Embedding Generation         │
│   (HuggingFace Models)        │
└───────────────┬──────────────┘
                │
                ▼
┌──────────────────────────────┐
│  Vector Database Storage      │
│        (Pinecone)             │
└───────────────┬──────────────┘
                │
                ▼
┌──────────────────────────────┐
│   Context Retrieval           │
│        (RAG)                  │
└───────────────┬──────────────┘
                │
                ▼
┌──────────────────────────────┐
│   LLM Processing              │
│   (Gemini / Groq)             │
└───────────────┬──────────────┘
                │
                ▼
┌──────────────────────────────┐
│  Structured Call Summary      │
│  + Sentiment Analysis         │
│  + Actionable Insights        │
└──────────────────────────────┘

---

## 🧩 Technology Stack

| Component | Technology |
|--------|------------|
| Speech-to-Text | OpenAI Whisper |
| LLMs | Gemini API, Groq API |
| Embeddings | HuggingFace Transformers |
| Vector Database | Pinecone |
| RAG | Custom / LangChain-compatible |
| Language | Python |

---

## 🔄 Workflow Explanation

1. **Audio Input**  
   Customer call recordings are provided in `.wav` or `.mp3` format.

2. **Speech Recognition**  
   Whisper converts audio into text transcripts.

3. **Transcript Chunking**  
   Long transcripts are split into semantically meaningful chunks.

4. **Vector Embedding**  
   HuggingFace models generate dense embeddings from transcript chunks.

5. **Vector Storage & Retrieval**  
   Embeddings are stored in Pinecone and retrieved based on semantic similarity.

6. **RAG-based Summarization**  
   Gemini or Groq LLM generates summaries using transcript + retrieved context.

7. **Sentiment Analysis**  
   Overall customer sentiment is inferred from conversation tone and language.

---

## 📑 Output Structure

The generated output includes:

- **Call Summary** – High-level overview of the conversation  
- **Participants & Roles** – Agent / Customer (if identifiable)  
- **Customer Intent** – Primary and secondary objectives  
- **Key Resolutions** – Issues resolved during the call  
- **Action Items** – Next steps with ownership and deadlines  
- **Risks / Escalations** – Compliance or dissatisfaction signals  
- **Sentiment Analysis** – Positive / Neutral / Negative  
- **Insights & Recommendations** – Business and process-level insights  

---

## 😊 Sentiment Analysis

The system performs **context-aware sentiment analysis** based on:
- Language tone and word choice  
- Expressions of satisfaction, frustration, or concern  
- Repeated complaints or positive affirmations  

Sentiment is classified as:
- **Positive**
- **Neutral**
- **Negative**

This helps organizations:
- Monitor customer satisfaction  
- Detect escalation risks early  
- Improve agent performance and service quality  

---

## 🔐 Hallucination Control

To ensure reliability and trustworthiness:
- The model uses **only the transcript and retrieved context**
- Missing or unclear information is explicitly stated
- No assumptions or fabricated details are generated

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/your-username/call-summarization-rag.git
cd call-summarization-rag
pip install -r requirements.txt
