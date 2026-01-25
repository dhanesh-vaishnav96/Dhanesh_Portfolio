# 🌐 Portfolio Website — FastAPI Web Application

A modern, fully responsive **portfolio web application** built using **FastAPI**, **Jinja2**, **Tailwind CSS**, and **MongoDB**.

This project is designed to showcase **featured projects, tools & technologies, certifications, education, and resume content** through a clean, animated, and responsive user interface.  
It also includes a functional **contact form** with backend data storage.

---

## 🌐 Live Demo
🚀 Deployed on Render  
👉 https://dhanesh-portfolio.onrender.com

---

## ✨ Project Features

- Modern portfolio landing page
- Featured projects showcase
- Tools & Technologies section
- Certifications display
- Education section
- Resume preview and download
- Contact form with backend storage
- Animated and interactive UI
- Fully responsive design (mobile, tablet, desktop)
- Server-side rendering with Jinja2
- Cloud deployment on Render

---

## 📂 Featured Projects Included

### 🔹 Skill Verification Engine
AI-based system to verify skills using GitHub repositories and automated code analysis.

### 🔹 Expense Tracker System
A full-stack expense tracker enabling secure transactions, monthly summaries, and visual analytics.

### 🔹 DV_!NEWS
API-powered news web application delivering real-time articles with FastAPI and NewsAPI integration.

### 🔹 Portfolio Website
Personal portfolio project showcasing projects, technologies, certifications, and contact functionality.

### 🔹 IdeaVault
Idea management web application enabling users to create, update, organize, and delete ideas.

---

## 🛠 Tools & Technologies

### Core Programming
- Python
- Java
- JavaScript
- C++
- C

### Databases
- MongoDB
- PostgreSQL
- MySQL

### Backend & Web
- FastAPI
- Pydantic
- Jinja2 Templates
- HTML5
- CSS3
- Tailwind CSS

### Development Tools & Platforms
- Git
- GitHub
- VS Code
- Antigravity
- Claude
- OpenAI
- Gemini

### Cloud & Deployment
- AWS
- Render

---

## 📁 Project Structure
```
Portfolio/
│
├── app/
│ ├── config/
│ │ └── configuration.py
│ │
│ ├── models/
│ │ └── model.py
│ │
│ ├── routes/
│ │ └── portfolio.py
│ │
│ ├── services/
│ │ └── portfolio_service.py
│ │
│ ├── static/
│ │ └── style.css
│ │
│ └── templates/
│ └── index.html
│
├── main.py
└── README.md
```

---


---

## ⚙️ How It Works

1. Client requests the portfolio homepage
2. FastAPI handles routing and requests
3. Jinja2 renders dynamic HTML templates
4. Static assets are served via FastAPI
5. Contact form submits data using POST
6. Messages are stored in MongoDB
7. Application is hosted on Render

---

## 🗄️ Database

- MongoDB Atlas is used for data persistence
- Stores contact form submissions:
  - Name
  - Email
  - Message
- Database connection handled via backend configuration

---

## 🔐 Environment Variables

For production deployment, secrets should be stored as environment variables:


---

## 🚀 Deployment on Render

1. Push project source code to GitHub
2. Create a new Web Service on Render
3. Connect the GitHub repository
4. Set Build Command:
   pip install -r requirements.txt
5. Set Start Command:
   uvicorn main:app --host 0.0.0.0 --port 10000
6. Add required environment variables
7. Deploy the application

---

## 📌 Project Highlights

- Clean modular backend architecture
- Server-side rendering with FastAPI
- Responsive UI with Tailwind CSS
- Cloud-ready deployment
- Portfolio-grade full-stack implementation

---

## 📜 License

This project is created for learning, demonstration, and educational purposes.
