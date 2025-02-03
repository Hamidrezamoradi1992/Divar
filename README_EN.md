# 🚀 Website Simulator Project with Django & DRF

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white)

---

## 🏗 Technologies Used

- **Backend**: Django 4.x + DRF
- **Database**: PostgreSQL
- **Caching & Queue**: Redis + Celery
- **Containerization**: Docker & Docker Compose
- **Authentication**: JWT + OTP
- **Email Service**: SMTP + Celery Tasks
- **File Handling**: Generic Relations for ads' images

---

## 🎯 Features

### 🔐 Authentication & Security
- ✅ Two-factor authentication (OTP)
- 🔑 JWT authentication
- ⚡ Data caching with Redis

### 👤 User Panel
- ✉️ Messaging between users
- 📢 Post ads (free & paid)
- 🔍 Advanced search filters
- 📧 Email notifications

### 🔧 Admin Panel
- 🎛 User & Ad management
- 📊 Analytics & Reports
- ⚙️ Advanced settings

---

## 🚀 Setup Guide

### Prerequisites
- 🐍 Python 3.10+
- 🐳 Docker & Docker Compose

### 🏁 Installation Steps

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
cp .env.example .env
```

🔧 Update `.env` with database, Redis, and SMTP settings.

```bash
docker-compose up --build
```

```bash
docker-compose exec web python manage.py migrate
```

```bash
docker-compose exec web python manage.py createsuperuser
```

🌍 Access the project at `http://localhost:8000`

---

## 📜 API Documentation

📌 Auto-generated with **Swagger** & **ReDoc**.
🌐 Visit `/api/swagger/` or `/api/schema/redoc/` after running the project.

---

## ⚙️ Environment Variables (`.env`)
```ini
DEBUG=True
TIME_ZONE=Asia/Tehran
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=1
POSTGRES_PORT=5432
DB_HOST=0.0.0.0
REDIS_HOST=0.0.0.0
REDIS_PORT=6379
```

---

## 🤝 Contributing

1️⃣ Fork the repo
2️⃣ Create a feature branch
3️⃣ Commit & push changes
4️⃣ Submit a PR 🚀

---

## 📜 License

📌 This project is under the **MIT License**.

💡 **Your feedback helps improve this project!** 🚀
