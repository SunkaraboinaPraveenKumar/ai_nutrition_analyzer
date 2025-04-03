# 🍏 AI-Based Food Nutrition Analyzer

## 📌 Overview
The **AI-Based Food Nutrition Analyzer** is a powerful tool that provides detailed nutritional insights about food items and answers nutrition-related questions based on uploaded documents. It leverages **FastAPI** as the backend and **Streamlit** as the frontend, integrating **LangChain**, **FAISS**, and **Hugging Face Embeddings** for efficient information retrieval.

---

## 🚀 Features
✅ **Analyze Food Items:** Get detailed nutritional information about any food item.
✅ **Ask Nutrition Questions:** Retrieve answers based on a document-based knowledge base.
✅ **FastAPI Backend:** Lightweight and efficient RESTful API.
✅ **Streamlit Frontend:** Professional and user-friendly interface with emojis and icons.
✅ **FAISS Vector Store:** High-performance search over indexed documents.
✅ **Hugging Face Embeddings:** Efficient text embeddings for retrieval.

---

## 🏗️ Tech Stack
- **FastAPI** - Backend framework for API development
- **Streamlit** - Frontend for a professional UI
- **LangChain** - For document processing and retrieval
- **FAISS** - Vector store for efficient search
- **Hugging Face Embeddings** - Text embedding model
- **Groq (LLama 3.3-70B)** - Language model for responses
- **Loguru** - Advanced logging system

---

## 📂 Project Structure
```
📁 ai-food-nutrition-analyzer
│── 📂 src
│   ├── ai_model.py  # Handles food analysis and question answering
│── 📂 data          # Stores uploaded documents for indexing
│── 📂 logs          # Stores logs for debugging
│── main.py         # FastAPI Backend
│── app.py          # Streamlit Frontend
│── requirements.txt # Dependencies
│── README.md       # Project Documentation
```

---

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ai-food-nutrition-analyzer.git
cd ai-food-nutrition-analyzer
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and add your **Groq API Key**:
```
GROQ_API_KEY=your_api_key_here
```

### 5️⃣ Run the FastAPI Backend
```bash
uvicorn main:app --reload
```

### 6️⃣ Run the Streamlit Frontend
```bash
streamlit run app.py
```

---

## 🎯 API Endpoints
### 🌟 Root Endpoint
**GET /**  
_Returns API status._
```json
{
  "message": "AI-Based Food Nutrition Analyzer is running!"
}
```

### 🥗 Get Nutrition Info
**GET /analyze/{food_item}**  
_Returns nutrition details for a food item._
```json
{
  "food": "apple",
  "nutrition_info": "Rich in fiber, vitamin C, and antioxidants."
}
```

### ❓ Ask a Nutrition Question
**GET /ask/{question}**  
_Returns an answer based on indexed documents._
```json
{
  "question": "What are the benefits of eating spinach?",
  "answer": "Spinach is rich in iron, vitamins A, C, and K, and supports eye health."
}
```

---

## 📌 To-Do List
- [ ] Add more food-related datasets
- [ ] Enhance Streamlit UI with additional features
- [ ] Improve retrieval accuracy with better embeddings

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repo and submit pull requests.

---

## 📬 Contact
For questions or collaborations, reach out to: **sunkaraboinap@gmail.com**

---

⭐ **If you find this project useful, don't forget to star the repository!**

