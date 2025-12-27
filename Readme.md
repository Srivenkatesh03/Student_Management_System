# 🎓 Student Management System – Django Web Application

A **full-stack Student Management System** built using **Django**, featuring authentication, role-based access control, CRUD operations, image uploads, search, pagination, and a clean Bootstrap UI.

This project demonstrates **practical Django development skills**, backend logic, and frontend integration suitable for **entry-level software engineering roles**.

---

## 📌 Features

### 🔐 Authentication & Authorization
- User login and logout using Django’s built-in authentication system
- Role-based access:
  - **Public users**: View student list and details
  - **Staff users**: Add, edit, and delete students
- Secure POST-based logout and CSRF protection

### 👨‍🎓 Student Management (CRUD)
- Add new students with profile image
- View student details in a card-based UI
- Update student information
- Delete students with confirmation modal
- Automatic cleanup of uploaded images using Django signals

### 🔍 Search & Pagination
- Search students by:
  - Name
  - Email
  - Roll number
  - Department
- Paginated student list for scalability
- Search state preserved across pagination

### 🖼 Image Handling
- Upload student profile images
- Default placeholder for missing images
- Automatically delete old images on update
- Automatically delete images when student is removed

### 🎨 UI & UX
- Responsive design using **Bootstrap 5**
- Clean dashboard-style layout
- Badges for department and year
- Confirmation modal for delete actions
- User-friendly form validation messages

---

## 🛠 Tech Stack

**Backend**
- Python
- Django

**Frontend**
- HTML5
- CSS3
- Bootstrap 5

**Database**
- SQLite (development)
- Easily configurable for MySQL / PostgreSQL

**Tools & Concepts**
- Django ORM
- ModelForms
- Django Signals
- Authentication & Authorization
- Pagination & Filtering
- Git & GitHub

---

## 📂 Project Structure

```text
student_manager/
│
├── core/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── signals.py
│   └── templates/
│       └── core/
│           ├── student_list.html
│           ├── student_detail.html
│           ├── student_form.html
│           └── base.html
│
├── templates/
│   └── registration/
│       └── login.html
│
├── media/
│   └── students/
│
├── manage.py
└── requirements.txt
