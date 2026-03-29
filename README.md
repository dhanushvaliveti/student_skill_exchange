# 🎓 Student Skill Exchange Platform

A web-based platform that enables students to teach and learn skills from each other using a credit-based system.

---

## 🚀 Features

### 🔐 Authentication
- User Registration
- Login & Logout
- Automatic Profile Creation (Django Signals)

---

### 🧠 Skill Management
- Add skills you can teach
- Browse available skills
- Skill levels:
  - Beginner
  - Intermediate
  - Advanced

---

### 🔄 Request System
- Send learning requests
- Accept / Reject requests
- Track request status:
  - Pending
  - Accepted
  - Scheduled
  - Completed

---

### 📅 Session Scheduling
- Teacher schedules session
- Select date and time
- Add meeting link (Zoom / Google Meet)

---

### 💬 Session System
- Join session using meeting link
- Chat section during session
- Session completion handled by teacher only

---

### 💰 Credit System
- Earn credits by teaching
- Spend credits when learning

Credit rules:
- Beginner → 1 credit
- Intermediate → 2 credits
- Advanced → 3 credits

---

### 🔥 Streak System
- Tracks user activity
- Increases with continuous participation

---

### 🏆 Leaderboard
- Ranks users based on:
  - Sessions taught
  - Streak
- Displays top users

---

### 💳 Buy Credits
- Simulated payment system
- Adds credits to user profile

---

## 🛠️ Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite
- Deployment: Replit

---

## 📁 Project Structure

skill_exchange/
│
├── accounts/
├── skills/
├── requests/
├── sessions/
├── credits/
├── leaderboard/
│
├── templates/
├── static/
├── db.sqlite3
├── manage.py

---

## ⚙️ Setup Instructions

1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/student_skill_exchange.git  
cd student_skill_exchange  

---

2. Install Dependencies

pip install django  
pip install gunicorn  

---

3. Apply Migrations

python manage.py migrate  

---

4. Create Superuser

python manage.py createsuperuser  

---

5. Run Server

python manage.py runserver  

---

## 🌐 Deployment (Replit)

gunicorn skill_exchange.wsgi:application --bind 0.0.0.0:8000  

---

## 🧪 Workflow

Add Skill → Send Request → Accept → Schedule → Join Session → Complete → Credits Update → Leaderboard Update  

---

## 🔒 Security Rules

- Only teacher can mark session as completed  
- Backend validation prevents unauthorized actions  

---

## 📌 Future Improvements

- Real-time chat system  
- Video call integration  
- Notifications system  
- Smart skill matching  

---

## 👨‍💻 Author

Dhanush Valiveti  

---

## ⭐ Note

This project is developed as part of academic learning and demonstrates full-stack development using Django.
