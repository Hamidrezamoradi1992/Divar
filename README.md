# پروژه شبیه‌ساز سایت دیوار با Django و DRF

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white)

پروژه پیاده‌سازی پلتفرم آگهی‌های آنلاین با معماری مدرن و امکانات پیشرفته

## 🚀 فناوری‌های استفاده شده
- **Backend**: Django 4.x + Django REST Framework (DRF)
- **Database**: PostgreSQL + Redis (برای کشینگ)
- **Task Queue**: Celery + RabbitMQ
- **Containerization**: Docker + Docker Compose
- **Authentication**: JWT + OTP (Two-Factor)
- **Email Service**: SMTP + Celery Tasks
- **Search Engine**: Django-filter (سرچ پیشرفته چندوجهی)

## 🌟 امکانات اصلی
### بخش کاربری
- 📨 سیستم ارسال/دریافت پیام بین کاربران
- 📢 انتشار آگهی با دسته‌بندی پولی/رایگان
- 🔍 سیستم جستجوی پیشرفته چندوجهی (فیلتر بر اساس قیمت، موقعیت مکانی، دسته‌بندی و...)
- 📧 ارسال ایمیل اطلاع‌رسانی برای فعالیت‌های مهم
- 🔐 احراز هویت دو مرحله‌ای با OTP
- 🔑 سیستم احراز هویت مبتنی بر JWT
- ⚡ کشینگ داده‌های پراستفاده با Redis

### بخش مدیریت
- 👤 پنل مدیریت پیشرفته برای ادمین
- 📊 مدیریت کاربران، آگهی‌ها و دسته‌بندی‌ها
- 📈 آمار و گزارش‌های تحلیلی
- ⚙️ مدیریت تنظیمات سیستمی

## 🛠️ راه‌اندازی پروژه

### پیش‌نیازها
- Docker
- Docker Compose
- Python 3.10+

### مراحل نصب
1. کلون کردن مخزن:
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
