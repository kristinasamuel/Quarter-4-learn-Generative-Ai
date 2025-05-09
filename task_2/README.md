# 🚀 FastAPI – Quick Setup

## 📌 What is FastAPI?

FastAPI is a **modern, high-performance** web framework for building APIs with Python. It uses Python type hints for validation, automatic docs, and asynchronous support — making it ideal for fast development of RESTful APIs.

---

## ✅ Why we use FastAPI?

- ⚡ **Fast & efficient**: High performance, on par with Node.js and Go.
- 🛠️ **Auto-generated docs**: Comes with Swagger UI and ReDoc.
- 🧠 **Smart validation**: Uses type hints for validation and data parsing.
- ⏱️ **Asynchronous support**: Great for real-time and concurrent apps.
- 📦 **Easy setup** with modern tools like `uv` and virtual environments.

---

## 🛠️Project Setup

- Step 1: Initialize a new FastAPI project
uv init task_2

- Step 2: Move into the project directory
cd task_2

- Step 3: Add FastAPI and standard dependencies
uv add fastapi[standard]

- Step 4: Activate the virtual environment
.venv\Scripts\activate

- Step 5: Run the development server
fastapi dev main.py

- Visit at:
http://127.0.0.1:8000
Swagger Docs: http://127.0.0.1:8000/docs

## What is `uv`?

**`uv`** is a **project manager** that helps you easily manage dependencies and virtual environments in Python projects.  
