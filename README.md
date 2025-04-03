# 🐍 Flask User App

## 🌍 Overview
This is a simple Flask app that demonstrates authentication and account management using SQLite3 as the database. The app includes:

- 👤 Registration & 🔑 Login
- ✉️ Email & 🔑 Password updates
- ❌ Account deletion
- 🏆 Admin privileges (manage users, assign roles, delete accounts)
- 🔒 Ensures at least 1️⃣ admin & 1️⃣ user always exist

## Features

1. **🔑 Authentication**  
   - 👥 Sign up & log in securely.
   
2. **👤 Profile 🛠️**  
   - ✉️ Update email & 🔑 password.
   - ❌ Delete account.
   
3. **🏆 Admin Perks**  
   - 🥇 First user = 👑 Admin.
   - 🔒 Must always have 1️⃣ admin.
   - 🔒 Must always have 1️⃣ user.
   - 🛠️ Admins can manage users, assign roles, and delete accounts.
   
## 🛠️ Technologies Used

- **🖥️ Backend:** 🐍 Flask
- **🗃️ Database:** SQLite3
- **🔐 Auth:** Flask-Login, Flask-WTF

## 🚀 Installation

1. 📥 Clone repo:
   ```sh
   git clone https://github.com/yourusername/flask-user-management.git
   cd flask-user-management
   ```
2. ⚙️ Create virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # 🪟 Use `venv\Scripts\activate`
   ```
3. 📦 Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. 🗃️ Initialize database:
   ```sh
   cd backend/
   python create_db.py
   ```
5. ▶️ Run Flask app:
   ```sh
   flask run
   ```

## Usage

1. 🌍 Open in browser (`http://127.0.0.1:5000`).
2. 📝 Register (🥇 user = 👑 Admin).
3. 🔑 Log in & explore features.

## Future Enhancements

- 🔄 Password reset via ✉️
- 🔑🔑 Add 2FA
- 🎨 Improve UI with 🖌️ Bootstrap

## 📜 License

📂 Open-source under [MIT License](https://opensource.org/licenses/MIT).

