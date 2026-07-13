# 🎓 CampusPilot AI

CampusPilot AI is an AI-powered college companion that helps students with study planning, placements, interview preparation, resume building, budget management, internships, scholarships, hostel life, laptop troubleshooting, and other college-related queries.

It uses Retrieval-Augmented Generation (RAG) with Ollama to provide accurate and domain-specific responses from a custom knowledge base.

---

# 🚀 Features

- User Login & Signup
- AI Chatbot Interface
- Study Planning
- Placement Preparation
- Interview Tips
- Resume Guidance
- Budget Management
- Hostel Life Tips
- Laptop Troubleshooting
- Internship Guidance
- Scholarship Information
- Mental Wellbeing Support
- Coding Roadmaps
- Dark & Light Theme
- Chat History
- RAG-based Knowledge Retrieval
- Local AI using Ollama

---

# 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Flask
- Python

### AI & RAG
- Ollama (Qwen2.5:1.5B)
- Sentence Transformers
- FAISS
- NumPy

---

# 📂 Project Structure

```
CampusPilot-AI/
│
├── app.py
├── requirements.txt
│
├── knowledge_base/
│   ├── study_planning.txt
│   ├── placements.txt
│   ├── resume.txt
│   ├── internships.txt
│   ├── scholarships.txt
│   └── ...
│
├── rag/
│   ├── create_index.py
│   ├── retriever.py
│   ├── faiss_index.bin
│   └── documents.pkl
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

# ⚙️ How It Works

1. User opens the application.
2. User logs in to the system.
3. The chatbot interface is displayed.
4. The user asks a college-related question.
5. The question is converted into embeddings using Sentence Transformers.
6. FAISS searches the knowledge base for relevant information.
7. The retrieved context is sent to Ollama (Qwen2.5).
8. The AI model generates a clear and relevant response.
9. The chatbot displays the answer to the user.

---

# 🧠 Why I Chose RAG

I used the Retrieval-Augmented Generation (RAG) approach because it allows the chatbot to use a custom knowledge base without retraining the AI model. Whenever new information is added, I only need to update the knowledge base and rebuild the FAISS index.

---

# Tradeoff

The chatbot provides high-quality responses only when relevant information exists in the knowledge base. If the required information is missing, the chatbot may generate a more general response.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Vimala17/Campuspilot-Ai.git
```

Go to the project folder:

```bash
cd Campuspilot-Ai
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Ollama and download the model:

```bash
ollama pull qwen2.5:1.5b
```

Create the FAISS index:

```bash
python rag/create_index.py
```

Run the application:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

# 📚 Knowledge Base

The chatbot uses a custom knowledge base containing information about:

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
- College Life Tips

---

# 📸 Demo

The chatbot can answer questions like:

- How can I prepare for placements?
- I missed a class. What should I do?
- Help me manage ₹500 for this week.
- Give me resume tips.
- How can I prepare for coding interviews?
- My laptop is slow before a coding contest.

---

# 🔮 Future Enhancements

- Voice Assistant
- PDF Upload Support
- Web Scraping for Automatic Knowledge Base Updates
- Multi-language Support
- Student Dashboard
- Attendance Tracker
- Personalized Recommendations

---

# 👩‍💻 Author

**Vanaparthi Vimala**

B.Tech CSE (Artificial Intelligence)

KIET Women

GitHub:
https://github.com/Vimala17
Youtube demo:
https://youtu.be/WQgLkpMKK9E?si=i4__2qPFSFoU9AAS

---
