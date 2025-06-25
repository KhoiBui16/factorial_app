import json
import os
import streamlit as st

USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

# Các hàm kiểm tra phân quyền
def is_logged_in():
    return st.session_state.get("logged_in", False)

def is_admin():
    return st.session_state.get("is_admin", False)

def is_allowed():
    return st.session_state.get("allowed", False)

def ensure_admin_user():
    users = load_users()
    if not any(u.get("is_admin", False) for u in users):
        users.append({
            "username": "admin",
            "password": "admin",
            "is_admin": True,
            "allowed": True
        })
        save_users(users)