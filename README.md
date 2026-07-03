 💊 Medicine Expiry Tracker

> **DBMS Course Project** — A full-stack web application to track medicine expiry dates for you and your family.

🌐 **Live Demo:** [https://medicine-expiry-tracker-ssul.onrender.com](https://medicine-expiry-tracker-ssul.onrender.com)

---

## 📌 About the Project

Medicine Expiry Tracker is a web-based application that helps users track the expiry dates of medicines for their entire family. It sends alerts for medicines that are expiring soon or have already expired, helping families avoid consuming expired medicines.

This project was built as part of the **Database Management Systems (DBMS)** course at **NMIT, Bangalore**.

---

## ✨ Features

- 🔐 **Google OAuth Login** — Sign in securely with your Google account
- 👨‍👩‍👧‍👦 **Family Management** — Track medicines for all family members
- 💊 **Medicine Validation** — Validates medicine names against a dataset of **249,345 Indian medicines**
- 🏷️ **Auto Category Detection** — Automatically detects medicine category (Tablet, Syrup, Ointment, etc.)
- 📅 **Expiry Tracking** — Color-coded status (Safe 🟢, Expiring Soon 🟡, Expired 🔴)
- 🔔 **Alerts** — Real-time alerts for expiring and expired medicines
- 📊 **Analytics** — Visual charts for medicine distribution and status
- 🔒 **Change Password** — Secure password management with view/hide toggle
- 📱 **Responsive Design** — Works on mobile and desktop

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | HTML, CSS, Bootstrap 5, JavaScript |
| **Backend** | Python, Flask |
| **Database** | MySQL (Filess.io - Free hosted) |
| **ORM** | SQLAlchemy |
| **Authentication** | Google OAuth 2.0 (Authlib) |
| **Deployment** | Render (Free tier) |
| **Dataset** | A-Z Medicines Dataset of India (Kaggle) |

---

## 🗃️ Database Schema

```
Users ──────────┐
                ├── FamilyMembers
                ├── Medicines ──── Categories
                └── Alerts
```

**Tables:**
- `Users` — Registered users
- `FamilyMembers` — Family members per user
- `Categories` — Medicine categories (Tablet, Syrup, etc.)
- `Medicines` — Medicine records with expiry dates
- `Alerts` — Expiry alerts

---

## 📸 Screenshots

### Login Page
- Google OAuth login
- Email/password login
- View/hide password toggle

### Dashboard
- Medicine count by status (Safe, Expiring Soon, Expired)
- Full medicine list with quantity and expiry date
- Edit and Delete options

### Add Medicine
- Medicine name validation (249K+ medicines)
- Auto category detection
- Family member selection

---

## 🚀 Project Setup (Local)

### Prerequisites
- Python 3.x
- MySQL database
- Google OAuth credentials

### Installation

```bash
# Clone the repository
git clone https://github.com/Reethika415/Medicine_Expiry_Tracker.git
cd Medicine_Expiry_Tracker/MedicineTracker_Backend

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

### Environment Variables
```
DATABASE_URL=mysql+pymysql://user:password@host:port/dbname
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
SECRET_KEY=your_secret_key
```

---

## 👥 Team

| Name | Role |
|------|------|
| K. Reethika Reddy | Backend & Deployment |

**Institution:** Nitte Meenakshi Institute of Technology (NMIT), Bangalore
**Course:** Database Management Systems (DBMS)
**Year:** 2026

---

## 📊 Dataset

- **Source:** [A-Z Medicines Dataset of India — Kaggle](https://www.kaggle.com/)
- **Records:** 249,345 unique medicine names
- **Usage:** Medicine name validation

---

## 🌐 Deployment

| Service | Purpose | Cost |
|---------|---------|------|
| [Render](https://render.com) | App Hosting | Free |
| [Filess.io](https://filess.io) | MySQL Database | Free |
| [Google Cloud](https://console.cloud.google.com) | OAuth 2.0 | Free |

---

## 📄 License

This project is for educational purposes only.
