# Leave Management System – Backend

A secure and scalable **Django REST Framework backend** for a Leave Management System, developed as per the **Application Requirements Document (ARD)**.

This backend handles authentication, role-based access control, leave workflows, discussions, notifications, and audit logging.  
It is designed to integrate seamlessly with a modern frontend application.

---

##  Tech Stack

- **Backend Framework:** Django, Django REST Framework  
- **Authentication:**
  - Firebase Authentication (login/signup handled in frontend)
  - JWT (JSON Web Tokens) for API authorization
- **Database:**
  - SQLite (development)
  - PostgreSQL (production – planned)
- **Authorization:** Role-Based Access Control (RBAC)
- **Notifications:** Django-based notification system
- **Audit Logs:** Backend-managed admin action tracking
- **Integrations:**
  - Firebase Admin SDK
  - Slack Webhook (optional / configurable)

---
## 🔐 Authentication Flow (Firebase + JWT)

###  Hybrid Authentication

#### Frontend
1. User logs in / signs up using **Firebase Authentication**
2. Firebase returns an `idToken`

#### Backend
1. Frontend sends `idToken` to:

POST /api/v1/auth/firebase/login/
2. Backend:
- Verifies Firebase token
- Creates or fetches Django user
- Issues JWT access & refresh tokens

#### Secured APIs
All protected endpoints require:

Authorization: Bearer <access_token>

---

##  Environment Setup

### 1️⃣ Clone Repository
```bash
git clone <backend-repo-url>
cd BACKEND
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate    # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Environment Variables
SECRET_KEY=your-django-secret-key
DEBUG=True
5️⃣ Firebase Admin Setup

Download Firebase service account key

Save as: firebase_service_account.json

⚠️ Do NOT commit this file
Already ignored in .gitignore:
firebase_service_account.json
.env
db.sqlite3
venv/
__pycache__/
*.pyc
6️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate
7️⃣ Create Superuser
python manage.py createsuperuser
8️⃣ Start Server
python manage.py runserver
Backend runs at: http://127.0.0.1:8000

📡 API Reference (Summary)
🔐 Authentication
| Method | Endpoint                       |
| ------ | ------------------------------ |
| POST   | `/login/`                      |
| POST   | `/token/refresh/`              |
| POST   | `/api/v1/auth/firebase/login/` |
| GET    | `/api/v1/auth/me/`             |

📝 Leave APIs
| Method | Endpoint                       | Access   |
| ------ | ------------------------------ | -------- |
| GET    | `/api/v1/leaves/`              | Auth     |
| POST   | `/api/v1/leaves/`              | Employee |
| PATCH  | `/api/v1/leaves/{id}/approve/` | Admin    |
| PATCH  | `/api/v1/leaves/{id}/reject/`  | Admin    |
| PATCH  | `/api/v1/leaves/{id}/update/`  | Admin    |

💬 Discussions
| Method | Endpoint                                             |
| ------ | ---------------------------------------------------- |
| GET    | `/api/v1/discussions/leaves/{leave_id}/discussions/` |
| POST   | `/api/v1/discussions/leaves/{leave_id}/discussions/` |

🔔 Notifications
| Method | Endpoint                           |
| ------ | ---------------------------------- |
| GET    | `/api/v1/notifications/`           |
| PATCH  | `/api/v1/notifications/{id}/read/` |

🧾 Audit Logs
| Method | Endpoint          | Access |
| ------ | ----------------- | ------ |
| GET    | `/api/v1/audits/` | Admin  |
