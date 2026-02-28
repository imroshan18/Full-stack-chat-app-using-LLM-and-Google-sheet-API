

### Cloud-Based LLM Chat System with Google Sheets 

SheetBrain AI is a full-stack AI chat application that integrates a Large Language Model (LLM) with a FastAPI backend and Google Sheets as a cloud-based logging datastore.

The system demonstrates production-style architecture for AI applications, combining:

* Real-time LLM inference
* Structured API design
* Cloud-based interaction logging
* Secure environment configuration
* Modular service architecture

---

## Author

**imroshan18**

---

## Project Overview

SheetBrain AI provides an interactive web chat interface where users can:

* Communicate with a high-speed LLM (via Groq API)
* Receive real-time AI-generated responses
* Automatically log conversation history to Google Sheets
* Maintain structured metadata for analytics

Instead of using a traditional database, Google Sheets acts as a lightweight cloud-based logging layer.

This project showcases how AI services can be integrated into modern web applications with persistent tracking.

---

## Core Capabilities

### AI-Powered Conversations

* Uses Groq’s Llama-3 model
* Fast inference
* Structured request/response handling

### Persistent Cloud Logging

Each interaction is stored in Google Sheets with:

* User message
* AI response
* Timestamp
* Optional metadata

### Modular Backend Design

Separation of concerns:

* API routes
* LLM service logic
* Google Sheets integration layer

### Web-Based Frontend

* Lightweight HTML/CSS/JS interface
* Async API calls
* Clean chat layout
* Real-time updates

---

## System Architecture

The system follows a service-oriented architecture.

---

### 1. Frontend Layer

Responsible for:

* Capturing user input
* Sending API requests
* Rendering responses
* Displaying conversation history

Built with:

* HTML5
* CSS3
* Vanilla JavaScript

---

### 2. Backend API (FastAPI)

Handles:

* Chat request routing
* Input validation (Pydantic)
* LLM inference calls
* Response formatting
* Error handling

Runs via:

```plaintext
Uvicorn ASGI server
```

---

### 3. LLM Service Layer

Located in:

```plaintext
services/
```

Responsibilities:

* Sending prompts to Groq API
* Managing inference configuration
* Handling response parsing
* Returning structured output

---

### 4. Google Sheets Service Layer

Handles:

* Authentication using Service Account
* Writing conversation logs
* Spreadsheet row management
* Secure credential loading

---

## Technology Stack

| Layer                  | Technology            |
| ---------------------- | --------------------- |
| Backend                | FastAPI               |
| AI Provider            | Groq Llama-3          |
| Storage                | Google Sheets API     |
| Frontend               | HTML, CSS, JavaScript |
| Auth Libraries         | google-auth, gspread  |
| Environment Management | python-dotenv         |
| Server                 | Uvicorn               |
| Language               | Python 3.8+           |

---

## Installation Guide

### 1. Clone Repository

```bash
git clone https://github.com/your-username/SheetBrain-AI.git
cd SheetBrain-AI
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

### Step 1: Create `.env` File

```env
GROQ_API_KEY=your_groq_api_key
SPREADSHEET_ID=your_google_sheet_id
```

* `GROQ_API_KEY` → Obtain from Groq Console
* `SPREADSHEET_ID` → Extract from your Google Sheet URL

---

### Step 2: Google Service Account Setup

1. Create Google Cloud Project
2. Enable Google Sheets API
3. Create Service Account
4. Download JSON key file
5. Rename to:

```plaintext
credentials.json
```

6. Place it in the root directory

Important:
Share your Google Sheet with the `client_email` inside `credentials.json`.

---

## Running the Application

```bash
python run.py
```

Access:

Frontend:

```plaintext
http://localhost:8000
```

API Docs:

```plaintext
http://localhost:8000/docs
```

---

## Project Structure

```plaintext
SheetBrain-AI/
│
├── backend/              # FastAPI application
├── frontend/             # Static web interface
├── services/             # LLM and Sheets integrations
├── run.py                # Application entry point
├── requirements.txt
├── .env                  # Environment variables
├── credentials.json      # Google service account key
└── README.md
```

---

## Security Considerations

* `.env` excluded via `.gitignore`
* Service account credentials not committed
* API keys stored securely
* Minimal exposure of sensitive data

---

## Future Improvements

* Add conversation history retrieval
* Add user authentication
* Replace Sheets with PostgreSQL for scalability
* Add rate limiting
* Docker containerization
* Deploy on AWS / Render / Railway
* Implement streaming LLM responses

---

## Professional Positioning

This project demonstrates:

* AI integration into web applications
* API-first backend architecture
* Cloud-based logging strategies
* Modular service separation
* Secure environment management
* Real-time frontend-backend communication


