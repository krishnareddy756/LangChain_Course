# LangChain Course - AI Agent Chatbot

Welcome to the LangChain course by Aurelio AI! This repository contains a complete full-stack AI chatbot application with deployment guides.

## 🌐 **Live Demo**

- **Frontend**: [https://lang-chain-course.vercel.app](https://lang-chain-course.vercel.app)
- **API**: [https://langchain-chatbot-5gvk.onrender.com](https://langchain-chatbot-5gvk.onrender.com)
- **API Docs**: [https://langchain-chatbot-5gvk.onrender.com/docs](https://langchain-chatbot-5gvk.onrender.com/docs)

## 🚀 **Features**

- ✅ **AI-Powered Conversations** - GPT-4 powered responses using OpenAI
- ✅ **Web Search Integration** - Real-time web search using SerpAPI
- ✅ **Streaming Responses** - Real-time response streaming for better UX
- ✅ **LangChain Agent** - Advanced reasoning and tool usage
- ✅ **Modern UI** - Clean, responsive React/Next.js frontend
- ✅ **Production Ready** - Deployed on Vercel + Render

## 🛠 **Tech Stack**

### **Backend (API)**
- **FastAPI** - Modern Python web framework
- **LangChain** - AI agent framework
- **OpenAI GPT-4** - Language model
- **SerpAPI** - Web search integration
- **Python 3.13** - Latest Python runtime

### **Frontend (Web App)**
- **Next.js 15** - React framework with Turbopack
- **React 19** - UI library
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS

### **Deployment**
- **Vercel** - Frontend hosting
- **Render** - Backend API hosting

## 🏃 **Quick Start - Capstone Project**

The main application is located in `chapters/09-capstone/`. Here's how to run it locally:

### **1. Environment Setup**

First, set up your environment variables:

```bash
# Copy the example file
cp env.example .env

# Edit .env with your API keys
OPENAI_API_KEY=your_openai_api_key_here
SERPAPI_API_KEY=your_serpapi_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

### **2. Backend Setup**

```bash
# Navigate to the API directory
cd chapters/09-capstone/api

# Start the FastAPI server
uv run uvicorn main:app --reload
```

Backend will be available at: `http://localhost:8000`

### **3. Frontend Setup**

```bash
# Navigate to the app directory
cd chapters/09-capstone/app

# Install dependencies and start
npm install
npm run dev
```

Frontend will be available at: `http://localhost:3000`

## Getting Started - Course Environment

### Python Environment (IMPORTANT)

This course repo contains everything you need to install an exact duplicate Python environment as used during the course creation. 

#### Installing Python Venvs

The Python packages are managed using the [uv](https://github.com/astral-sh/uv) package manager, and so we must install `uv` as a prerequisite for the course. We do so by following the [installation guide](https://docs.astral.sh/uv/#getting-started). For Mac users, as of 22 Oct 2024 enter the following in your terminal:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Once `uv` is installed and available in your terminal you can navigate to the course root directory and execute:

```bash
uv python install 3.12.7
uv venv --python 3.12.7
uv sync
```

> ❗️ You may need to restart the terminal if the `uv` command is not recognized by your terminal.

With that we have our chapter venv installed. When working through the code for a specific chapter, always create a new venv to avoid dependency hell.

#### Using Venv in VS Code / Cursor

To use our new venv in VS Code or Cursor we simply execute:

```
cd example-chapter
cursor .  # run via Cursor
code .    # run via VS Code
```

This command will open a new code window, from here you open the relevant files (like Jupyter notebook files), click on the top-right **Select Environment**, click **Python Environments...**, and choose the top `.venv` environment provided.

#### Uninstalling Venvs

Naturally, we might not want to keep all of these venvs clogging up the memory on our system, so after completing the course we recommend removing the venv with:

```
deactivate
rm -rf .venv -r
```

### Ollama

The course can be run using OpenAI or Ollama. If using Ollama, you must go to [ollama.com](https://ollama.com/) and install Ollama for your respective OS (MacOS is recommended).

Whenever an LLM is used via Ollama you must:

1. Ensure Ollama is running by executing `ollama serve` in your terminal or running the Ollama application. Make sure to keep note of the port the server is running on, by default Ollama runs on `http://localhost:11434`

2. Download the LLM being used in your current example using `ollama pull`. For example, to download Llama 3.2 3B, we execute `ollama pull llama 3.2:3b` in our terminal.

## 🚀 **Deployment Guide**

The capstone project is configured for easy deployment on modern cloud platforms:

### **Frontend Deployment (Vercel)**

1. **Connect Repository**
   - Go to [vercel.com](https://vercel.com) and sign in with GitHub
   - Import your repository: `krishnareddy756/LangChain_Course`

2. **Configure Settings**
   - **Root Directory**: `chapters/09-capstone/app`
   - **Framework**: Next.js
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`

3. **Environment Variables**
   ```
   NODE_ENV=production
   ```

4. **Deploy** - Vercel will automatically deploy on every push to main

### **Backend Deployment (Render)**

1. **Connect Repository**
   - Go to [render.com](https://render.com) and sign in with GitHub
   - Create new Web Service from your repository

2. **Configure Settings**
   - **Root Directory**: `chapters/09-capstone/api`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

3. **Environment Variables**
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   SERPAPI_API_KEY=your_serpapi_key_here
   LANGCHAIN_API_KEY=your_langchain_api_key_here
   ```

4. **Deploy** - Render will automatically deploy on every push to main

## 📝 **Usage**

### **Live Application**
Visit [https://lang-chain-course.vercel.app](https://lang-chain-course.vercel.app) to use the deployed chatbot.

### **Example Interactions**
- "What's the weather like in New York today?"
- "Explain machine learning in simple terms"
- "Search for the latest news about artificial intelligence"
- "How do I deploy a Python app to production?"

### **Features**
- **Real-time Streaming**: Responses stream in real-time as the AI thinks
- **Web Search**: Agent can search the web for current information
- **Multi-step Reasoning**: Complex queries are broken down and solved step-by-step
- **Tool Usage**: Dynamic selection and usage of appropriate tools

## 📁 **Project Structure**

```
langchain-course/
├── chapters/
│   ├── 01-intro.ipynb
│   ├── 02-langsmith.ipynb
│   ├── ...
│   └── 09-capstone/          # Main deployed application
│       ├── api/              # FastAPI Backend
│       │   ├── main.py       # API server
│       │   ├── agent.py      # LangChain agent
│       │   └── requirements.txt
│       └── app/              # Next.js Frontend
│           ├── src/
│           └── package.json
├── .env                      # Environment variables
├── pyproject.toml           # Python dependencies
└── README.md
```

## 🔧 **Configuration**

### **Environment Variables**

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for GPT-4 | ✅ Yes |
| `SERPAPI_API_KEY` | SerpAPI key for web search | ✅ Yes |
| `LANGCHAIN_API_KEY` | LangSmith tracking (optional) | ❌ No |

### **API Endpoints**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/health` | GET | Detailed system status |
| `/invoke` | POST | Chat with AI agent |
| `/docs` | GET | Interactive API documentation |

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

**Built with ❤️ using LangChain, FastAPI, and Next.js**