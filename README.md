# 🛍️ AI-Powered Shopping Agent

An intelligent shopping assistant powered by AI that fetches live product data from a public API and helps users make smart purchasing decisions. The assistant is built using Python and integrates with OpenAI-compatible models (like Gemini) for natural language processing.

---

## 🚀 Features

- 🤖 Conversational AI assistant
- 🔌 Live product data via external API
- 🧠 Suggests products based on user queries
- 💬 Friendly, helpful responses
- 📦 Easily extendable with more tools

---

## 🧰 Tech Stack

- **Python 3.10+**
- **OpenAI Agent Framework**
- **Gemini API (via OpenAI-compatible client)**
- **Requests (for API calls)**
- **Dotenv (for environment variables)**

---

## 📡 Live API

The shopping agent pulls real-time product data from:

https://hackathon-apis.vercel.app/api/products


---

## 🧠 How It Works

1. The user inputs a natural language query (e.g., *"What should I buy to upgrade my room?"*).
2. The AI agent processes the input using a large language model.
3. The agent invokes a tool (`get_products`) to fetch live product data.
4. The agent analyzes the data and responds with relevant product suggestions.

---

## 🛠️ Setup & Run

### 1. Clone the Repository

```bash
git clone https://github.com/daniyalpervaiz/shopping-agent.git
cd shopping-agent
