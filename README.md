# Event-Driven Assessment & Auto-Grading Platform

📚 A Django + Celery based platform for **online exams with async grading, role-based access, and analytics using Pandas**.  
Built to demonstrate **system design, event-driven architecture, and scalable microservice evolution**.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![DRF](https://img.shields.io/badge/DRF-API-red)
![Celery](https://img.shields.io/badge/Celery-Async-orange)
![Redis](https://img.shields.io/badge/Redis-Cache-red)
![Pandas](https://img.shields.io/badge/Pandas-Analytics-blue)
![MySQL](https://img.shields.io/badge/MySQL-DB-yellow)
![Docker](https://img.shields.io/badgDocker-Container-lightblue)

---

## 🚀 Overview

This platform allows:
- **Role-based access** (Students, Teachers, Admins)  
- **Exam creation** with a reusable question bank  
- **Timer-based student portal** for test taking  
- **Auto-grading using Celery workers** (asynchronous, scalable)  
- **Result analytics with Pandas** (average score, pass/fail %, trends)  
- **Scalable design** that can evolve into a microservices system  

---


## 🏗️ Architecture

![Architecture Diagram]

#![Architecture](images/architecture.png)

**Core Components**
- **Accounts App** → Authentication, role management  
- **Exams App** → Question bank, exam creation, answer submission  
- **Results App** → Grading, result storage, analytics  
- **Tasks App** → Background jobs with Celery (grading, notifications)  
- **MySQL** → Persistent storage  
- **Redis** → Celery broker + result backend  
- **Pandas** → Analytics & reporting  
- **Swagger / ReDoc** -> API Docs

---

## 📂 Project Structure

online_assessment/
├── assessment_platform/ # Django project
├── accounts/ # Auth, roles
├── exams/ # Exams, questions
├── results/ # Grading, analytics
├── requirements.txt
├── README.md
└── .gitignore

---

## 🌐 API Endpoints

### 🔑 accounts
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/users/register/` | `POST` | Register a new student/teacher |
| `/api/users/login/` | `POST` | Obtain JWT token |
| `/api/users/profile/` | `GET` | Get current user profile |
| `/api/users/` | `GET` | (Admin only) List all users |


---

### 📝 Exams
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/exams/questions/` | `POST` | Add a question (teacher only) |
| `/api/exams/questions/` | `GET` | List all questions |
| `/api/exams/create/` | `POST` | Create an exam (teacher) |
| `/api/exams/` | `GET` | List all exams (student view) |
| `/api/exams/{exam_id}/submit/` | `POST` | Submit answers (student) |


**Example Submit Request**
```json
POST /api/exams/5/submit/
{
  "answers": {
    "q1": "B",
    "q2": "True",
    "q3": "42"
  }
}


📊 Results
| Endpoint | Method | Description |
|----------|--------|-------------|
|`/api/results/{exam_id}/` | `GET` | Get results of an exam |
|`/api/results/user/{user_id}/` | `GET` | Get results of a user |
|`/api/results/analytics/`|	`GET` |	Get exam statistics|

**Example analytical Response**
```Json
{
  "exam_id": 5,
  "average_score": 72.5,
  "pass_rate": 65,
  "highest_score": 95,
  "lowest_score": 40
}

⚡ Tasks (Async)
| Endpoint | Method | Description |
|----------|--------|-------------|
|`/api/tasks/status/{task_id}/`	| `GET` |	Get status of a Celery task |

⚙️ Installation (Local)
1️⃣ Clone Repository
git clone https://github.com/your-username/event-driven-assessment.git
cd event-driven-assessment

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment

Copy .env.example → .env and set values:

SECRET_KEY=your_django_secret
DEBUG=True
DB_NAME=assessment_db
DB_USER=root
DB_PASSWORD=password
DB_HOST=db
DB_PORT=3306
REDIS_URL=redis://redis:6379/0


5️⃣ Run Migrations
python manage.py migrate

6️⃣ Start Development Server
python manage.py runserver

🐳 Run with Docker
docker-compose up --build


Django → http://localhost:8000

MySQL → localhost:3306

Redis → localhost:6379


⚡ Celery Worker

In another terminal:

celery -A assessment worker -l info


📊 Sample Analytics (Pandas)
from results.models import ExamResult
import pandas as pd

qs = ExamResult.objects.all().values()
df = pd.DataFrame(qs)
print(df.groupby("exam_id")["score"].mean())


🔮 Future Enhancements

Convert into microservices (Auth, Exams, Results, Notifications)

Add React frontend for UI

Real-time notifications with WebSockets / Django Channels

Plagiarism detection service