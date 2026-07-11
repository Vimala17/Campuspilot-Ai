# 🎓 CampusPilot AI

CampusPilot AI is an AI-powered student assistant designed to help college students with academics, placements, career guidance, productivity, budgeting, and everyday college life.

It combines **Retrieval-Augmented Generation (RAG)** with a local Large Language Model (LLM) running on **Ollama (Qwen 2.5)** to provide accurate, context-aware, and domain-specific responses.

---

# 🚀 Features

- Study Planning
- Placement Preparation
- Interview Checklists
- Resume Guidance
- Budget Management
- Hostel Life Tips
- Laptop Troubleshooting
- Time Management
- Internship Guidance
- Scholarship Information
- Mental Wellbeing Support
- Coding Roadmaps
- Chat History
- Dark / Light Theme
- RAG-based Knowledge Retrieval
- Local AI using Ollama

---

# 🏗️ Tech Stack

## Frontend

- HTML
- CSS
- JavaScript

## Backend

- Flask
- Python

## AI

- Ollama
- Qwen2.5:1.5B
- Sentence Transformers
- FAISS

---

# 📂 Project Structure

```
CampusPilot-AI
│
├── app.py
├── requirements.txt
│
├── knowledge_base/
│     study_planning.txt
│     placements.txt
│     resume.txt
│     internships.txt
│     ...
│
├── rag/
│     create_index.py
│     retriever.py
│     faiss_index.bin
│     documents.pkl
│
├── templates/
│     index.html
│
├── static/
│     style.css
│     script.js
│
└── README.md
```

---

# ⚙️ How It Works

1. The user asks a question.

2. The question is converted into embeddings using Sentence Transformers.

3. FAISS searches the knowledge base and retrieves the most relevant content.

4. The retrieved information is added to the prompt.

5. Ollama (Qwen2.5) generates the final answer.

```
User Question
      │
      ▼
Sentence Transformer
      │
      ▼
FAISS Retrieval
      │
      ▼
Relevant Knowledge
      │
      ▼
Ollama (Qwen2.5)
      │
      ▼
Final Response
```

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/Vimala17/Campuspilot-Ai.git
```

Go into the project

```bash
cd Campuspilot-Ai
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Download Ollama

https://ollama.com

Pull the model

```bash
ollama pull qwen2.5:1.5b
```

Create the FAISS index

```bash
python rag/create_index.py
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 📚 Knowledge Base

The chatbot uses a structured knowledge base containing information on:

- Study Planning
- Placement Preparation
- Resume Building
- Interview Preparation
- Budget Management
- Hostel Life
- Productivity
- Time Management
- Coding Roadmaps
- Scholarships
- Internships
- Laptop Troubleshooting
- Mental Wellbeing

The knowledge base can be expanded by adding more `.txt` files and rebuilding the FAISS index.

---

# Why I Built This

College students often search for information across multiple websites and videos. CampusPilot AI brings useful academic and career guidance together in one assistant, making it easier to get quick, relevant answers.

---

# Design Tradeoff

I chose a **RAG-based approach** instead of fine-tuning a language model.

### Why?

- Faster to build and update
- Easy to add new knowledge by editing text files
- Lower hardware requirements
- Runs completely offline using Ollama
- Better control over domain-specific information

### Tradeoff

The quality of responses depends on the knowledge base. If the required information is missing from the knowledge base, the chatbot may provide only general guidance instead of detailed domain-specific answers.

---

# 🔮 Future Improvements

- Voice Assistant
- PDF Upload Support
- Student Dashboard
- Attendance Calculator
- CGPA Predictor
- Budget Tracker
- AI Study Planner
- Export Chat as PDF
- Multi-language Support
- Personalized Recommendations

---

# Author

**Vanaparthi Vimala**

B.Tech CSE (AI)

KIET Women

GitHub

https://github.com/Vimala17

---

