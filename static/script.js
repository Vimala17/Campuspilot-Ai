document.addEventListener("DOMContentLoaded", () => {
    const sendBtn = document.getElementById("sendBtn");
    const questionInput = document.getElementById("question");
    const chatBox = document.getElementById("chatBox");
    const themeToggle = document.getElementById("themeToggle");
    const newChatBtn = document.getElementById("newChat");
    const historyList = document.getElementById("historyList");
    const historySearch = document.getElementById("historySearch");
    const suggestions = document.querySelectorAll(".suggestion");

    // Refresh resilience matrix configurations
    let currentSessionId = Date.now(); 
    let allSessionsMemory = JSON.parse(localStorage.getItem("allSessionsMemory")) || {}; 
    let sessionTitles = JSON.parse(localStorage.getItem("sessionTitles")) || {};     
    
    // Race-condition guard flag (Double execution complete block avvadaniki)
    let isRequestPending = false;

    const defaultWelcomeHTML = `
    <div class="bot-message">
        <div class="avatar">🤖</div>
        <div class="message welcome-card">
            <div class="welcome-header-clean">
                <h3>Welcome to CampusPilot AI 👋</h3>
            </div>
        </div>
    </div>
`;

    function saveToLocalStorage() {
        localStorage.setItem("allSessionsMemory", JSON.stringify(allSessionsMemory));
        localStorage.setItem("sessionTitles", JSON.stringify(sessionTitles));
    }

    function appendMessage(text, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add(sender === "user" ? "user-message" : "bot-message");

        // Simple raw linebreak processing matching Qwen model syntax
        const formattedText = text.replace(/\n/g, '<br>');

        messageDiv.innerHTML = `
            <div class="avatar">${sender === 'user' ? '👤' : '🤖'}</div>
            <div class="message"><p>${formattedText}</p></div>
        `;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;

        if (!allSessionsMemory[currentSessionId]) {
            allSessionsMemory[currentSessionId] = [];
        }
        allSessionsMemory[currentSessionId].push({ sender, text });
        saveToLocalStorage();
    }

    function renderHistory() {
        historyList.innerHTML = "";
        const query = historySearch.value.toLowerCase();

        Object.keys(sessionTitles).forEach(sessionId => {
            const titleText = sessionTitles[sessionId];
            if (!titleText.toLowerCase().includes(query)) return;

            const row = document.createElement("div");
            row.className = "history-item";
            if (Number(sessionId) === currentSessionId) row.classList.add("active-session");

            // Change inside your renderHistory() filtered loop row format setup:
row.innerHTML = `
    <div class="history-clickable">
        <i class="fa-regular fa-comment"></i>
        <span>${titleText}</span>
    </div>
    <button class="history-delete-btn" title="Delete Chat">
        <i class="fa-regular fa-trash-can"></i>
    </button>
`;

            row.querySelector(".history-clickable").addEventListener("click", () => {
                if (isRequestPending) return; // Blocker protection during stream fetching
                
                currentSessionId = Number(sessionId);
                chatBox.innerHTML = "";
                
                const historicStream = allSessionsMemory[currentSessionId] || [];
                historicStream.forEach(msg => {
                    const messageDiv = document.createElement("div");
                    messageDiv.className = msg.sender === "user" ? "user-message" : "bot-message";
                    const fmt = msg.text.replace(/\n/g, '<br>');
                    messageDiv.innerHTML = `
                        <div class="avatar">${msg.sender === 'user' ? '👤' : '🤖'}</div>
                        <div class="message"><p>${fmt}</p></div>
                    `;
                    chatBox.appendChild(messageDiv);
                });
                chatBox.scrollTop = chatBox.scrollHeight;
                renderHistory(); 
            });

            row.querySelector(".history-delete-btn").addEventListener("click", (e) => {
                e.stopPropagation();
                delete allSessionsMemory[sessionId];
                delete sessionTitles[sessionId];
                saveToLocalStorage();
                
                if (currentSessionId === Number(sessionId)) {
                    currentSessionId = Date.now();
                    chatBox.innerHTML = defaultWelcomeHTML;
                }
                renderHistory();
            });

            historyList.appendChild(row);
        });
    }

    async function fetchOllamaRAGResponse(prompt) {
        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: prompt })
            });
            const data = await response.json();
            return data.answer || "Error: Received empty response stack.";
        } catch (error) {
            console.error("Backend pipeline unreachable: ", error);
            return "Connection error. Please ensure your Ollama Flask service runner instance is fully up.";
        }
    }

    async function handleSend() {
        // Double transmission lock out execution
        if (isRequestPending) return;

        const text = questionInput.value.trim();
        if (!text) return;

        // FIXED RULE: Clear out text buffer instantly so subsequent parallel event triggers bounce out safely
        questionInput.value = "";
        isRequestPending = true;
        sendBtn.style.opacity = "0.5"; // Visual tracking indicator block
        
        // Single session tracking title string update context
        if (!sessionTitles[currentSessionId]) {
            const cleanTitle = text.length > 20 ? text.substring(0, 20) + "..." : text;
            sessionTitles[currentSessionId] = cleanTitle;
        }

        appendMessage(text, "user");
        renderHistory(); 

        // 🚀 1. INJECT LOADER: Response dynamic pipeline hit avvagane indicator append chesthundhi mawa
        const typingIndicatorDiv = document.createElement("div");
        typingIndicatorDiv.className = "typing-container-wrapper";
        typingIndicatorDiv.id = "liveTypingLoaderNode";
        typingIndicatorDiv.innerHTML = `
            <div class="avatar">🤖</div>
            <div class="typing-indicator">
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
            </div>
        `;
        chatBox.appendChild(typingIndicatorDiv);
        chatBox.scrollTop = chatBox.scrollHeight;

        // Pipeline API processing trigger execution
        const botOutput = await fetchOllamaRAGResponse(text);

        // 🚀 2. DROP LOADER: Bot response ready avvagane dynamic placeholder bubble ni clean ga remove chesthundhi
        const standardTargetLoader = document.getElementById("liveTypingLoaderNode");
        if (standardTargetLoader && standardTargetLoader.parentNode) {
            standardTargetLoader.parentNode.removeChild(standardTargetLoader);
        }

        appendMessage(botOutput, "bot");

        // Release event listeners framework lock
        isRequestPending = false;
        sendBtn.style.opacity = "1";
        questionInput.focus();
    }

    // Consolidated core triggers block setup mapping
    sendBtn.addEventListener("click", (e) => {
        e.preventDefault();
        handleSend();
    });

    questionInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault(); // Prevents line breaks and text submission duplication
            handleSend();
        }
    });

    historySearch.addEventListener("input", renderHistory);

    suggestions.forEach(btn => {
        btn.addEventListener("click", () => {
            if (isRequestPending) return;
            questionInput.value = btn.innerText.replace(/[^\w\s₹]/g, '').trim(); 
            questionInput.focus();
        });
    });

    themeToggle.addEventListener("click", () => {
        const body = document.body;
        const icon = themeToggle.querySelector("i");
        if (body.classList.contains("dark")) {
            body.classList.replace("dark", "light");
            icon.className = "fa-solid fa-sun";
        } else {
            body.classList.replace("light", "dark");
            icon.className = "fa-solid fa-moon";
        }
    });

    newChatBtn.addEventListener("click", () => {
        if (isRequestPending) return;
        currentSessionId = Date.now(); 
        chatBox.innerHTML = defaultWelcomeHTML;
        questionInput.value = "";
        questionInput.focus();
        renderHistory();
    });

    // Execution entrypoint sequence setup
    chatBox.innerHTML = defaultWelcomeHTML;
    renderHistory();
});