from fastapi import FastAPI
from pydantic import BaseModel
import openai
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env
load_dotenv()

# Get the API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Verify if the key is loaded correctly (optional for debugging)
if not openai.api_key:
    raise ValueError("OpenAI API key is missing! Check your .env file.")

# Database Setup
DATABASE_URL = "sqlite:///./tasks.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    due_date = Column(String)

Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI()


class TaskRequest(BaseModel):
    text: str

@app.post("/generate_tasks")
async def generate_tasks(request: TaskRequest):
    # prompt = f"Extract tasks and due dates from this input: {request.text}"
    client = openai.OpenAI()  # Create a client instance
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello, how are you?"}]
    )

    print(response.choices[0].message.content)

    tasks = response["choices"][0]["message"]["content"]

    # Store task in database
    new_task = Task(description=request.text, due_date="2024-02-20")  # Placeholder date
    db.add(new_task)
    db.commit()
    
    return {"tasks": tasks}
