# 🧾 Review Filter App using LangChain, Groq & Streamlit

This project is an **AI-powered review filtering app** that extracts structured insights from customer reviews using **LangChain**, **Groq LLM (LLaMA3)**, and **Streamlit**. It demonstrates how to build an intelligent text extractor capable of identifying:

- Whether a product was bought as a gift
- The number of delivery days
- Key sentences about the price/value

Perfect for product teams, data analysts, or ML enthusiasts looking to explore **LLMs for real-world NLP tasks**.

---

## 🎯 Features

- ✅ Detects if the item was a gift or not  
- ⏱️ Extracts delivery time in days  
- 💬 Pulls sentences discussing product value or price  
- 🔗 Uses LangChain's `StructuredOutputParser` for accurate output  
- 💡 Clean and interactive UI with Streamlit  
- ⚡ Powered by Groq’s lightning-fast LLaMA3 models

---

## 🛠 Technologies Used

| Tool            | Purpose                                      |
|------------------|----------------------------------------------|
| Python 3         | Core programming language                    |
| Streamlit        | Web interface for user interaction           |
| LangChain        | Prompt formatting & structured parsing       |
| Groq LLaMA3      | Language model for review understanding      |
| dotenv           | For managing API keys securely               |

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x  
- A [Groq API Key](https://console.groq.com)  
- pip (Python package installer)

---

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/kashifali-ai/review-filter-app.git

# Navigate into the project directory
cd review-filter-app

# Install dependencies
pip install -r requirements.txt
