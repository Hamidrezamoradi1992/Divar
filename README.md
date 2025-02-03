# 📌 پروژه شبیه‌ساز سایت دیوار با Django و DRF

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white)

🚀 این پروژه 100٪ API-محور بوده و از Django REST Framework (DRF) برای توسعه استفاده شده است.

---

## 🚀 فناوری‌های استفاده‌شده

- **Backend**: Django 4.x + Django REST Framework (DRF)
- **Database**: PostgreSQL (بانک اطلاعاتی اصلی)
- **Caching & Message Broker**: Redis (سیستم کشینگ و پیام‌رسان برای Celery)
- **Task Queue**: Celery (مدیریت وظایف پس‌زمینه)
- **Containerization**: Docker + Docker Compose (مدیریت سرویس‌ها)
- **Authentication**: JWT + OTP (احراز هویت دو مرحله‌ای)
- **Email Service**: SMTP + Celery Tasks (ارسال ایمیل‌های غیرهمزمان)
- **Generic Relations**: استفاده از Generic Relation برای مدیریت تصاویر آگهی‌ها

---

## 🌟 امکانات اصلی

### 🔹 احراز هویت و امنیت
- 🔐 احراز هویت دو مرحله‌ای با OTP
- 🔑 احراز هویت با JWT
- ⚡ کشینگ داده‌ها و پیام‌رسانی با Redis

### 🔹 بخش کاربری
- 📩 ارسال و دریافت پیام بین کاربران
- 📢 انتشار آگهی با دسته‌بندی رایگان یا پولی
- 🔍 جستجوی پیشرفته (فیلتر بر اساس قیمت، موقعیت مکانی، دسته‌بندی و...)
- 📧 ارسال ایمیل اطلاع‌رسانی برای فعالیت‌های مهم

### 🔹 بخش مدیریت
- 👤 پنل مدیریت پیشرفته
- 📊 مدیریت کاربران، آگهی‌ها و دسته‌بندی‌ها
- 📈 آمار و گزارش‌های تحلیلی
- ⚙️ تنظیمات سیستمی پیشرفته

---

## 🛠️ راه‌اندازی پروژه

### پیش‌نیازها
- **Docker & Docker Compose**
- **Python 3.10+**

### 🚀 مراحل نصب

1️⃣ **کلون کردن مخزن:**
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2️⃣ **ایجاد فایل متغیرهای محیطی:**
```bash
cp .env.example .env
```
🔹 مقادیر مربوط به دیتابیس، Redis و SMTP را در `.env` تنظیم کنید.

3️⃣ **اجرای پروژه با Docker Compose:**
```bash
docker-compose up --build
```

4️⃣ **اجرای مهاجرت‌های پایگاه داده:**
```bash
docker-compose exec web python manage.py migrate
```

5️⃣ **ایجاد کاربر سوپرادمین:**
```bash
docker-compose exec web python manage.py createsuperuser
```

🔹 **دسترسی به پروژه:**
پس از اجرای موفقیت‌آمیز، سرور روی `http://localhost:8000` در دسترس خواهد بود.

---

## 📚 مستندات API

📌 مستندات کامل API به‌صورت خودکار توسط **Swagger** و **ReDoc** تولید می‌شود.
🔗 پس از اجرای پروژه، به مسیرهای `api/swagger/` یا `/api/schema/redoc/` مراجعه کنید.

---

## 🔧 متغیرهای محیطی نمونه (`.env`)
```ini
# تنظیمات عمومی
DEBUG=True
TIME_ZONE=Asia/Tehran

# تنظیمات پایگاه داده PostgreSQL
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=1
POSTGRES_PORT=5432
DB_HOST=0.0.0.0

# تنظیمات Redis
REDIS_HOST=0.0.0.0
REDIS_PORT=6379
```

---

## 🤝 مشارکت در پروژه

1️⃣ **مخزن را Fork کنید**

2️⃣ **یک Branch جدید ایجاد کنید:**
```bash
git checkout -b feature/feature-name
```

3️⃣ **تغییرات خود را Commit کنید:**
```bash
git commit -m "Add new feature"
```

4️⃣ **کد را به مخزن خودتان Push کنید:**
```bash
git push origin feature/feature-name
```

5️⃣ **Pull Request ایجاد کنید**

---

## 📄 لایسنس

🔹 این پروژه تحت **لایسنس MIT** منتشر شده است.

---

🎯 **با ارسال نظرات و پیشنهادات خود، به بهبود این پروژه کمک کنید!** 🚀
