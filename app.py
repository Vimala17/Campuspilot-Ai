from flask import Flask, render_template, request, jsonify
from rag.retriever import retrieve
import ollama
import time

app = Flask(__name__)

MODEL_NAME = "qwen2.5:1.5b"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_question = request.json.get("message", "").strip()

        if not user_question:
            return jsonify({
                "answer": "Please enter a question.",
                "sources": []
            })

        start = time.time()
        context, sources = retrieve(user_question)
        print(f"Retriever Time: {time.time() - start:.2f} sec")

        context = context[:700]

        prompt = f"""
You are CampusPilot AI.

You are a practical college life assistant for students.

Help students with:
- Study planning
- Budget management
- Placement preparation
- Resume tips
- Interview checklist
- Hostel life
- Laptop troubleshooting
- Time management
- Productivity
- Scholarships
- Internship guidance

Rules:
- Use the retrieved knowledge first.
- If needed, use your own general student-life knowledge.
- Keep the answer concise, actionable, and under 200 words.
- Give simple, actionable steps.
- If the question is unrelated to college/student life, politely say you only help with student-life guidance.

Knowledge:
{context}

Question:
{user_question}

Answer format:
✅ Problem:
💡 Solution:
🚀 Action Plan:
"""

        start = time.time()

        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": 0.1,
                "num_predict": 350,  # FIXED: Increased from 120 to 350 so generation completes fully
                "top_k": 20,
                "top_p": 0.8,
                "num_ctx": 2048     # Increased context window to ensure full prompt intake
            }
        )

        print(f"LLM Time: {time.time() - start:.2f} sec")

        answer = response["message"]["content"].strip()

        return jsonify({
            "answer": answer,
            "sources": sources
        })

    except Exception as e:
        print("ERROR:", e)

        return jsonify({
            "answer": str(e),
            "sources": []
        })


if __name__ == "__main__":
    app.run(debug=True)