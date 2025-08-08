# 📰 Auto News Fetcher & Dashboard

A Django project that fetches the latest news using RSS feeds and displays them on a web dashboard.

## 🔧 Features
- Fetches and displays recent news headlines
- Avoids duplicate entries based on title
- Manual "Fetch Latest News" button
- Admin panel for managing articles

## ⚙️ Setup Instructions

1. Clone the repo and navigate to project folder  
2. Install requirements:  
   `pip install -r requirements.txt`
3. Run migrations:  
   `python manage.py migrate`
4. Create admin user:  
   `python manage.py createsuperuser`
5. Start server:  
   `python manage.py runserver`

   
Visit: http://127.0.0.1:8000/
