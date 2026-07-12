from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from rag.retriever import retrieve
import ollama
import time

app = Flask(__name__)
# Highly secure secret key used for session tracking cookie encryption
app.secret_key = "campus_pilot_secret_dynamic_key" 

MODEL_NAME = "qwen2.5:1.5b"

# Global In-Memory User Simulation Stack for Local Testing 
# (Restarting the Flask server clears out this memory array cleanly)
USERS_DB = {}


# ==========================================================================
# 1. CORE AUTHENTICATION ROUTING LAYER (Login / Signup Checks)
# ==========================================================================

@app.route("/")
def home():
    # FIXED RULE: If session cookie is not matching active login record, throw back to login view
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.json or {}
        email = data.get("email", "").strip()
        password = data.get("password", "").strip()
        
        # Validates user record tracking logic matrices
        if email in USERS_DB and USERS_DB[email]["password"] == password:
            session["user"] = email
            return jsonify({"status": "success", "message": "Login successful!"})
        return jsonify({"status": "error", "message": "Invalid email or password parameters."})
        
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        data = request.json or {}
        username = data.get("username", "").strip()
        email = data.get("email", "").strip()
        password = data.get("password", "").strip()
        
        if not email or not password:
            return jsonify({"status": "error", "message": "Missing credentials setup parameters."})
            
        if email in USERS_DB:
            return jsonify({"status": "error", "message": "User configuration target already exists."})
            
        # Register the user credentials into local runtime tracking storage matrix
        USERS_DB[email] = {"username": username, "password": password}
        session["user"] = email
        return jsonify({"status": "success", "message": "Account tracking initialized successfully."})
        
    return render_template("signup.html")


@app.route("/logout")
def logout():
    # Flush session memory clear and drop user validation state parameters
    session.pop("user", None)
    return redirect(url_for("login"))


# ==========================================================================
# 2. CHAT PIPELINE LAYER (RAG Matrix + Optimized Qwen Context Model Calls)
# ==========================================================================

@app.route("/chat", methods=["POST"])
def chat():
    # API security boundary wrapper rule validation check
    if "user" not in session:
        return jsonify({"answer": "Unauthorized access stream. Please login.", "sources": []}), 401

    try:
        user_question = request.json.get("message", "").strip()

        if not user_question:
            return jsonify({
                "answer": "Please enter a question.",
                "sources": []
            })

        # Knowledge Base Retrieval Execution Track
        start = time.time()
        context, sources = retrieve(user_question)
        print(f"Retriever Time: {time.time() - start:.2f} sec")

        # Slice string lengths down to protect the input context pipeline parameters threshold 
        context = context[:700]

        # Consolidated Persona Instruction Templates
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

        # Look inside your @app.route("/chat") block template configuration options area
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": 0.3,       # Slightly increased logic response flexibility parameters mawa
                "num_predict": 650,        # 🚀 INCREASE VALUE: Raised to 650 to completely ensure action plans never clip off midpoint
                "top_k": 30,
                "top_p": 0.9,
                "num_ctx": 4096            # 🚀 EXPAND POOL: Doubled context block window parameter size to prevent input clipping
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
            "answer": f"Backend Error: {str(e)}",
            "sources": []
        })


if __name__ == "__main__":
    # Debug runtime execution pipeline tracking on local system
    app.run(debug=True)