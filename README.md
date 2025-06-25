# 📦 Factorial App

A secure and user-friendly Streamlit application that calculates the factorial of a number, with built-in user authentication and admin access control.

---

## 📑 Table of Contents
1. [📁 Project Structure](#-project-structure)
2. [🔐 Features](#-features)
3. [📦 Example Usage](#-example-usage)
4. [🚀 Getting Started](#-getting-started)
5. [☁️ Deploying on Streamlit Cloud](#deploying-on-streamlit-cloud)
6. [🛠 Tech Stack](#-tech-stack)
7. [📬 Contact](#-contact)
---

## 📁 Project Structure
factorial_app/

├── app.py               
├── auth.py              
├── factorial.py         
├── user_utils.py        
├── users.json          
├── requirements.txt     
└── README.md          

---

## 🔐 Features

- User registration and login
- Passwords securely stored using SHA-256 hashing
- Admin panel:
  - Approve/reject user access (`allowed`)
  - Delete users
- Users can only access functionality after admin approval
- Seamless single-page app for both normal users and admins

---

## 📦 Example Usage
- Input: 5
- Output: The factorial of 5 is 120
- **Restrictions:** Input must be between 0 and 900 (to prevent overflow

## 🚀 Getting Started
Follow these steps to clone and run app on your local machine.

### 1. Clone the repository
```bash
git clone https://github.com/KhoiBui16/factorial_app.git
cd factorial_app
```
### 2. Set up your environment
- On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

- On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
- Make sure you have **pip** installed, then run:
```bash
pip install -r requirements.txt
```
This will install Streamlit and any other required packages listed in the file.

### 4. Run the app
- Once everything is installed, run the following command to launch the app
```bash
streamlit run app.py
```
- After a few seconds, your browser should open at:
```bash
http://localhost:8501
```
---

## ☁Deploying on Streamlit Cloud
- Want to make your app public online?
- Push your project to a public GitHub repository.
- Go to [Streamlit Cloud](https://streamlit.io/cloud)
- Click “New app”.
- Choose your repo and app.py as the main file.
- Click Deploy and enjoy your app online!

## 🛠 Tech Stack
- Python 3.x
- Streamlit
- Built-in math module for factorial computation

## 📬 Contact
For suggestions, feedback, or contributions:
+ 📧 Email: khoibui1601.email@example.com
+ 🐛 Report an issue or submit a pull request
