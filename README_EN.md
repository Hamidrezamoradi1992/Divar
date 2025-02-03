
# 📌 Website Simulator Project (Similar to Divar) with Django and DRF

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white)

🚀 This project is 100% API-driven and utilizes Django REST Framework (DRF) for development.

---

## 🚀 Technologies Used

- **Backend**: Django 4.x + Django REST Framework (DRF)
- **Database**: PostgreSQL (Main database)
- **Caching & Message Broker**: Redis (Caching system and message broker for Celery)
- **Task Queue**: Celery (Background task management)
- **Containerization**: Docker + Docker Compose (Service management)
- **Authentication**: JWT + OTP (Two-factor authentication)
- **Email Service**: SMTP + Celery Tasks (Asynchronous email sending)
- **Generic Relations**: Using Generic Relation to manage advertisement images

---

## 🌟 Main Features

### 🔹 Authentication & Security
- 🔐 Two-factor authentication with OTP
- 🔑 JWT-based authentication
- ⚡ Data caching and messaging with Redis

### 🔹 User Features
- 📩 Send and receive messages between users
- 📢 Post advertisements with either free or paid categories
- 🔍 Advanced search (Filter by price, location, category, etc.)
- 📧 Send notification emails for important activities

### 🔹 Admin Features
- 👤 Advanced admin panel
- 📊 Manage users, advertisements, and categories
- 📈 Analytics and reporting
- ⚙️ Advanced system settings

---

## 🛠️ Setup Guide

### Prerequisites
- **Docker & Docker Compose**
- **Python 3.10+**

### 🚀 Installation Steps

1️⃣ **Clone the repository:**
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2️⃣ **Create the environment variables file:**
```bash
cp .env.example .env
```
🔹 Set values for the database, Redis, and SMTP in the `.env` file.

3️⃣ **Run the project with Docker Compose:**
```bash
docker-compose up --build
```

4️⃣ **Run database migrations:**
```bash
docker-compose exec web python manage.py migrate
```

5️⃣ **Create a superuser account:**
```bash
docker-compose exec web python manage.py createsuperuser
```

🔹 **Access the project:**
Once the setup is complete, the server will be available at `http://localhost:8000`.

---

## 📚 API Documentation

📌 Complete API documentation is automatically generated using **Swagger** and **ReDoc**.
🔗 After running the project, visit `/swagger/` or `/redoc/` paths.

---

## 🔧 Sample Environment Variables (`.env`)
```ini
# General settings
DEBUG=True
TIME_ZONE=Asia/Tehran

# PostgreSQL database settings
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=1
POSTGRES_PORT=5432
DB_HOST=0.0.0.0

# Redis settings
REDIS_HOST=0.0.0.0
REDIS_PORT=6379
```

---

## 🤝 Contributing

1️⃣ **Fork the repository**

2️⃣ **Create a new branch:**
```bash
git checkout -b feature/feature-name
```

3️⃣ **Commit your changes:**
```bash
git commit -m "Add new feature"
```

4️⃣ **Push your code to your fork:**
```bash
git push origin feature/feature-name
```

5️⃣ **Create a Pull Request**

---

## 📄 License

🔹 This project is licensed under the **MIT License**.

---

🎯 **Help improve this project by submitting your feedback and suggestions!** 🚀
