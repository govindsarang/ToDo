# ✅ Django ToDo App

A simple and clean **Task Manager** web application built with **Django** (backend) and styled with **custom CSS + Bootstrap 5** (frontend).

---

## 📌 Project Overview

This project allows users to:
- ➕ Add new tasks
- ✅ Mark tasks as **Done**
- ↩️ Mark completed tasks as **Undone**
- ✏️ Edit existing tasks
- 🗑️ Delete tasks

Tasks are stored in a **SQLite database** via Django's ORM.

---

## 🗂️ Project Structure

```
ToDo/
│
├── manage.py
├── db.sqlite3
│
├── templates/
│   ├── home.html          ← Main task dashboard
│   └── edit_task.html     ← Edit task page
│
├── todo/                  ← Django App
│   ├── models.py          ← Task model
│   ├── views.py           ← CRUD logic
│   ├── urls.py            ← URL routing
│   └── admin.py           ← Admin panel config
│
└── todo_main/             ← Django Project settings
    ├── settings.py
    └── urls.py
```

---

## 🧱 HTML Structure

### `home.html` — Main Dashboard

| Section | Description |
|---|---|
| `<head>` | Links Bootstrap 5 CDN, Font Awesome icons, Google Fonts (Poppins) |
| **App Header** | Gradient banner with app title and current date |
| **Pending Tasks Column** | Left side — loops `{% for task in tasks %}` to display active tasks with Edit, Delete, Done buttons |
| **Completed Tasks Column** | Right side — loops `{% for task in completed_tasks %}` to show finished tasks with Undo button |
| **Add Task Bar** | Fixed bottom bar — `<form>` with `POST` method connected to `addTask` URL |
| `{% csrf_token %}` | Django security token included in all forms |
| `{% url %}` | Django template tag used for all action links (mark done, edit, delete) |

### `edit_task.html` — Edit Task Page

| Section | Description |
|---|---|
| **Card Layout** | Centred white card — vertically and horizontally centred on screen |
| **Icon Circle** | Decorative gradient circle with pencil icon |
| **Form** | `POST` form pre-filled with `{{ get_task.task }}` value, connected to `edit_task` URL |
| **Cancel Button** | `<a>` link back to home page |
| **Save Button** | Submit button to update the task |

---

## 🎨 CSS Concepts Used

### 1. Box Model
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```
Universal reset using `box-sizing: border-box` so padding doesn't overflow element width.

---

### 2. Flexbox
Used extensively for layout alignment:
```css
.task-card {
    display: flex;
    align-items: center;
    justify-content: space-between;
}
```
Also used in the add-task bar, button rows, and header layout.

---

### 3. CSS Gradients
Used for the header banner and primary buttons:
```css
background: linear-gradient(135deg, #667eea, #764ba2);
```
Creates a smooth purple-to-violet diagonal gradient.

---

### 4. Box Shadow
Adds depth and elevation to cards:
```css
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.07);
```

---

### 5. Border Radius
Rounds corners for a modern card style:
```css
border-radius: 12px;
```

---

### 6. CSS Transitions (Hover Effects)
Adds smooth hover animations:
```css
transition: transform 0.18s ease, box-shadow 0.18s ease;
```
```css
.task-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
}
```

---

### 7. Position: Fixed
Keeps the Add Task bar pinned to the bottom of the screen:
```css
.add-task-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
}
```

---

### 8. Custom Scrollbar
Styles the task list scrollbar using webkit pseudo-elements:
```css
.tasks-column::-webkit-scrollbar { width: 5px; }
.tasks-column::-webkit-scrollbar-thumb { background: #b0b8d8; border-radius: 10px; }
```

---

### 9. CSS Variables / Color Theming
Consistent color palette used across the project:

| Color | Usage |
|---|---|
| `#667eea` | Primary — buttons, borders, header |
| `#764ba2` | Gradient end — header, primary buttons |
| `#28c76f` | Success — Done button, completed cards |
| `#ff6b6b` | Danger — Undo / Delete buttons |
| `#f0f2f5` | Background — page body |

---

### 10. Media Queries (Responsive Design)
Adjusts layout for smaller screens:
```css
@media (max-width: 768px) {
    .col-divider {
        border-right: none;
        border-bottom: 1px solid #e0e4f0;
    }
    .tasks-column {
        height: 280px;
    }
}
```

---

### 11. Google Fonts
Custom font loaded from Google Fonts CDN:
```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```
```css
font-family: 'Poppins', sans-serif;
```

---

### 12. Overflow + Scroll
Task list is scrollable within a fixed height:
```css
.tasks-column {
    height: 420px;
    overflow-y: auto;
}
```

---

## ⚙️ Backend (Django)

| Feature | File |
|---|---|
| Task Model (task, is_completed, created_at, updated_at) | `todo/models.py` |
| Add, Mark Done/Undone, Edit, Delete views | `todo/views.py` |
| URL routing for all CRUD operations | `todo/urls.py` |
| Admin panel registration | `todo/admin.py` |

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/govindsarang/ToDo.git
cd ToDo

# 2. Create and activate virtual environment
python -m venv env
env\Scripts\activate        # Windows
source env/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install django

# 4. Run migrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver
```

Then open **http://127.0.0.1:8000** in your browser.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core language |
| Django | Backend framework |
| SQLite | Database |
| HTML5 | Page structure |
| Custom CSS | Styling & animations |
| Bootstrap 5 | Grid layout & responsive utilities |
| Font Awesome 4.7 | Icons |
| Google Fonts (Poppins) | Typography |

---

## 👤 Author

**Govind Sarang**  
GitHub: [@govindsarang](https://github.com/govindsarang)
