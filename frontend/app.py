import streamlit as st
import requests

BASE_URL="http://127.0.0.1:8000"

st.title("Task Manager")
menu=st.sidebar.selectbox("Menu",[
    "Signup",
    "Login",
    "Create Project",
    "View Projects",
    "Create Task",
    "View Tasks",
    "Dashboard"
])

if "token" in st.session_state:
    if st.sidebar.button("Logout"):
        del st.session_state["token"]
        st.success("Logged out successfully")
        st.rerun()
    

if menu not in ["Signup", "Login"] and "token" not in st.session_state:
    st.warning("Please login first")
    st.stop()

if menu== "Signup":
    st.subheader("Signup")

    name=st.text_input("Name")
    email=st.text_input("Email")
    password=st.text_input("Password",type="password")

    if st.button("Signup"):
        if not name or not email or not password:
            st.warning("All fields are required!")
        else:
            response = requests.post(f"{BASE_URL}/signup", json={
                "name": name,
                "email": email,
                "password": password
            })
            data = response.json()

            if response.status_code==200:
                st.success(data.get("message","Signup successful"))
            else:
                st.error(data)
elif menu=="Login":
    st.subheader("Login")

    email=st.text_input("Email")
    password=st.text_input("Password",type="password")

    if st.button("Login"):
        response = requests.post(f"{BASE_URL}/login", json={
            "email": email,
            "password": password
        })
        data=response.json()

        if "access_token" in data:
            st.success("Login successful")
            st.session_state["token"]=data["access_token"]

        else:
            st.error(data)

        st.write(data)
elif menu=="Create Project":
    st.subheader("Create Project")

    name=st.text_input("Project Name")
    desc=st.text_input("Description")

    if st.button("Create Project"):
        if not name or not desc:
            st.warning("All fields are required!")
        else:
            response = requests.post(f"{BASE_URL}/projects/", json={
                "name": name,
                "description": desc
            })
            data = response.json()
            if response.status_code == 200:
                st.success("Project created successfully")
                st.json(data)
            else:
                st.error(data)
elif menu=="View Projects":
    st.subheader("Projects")

    res=requests.get(f"{BASE_URL}/projects/")
    if res.status_code==200:
        st.dataframe(res.json())
    else:
        st.error(res.json())

elif menu=="Create Task":
    st.subheader("Create Task")
    title=st.text_input("Title")
    desc=st.text_input("Description")
    priority=st.selectbox("Priority",["Low","Medium","High"])
    assigned_to=st.number_input("Assign to User ID",min_value=1)
    project_id=st.number_input("Project ID",min_value=1)

    if st.button("Create Task"):
        res=requests.post(f"{BASE_URL}/tasks/",json={
            "title": title,
            "description": desc,
            "priority": priority,
            "due_date": "2026-12-31T00:00:00",
            "assigned_to": assigned_to,
            "project_id": project_id
        })
        data = res.json()
        if res.status_code == 200:
            st.success("Task created successfully")
            st.json(data)
        else:
            st.error(data)

elif menu=="View Tasks":
    st.subheader("Tasks")

    res=requests.get(f"{BASE_URL}/tasks/")
    if res.status_code==200:
        st.dataframe(res.json())
    else:
        st.error(res.json())

elif menu=="Dashboard":
    st.subheader("Dashboard")

    projects=requests.get(f"{BASE_URL}/projects/").json()
    tasks=requests.get(f"{BASE_URL}/tasks/").json()

    col1,col2=st.columns(2)

    with col1:
        st.metric("Total Projects",len(projects))
    with col2:
        st.metric("Total Tasks",len(tasks))

    st.divider()

    priorities=[task["priority"] for task in tasks if "priority" in task]

    st.write("Task Priority Distribution")
    st.bar_chart({
        "Low": priorities.count("Low"),
        "Medium": priorities.count("Medium"),
        "High": priorities.count("High")
    })
