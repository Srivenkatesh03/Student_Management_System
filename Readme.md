# Student Management System (Django + DevOps)

A full-stack **Student Management System** built using **Django** and **PostgreSQL**,containerized using **Docker** and orchestrated with **Docker Compose** designed to manage students, marks, attendance, analytics, and role-based access (Admin & Student).  
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
- **Database:** PostgreSQL
- **Authentication:** Django Auth
- **Exports:** CSV, Excel (`openpyxl`)

---

## Features
- Student CRUD operations
- Authentication & admin panel
- Media uploads
- PostgreSQL database
- Environment-based configuration

---

## Tech Stack
- Django
- PostgreSQL
- Docker
- Docker Compose
- Gunicorn

---

## Architecture
- Django runs in a Docker container
- PostgreSQL runs as a separate service
- Data persisted using Docker volumes
- App configured using environment variables

---

##Screenshot
<img width="1920" height="1080" alt="student attadance monthly" src="https://github.com/user-attachments/assets/71b2d79b-71c6-409a-892b-aecec20da1c9" />
<img width="1920" height="1080" alt="attadance" src="https://github.com/user-attachments/assets/87868acc-bb8d-45cb-96b8-3b9e3e9f3477" />
<img width="1920" height="1080" alt="view attadance" src="https://github.com/user-attachments/assets/34422ee9-cd4d-47b9-bb02-4bb4ffdccb35" />
<img width="1920" height="1080" alt="add marks" src="https://github.com/user-attachments/assets/08111fb7-0a64-4be2-8c46-5e90ac478bc7" />
<img width="1920" height="1080" alt="mark list" src="https://github.com/user-attachments/assets/712fc15e-f4d4-4b7f-b7c1-ee938adc2493" />
<img width="1920" height="1080" alt="student login mark" src="https://github.com/user-attachments/assets/393b5891-e19d-40d7-bac5-8b28ed155994" />
<img width="1920" height="1080" alt="student attadance" src="https://github.com/user-attachments/assets/86f160de-ca8a-4b2f-a3d2-5ee76883973c" />
<img width="1920" height="1080" alt="student attadance monthly" src="https://github.com/user-attachments/assets/57fbc022-20b7-4500-b1ec-ed64da549b39" />
<img width="1920" height="1080" alt="loginpage" src="https://github.com/user-attachments/assets/f334d702-75e6-49ab-825b-eb87b3cdf1ab" />
<img width="1920" height="1080" alt="dashboard" src="https://github.com/user-attachments/assets/59d6b63b-f105-4edc-bc35-6fa30fa1ae9f" />
<img width="1920" height="1080" alt="student_list" src="https://github.com/user-attachments/assets/91f97cfa-7da7-4253-9f36-e6524808e188" />
<img width="1920" height="1080" alt="student details" src="https://github.com/user-attachments/assets/1b5380cf-f2be-4fb9-b2cb-a58169f3f11f" />
<img width="1920" height="1080" alt="student marks" src="https://github.com/user-attachments/assets/38c1e053-1af6-4dfb-a2c1-672d699b9a0d" />
<img width="1920" height="1080" alt="Screenshot (271)" src="https://github.com/user-attachments/assets/cb615541-9566-49d0-af1d-d231068115d1" />
<img width="1920" height="1080" alt="edit or add" src="https://github.com/user-attachments/assets/a595fbf2-5d55-428b-97df-d014d799bccd" />




