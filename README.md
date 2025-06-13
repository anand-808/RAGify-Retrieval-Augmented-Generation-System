# 🤖 RAGify: Retrieval-Augmented Generation System with FastAPI, MongoDB & JWT

---

## 💡 What is RAGify?

> **RAGify** = *RAG* (Retrieval-Augmented Generation) + *ify* (to make something become)

**RAGify** transforms static documents, PDFs, and custom datasets into an intelligent, interactive Q&A system powered by **Retrieval-Augmented Generation (RAG)**. It combines **semantic search** and **text generation** to answer questions grounded in your own data.

Use RAGify to:
- 📄 Convert docs into chat-based interfaces
- 🧠 Build domain-specific AI assistants
- 🔐 Provide secure, authenticated access to smart search tools

---

## 📐 Architecture Diagram

📌 _[Insert architecture diagram here]_  
_A high-level diagram will show: Data Ingestion → Chunking → Embedding → Vector DB → Retrieval → Generation → Response_

---

## 📦 Tech Stack

| Layer               | Technology                             |
|---------------------|-----------------------------------------|
| API Framework       | FastAPI                                 |
| Authentication      | Firebase Auth + OAuth2 + JWT            |
| Embedding Model     | `sentence-transformers` (`all-MiniLM`)  |
| Vector Store        | FAISS / ChromaDB                        |
| Generator Model     | HuggingFace Transformers (T5/BART)      |
| Database            | MongoDB                                 |
| Admin Dashboard     | Streamlit or Gradio                     |
| Logging             | Python `logging` (+ optional Sentry)    |
| Deployment          | Docker + GitHub Actions + AWS EC2       |
| CI/CD Pipeline      | GitHub Actions                          |

---

## 🚀 Features

- 🔐 **Secure Login with OAuth2, Firebase, and JWT**
- 🔍 **Semantic document retrieval using FAISS/Chroma**
- 🧠 **Text generation using transformer models (T5, BART)**
- 💾 **MongoDB for storing user history, feedback, metadata**
- 📊 **Admin panel for monitoring queries and performance**
- 🐳 **Dockerized for easy local and cloud deployment**
- ⚙️ **CI/CD with GitHub Actions**
- 🌐 **Optional EC2-based deployment for production**

---

## 🗂️ Project Structure

```
ragify/
│
├── app/                            # FastAPI app
│   ├── main.py                     # Entry point
│   ├── api/                        # API routes
│   ├── auth/                       # Firebase + JWT logic
│   ├── db/                         # MongoDB interaction
│   ├── retriever/                  # FAISS or Chroma logic
│   ├── generator/                  # Text generation logic
│   ├── logger/                     # Logging config
│   └── utils/                      # Chunking, text cleaning
│
├── admin/                          # Streamlit or Gradio dashboard
│
├── data/                           # Sample input data (PDFs/text)
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env                            # Secrets & API keys
├── .github/workflows/              # GitHub Actions
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ragify.git
cd ragify
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Create `.env` File

```env
OPENAI_API_KEY=your_openai_key
FIREBASE_API_KEY=your_firebase_key
FIREBASE_PROJECT_ID=your_project_id
JWT_SECRET_KEY=your_jwt_secret
MONGO_URI=your_mongo_connection_string
```

### 4. Run the App

```bash
uvicorn app.main:app --reload
```

---

## 🔐 Authentication

- Uses **Firebase Authentication** for signup/login.
- Protects API routes with **OAuth2 + JWT** access tokens.
- User roles and access levels can be expanded as needed.

---

## 📊 Admin Dashboard

Located in `/admin`, built with **Streamlit** or **Gradio**.

Provides:
- Query & user activity logs
- Document upload/status
- System health monitoring

---

## 🐳 Docker Usage

### Build Image

```bash
docker build -t ragify-app .
```

### Run Container

```bash
docker run -p 8000:8000 --env-file .env ragify-app
```

---

## 🚀 Deployment

- Local: `uvicorn app.main:app --reload`
- Cloud: Dockerized + deploy on **AWS EC2 (Free Tier)**  
- CI/CD: **GitHub Actions** automatically builds and tests on push

---

## 🔁 CI/CD Pipeline

- ✅ Lint & format code
- 🧪 Run basic tests
- 🐳 Build Docker image
- ☁️ Deploy to cloud (optional)

Configured in `.github/workflows/deploy.yml`

---

## 🙌 Acknowledgments

- [HuggingFace Transformers](https://huggingface.co/)
- [Firebase Auth](https://firebase.google.com/)
- [ChromaDB](https://www.trychroma.com/) / [FAISS](https://github.com/facebookresearch/faiss)
- [LangChain (optional integrations)](https://www.langchain.com/)