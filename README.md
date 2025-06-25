# 📦 Factorial App

**A simple Streamlit app to calculate the factorial of a number.**

- ✅ Minimum input: `0`
- ✅ Maximum input: `900` (beyond this may cause overflow or delay)
- ⚠️ Values above `900` are restricted to prevent memory overflow.
- 🚀 Built using: `Python` + `Streamlit`

---

## 📑 Table of Contents
1. [📁 Project Structure](#-project-structure)
2. [💡 How It Works](#-how-it-works)
3. [📦 Example](#-example)
4. [🚀 Getting Started](#-getting-started)
5. [☁️ Deploy to Streamlit Cloud](#deploy-to-streamlit-cloud)
6. [🛠 Tech Stack](#-tech-stack)
7. [📬 Contact](#-contact)

---

## 📁 Project Structure
factorial_app/

├── app.py            
├── factorial.py        
├── requirements.txt   
└── README.md          

## 💡 How It Works
- Enter any number between 0 and 900 into the input field.
- Click the "Calculate" button.
- The app will display the result of n! (n factorial).
- If input is invalid or too large, it shows an error message.

## 📦 Example
- Input: 5
- Output: The factorial of 5 is 120

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

## ☁Deploy to Streamlit Cloud
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
+ Open an Issue
+ Submit a Pull Request
+ Or reach out via email: khoibui1601.email@example.com
