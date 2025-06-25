# app.py
import streamlit as st
from auth import login_page, register_page, logout
from user_utils import is_logged_in, is_admin, is_allowed, load_users, save_users
from factorial import fact

def admin_panel():
    st.subheader("Bảng quản lý người dùng")
    users = load_users()
    edited = False
    removed_username = []
    
    for i, user in enumerate(users):
        if user.get("is_admin", False):
            continue
        
        col1, col2, col3 = st.columns([3, 2, 1])
        with col1:
            st.write(f"{user['username']}")
        with col2:
            new_allowed = st.checkbox("Cho phép", value=user.get("allowed", False), key=user["username"])
            if new_allowed != user.get("allowed", False):
                user["allowed"] = new_allowed
                edited = True
        with col3:
            if st.button("Xóa", key=f"del_{user['username']}"):
                removed_username.append(user['username'])
                
            if new_allowed != user.get("allowed", False):
                user["allowed"] = new_allowed
                edited = True
    
    if removed_username:
        users = [u for u in users if u["username"] not in removed_username]
        edited = True
        save_users(users)
        st.success(f"Đã xóa các tài khoản: {', '.join(removed_username)}")    
        st.rerun()
        
        
    if edited:
        save_users(users)
        st.success("Cập nhật phân quyền thành công.")

def factorial_page():
    st.subheader("Máy tính giai thừa")
    number = st.number_input("Nhập số", min_value=0, max_value=900)
    if st.button("Tính giai thừa"):
        st.write(f"{number}! = {fact(number)}")

def user_home():
    st.title(f"Xin chào, {st.session_state.username}")
    if st.button("Đăng xuất"):
        logout()
    elif is_admin():
        admin_panel()
        
    elif is_allowed() or is_admin():
        factorial_page()
    else:
        st.warning("Tài khoản của bạn chưa được cấp quyền sử dụng ứng dụng.")

def main():
    if "page" not in st.session_state:
        st.session_state.page = "login"

    if is_logged_in():
        user_home()
    elif st.session_state.page == "register":
        register_page()
    else:
        login_page()

if __name__ == "__main__":
    main()
