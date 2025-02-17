### BACKEND

### Tech Stack:
🔹 FastAPI – Backend (handles AI processing)
🔹 React.js – Frontend (user interface)
🔹 OpenAI API – AI-powered task extraction
🔹 SQLite / PostgreSQL – Task storage

### Install Dependencies
pip install fastapi uvicorn openai sqlalchemy pydantic

### Run FastAPI Server
uvicorn main:app --reload

### FRONTEND

### Setup React Project
npx create-react-app smart-task-manager
cd smart-task-manager
npm install axios


### Run React Frontend
npm start

### Final Steps
✅ FastAPI running at http://127.0.0.1:8000
✅ React running at http://localhost:3000
✅ Now, enter tasks in the input box, and AI will generate suggestions! 🎯