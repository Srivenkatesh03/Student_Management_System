# 🎓 Student Management System (Django)

A full-stack **Student Management System** built using **Django**, designed to manage students, marks, attendance, analytics, and role-based access (Admin & Student).  
This project follows **real-world academic ERP logic** and is suitable for **college portals** and **learning management systems**.

---

## 🚀 Features

### 👨‍💼 Admin / Staff Features
- Add, update, delete students
- Upload student images
- Add subjects and marks
- Mark daily attendance (editable only for today)
- View attendance for any date
- Dashboard with analytics:
  - Total students
  - Pass / Fail count
  - Department-wise statistics
  - Average marks percentage
  - Average attendance percentage
  - Low attendance alerts (<75%)
- Export:
  - Individual student details (CSV)
  - Individual student marks (CSV)
  - All students + marks (Excel – multi-sheet)

---

### 👨‍🎓 Student Features
- Secure login (role-based)
- View only **their own**:
  - Profile
  - Marksheet
  - Attendance history
  - Monthly attendance report
- Attendance percentage calculated dynamically
- Monthly attendance summary (present / absent / percentage)
- Read-only access (no data modification)

---

## 🔐 Authentication & Authorization
- Django built-in authentication system
- Role-based access:
  - **Staff** → Full access
  - **Student** → Restricted to own data
- Object-level security (students cannot access others’ records)
- Safe login redirection (no infinite redirect loops)

---

## 📊 Attendance System
- Daily attendance (Present / Absent)
- Attendance can be:
  - ✅ Marked & edited only for **today**
  - ❌ Not edited for past dates
- Attendance percentage calculated dynamically
- Monthly attendance reports per student

---

## 🧠 Key Technical Concepts Used
- Django ORM & Model relationships
- Reusable business logic inside models
- Role-based dashboards
- Pagination & search
- File uploads (images)
- CSV & Excel export (`openpyxl`)
- Secure view protection
- Clean separation of concerns (models, views, templates)

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, Bootstrap
- **Database:** SQLite (can be switched to PostgreSQL/MySQL)
- **Authentication:** Django Auth
- **Exports:** CSV, Excel (`openpyxl`)

---
