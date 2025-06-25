# auth.py
import streamlit as st
from user_utils import load_users, save_users, ensure_admin_user

def login_page():
    ensure_admin_user()  # đảm bảo có admin trước khi login
    st.title("Đăng nhập")
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")

    if st.button("Đăng nhập"):
        if not username or not password:
            st.warning("Vui lòng nhập đầy đủ thông tin")
            return

        users = load_users()
        user = next((u for u in users if u["username"] == username), None)
        if not user:
            st.error("Tên đăng nhập không tồn tại.")
            return

        if user["password"] != password:
            st.error("Sai mật khẩu.")
            return

        st.session_state.username = username
        st.session_state.logged_in = True
        st.session_state.is_admin = user.get("is_admin", False)
        st.session_state.allowed = user.get("allowed", False)
        st.rerun()

    if st.button("Chưa có tài khoản? Đăng ký"):
        st.session_state.page = "register"
        st.rerun()

def register_page():
    st.title("Đăng ký tài khoản")
    username = st.text_input("Tên đăng nhập", key="reg_user")
    password = st.text_input("Mật khẩu", type="password", key="reg_pass")
    confirm = st.text_input("Nhập lại mật khẩu", type="password", key="reg_conf")

    if st.button("Đăng ký"):
        if not username or not password or not confirm:
            st.warning("Vui lòng nhập đầy đủ thông tin!")
            return
        if password != confirm:
            st.error("Mật khẩu không khớp.")
            return

        users = load_users()
        if any(u["username"] == username for u in users):
            st.error("Tên đăng nhập đã tồn tại!")
            return

        users.append({"username": username, "password": password, "allowed": False, "is_admin": False})
        save_users(users)
        st.success("Đăng ký thành công! Vui lòng chờ admin duyệt.")

    if st.button("Quay lại đăng nhập"):
        st.session_state.page = "login"
        st.rerun()
        
def logout():
    for key in ["logged_in", "username", "allowed", "is_admin"]:
        st.session_state.pop(key, None)
    st.session_state.page = "login"
    st.rerun()