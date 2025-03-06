import streamlit as st  
import pandas as pd  

# Set page configuration  
st.set_page_config(page_title="Student Portfolio", page_icon="🎓", layout="wide")  

# Sidebar navigation  
st.sidebar.title("📌 Navigation")  
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Customized Profile", "Contact"])  

# Owner credentials  
USERNAME = "Nshuti"  
PASSWORD = "boy250"  
OWNER_NAME = "Nshuti Blessing Prince"  
OWNER_EMAIL = "nshutiblessing13@gmail.com"  
LINKEDIN_PROFILE = "https://www.linkedin.com/in/nshuti-blessing-236822333/"  

# Authentication function  
def authenticate():  
    username = st.text_input("Enter Username")  
    password = st.text_input("Enter Password", type="password")  
    if username == USERNAME and password == PASSWORD:  
        return True  
    else:  
        return False  

# Home Section  
if page == "Home":  
    st.title("🎓 Student Portfolio")  

    # Profile picture upload (Only authenticated user can update)  
    if authenticate():  
        uploaded_image = st.file_uploader("Upload profile picture", type=["jpg", "png"])  
        if uploaded_image:  
            st.image(uploaded_image, width=150, caption="Profile Pic")  
        else:  
            st.image("Boy Prince.jpg", width=150, caption="Default")  
    else:  
        st.image("Boy Prince.jpg", width=150, caption="Profile Pic (Owner Only)")  

    # Student Details  
    st.write(f"👤 *Name:* {OWNER_NAME}")  
    st.write(f"📧 *Email:* {OWNER_EMAIL}")  
    st.write(f"📚 *LinkedIn:* [View Profile]({LINKEDIN_PROFILE})")  

    location = "Musanze, Rwanda"  
    field_of_study = "BSc Software Engineering Year 3"  
    university = "INES - Ruhengeri"  

    st.write(f"📌 {location}")  
    st.write(f"📚 {field_of_study}")  
    st.write(f"🌐 {university}")  

    # Download resume  
    with open("Boy Prince CV.pdf", "rb") as file:  
        resume_bytes = file.read()  
    st.download_button(label="📝 Download Resume",  
                       data=resume_bytes, file_name="Boy Prince.pdf", mime="application/pdf")  

    st.markdown("---")  

    # About Me section  
    st.subheader("About Me")  
    about_me = st.text_area("Write a short description about yourself", "I am a passionate AI student.")  
    st.write(about_me)  

# Projects Section  
elif page == "Projects":  
    st.title("💻 My Projects")  

    # Project Filtering  
    project_filter = st.selectbox("Filter projects by year:", ["All", "Year 1", "Year 2", "Year 3", "Final Year Project"])  

    projects = [  
        {"title": "Patiente Management System", "year": "Year 2", "type": "Individual", "tech": "Python, MySQL"},  
        {"title": "Ikigugu Website", "year": "Year 3", "type": "Individual", "tech": "PHP, HTML, CSS"},  
        {"title": "To-Do List App", "year": "Year 1", "type": "Group", "tech": "JavaScript, DOM"},  
        {"title": "Student Management System", "year": "Year 3", "type": "Individual", "tech": "PHP, MySQL"},  
        {"title": "Annet Foundation Website", "year": "Final Year Project", "type": "Individual", "tech": "Java, MySQL"},  
    ]  

    df = pd.DataFrame(projects)  

    # Display filtered projects  
    if project_filter != "All":  
        df = df[df["year"] == project_filter]  

    for _, project in df.iterrows():  
        with st.expander(f"🎯 {project['title']} ({project['year']})"):  
            st.write(f"*Type:* {project['type']}")  
            st.write(f"*Technologies:* {project['tech']}")  
            st.write("🔗 GitHub: [Link Not Available]")  

# Skills & Achievements  
elif page == "Skills":  
    st.title("🚀 Skills & Achievements")  

    st.subheader("Technical Skills")  
    st.progress(80)  # Python  
    st.write("Python: ⭐⭐⭐⭐")  

    st.progress(75)  # PHP  
    st.write("PHP: ⭐⭐⭐⭐")  

    st.progress(70)  # Java  
    st.write("Java: ⭐⭐⭐")  

    st.progress(85)  # HTML & CSS  
    st.write("HTML & CSS: ⭐⭐⭐⭐⭐")  

    st.markdown("---")  

    st.subheader("Achievements")  
    st.write("✅ Patiente Management System using Python & MySQL")  
    st.write("✅ Developed a Student Management System as a final year project")  
    st.write("✅ Created a website for Annet Fundation")  

# Customize Profile  
elif page == "Customized Profile":  
    st.title("🛠 Customize Your Profile")  

    if authenticate():  
        new_name = st.text_input("Edit Name", OWNER_NAME)  
        new_bio = st.text_area("Edit Bio", "I am a passionate AI student.")  

        if st.button("Save Changes"):  
            st.success("Profile Updated Successfully!")  
    else:  
        st.warning("You are not authorized to edit this profile.")  

# Contact Section  
elif page == "Contact":  
    st.title("📞 Contact Me")  
    st.write(f"Phone Number: +250786006001")
    st.write(f"📧 *Email:* {OWNER_EMAIL}")  
    st.write(f"📚 *LinkedIn:* [View Profile]({LINKEDIN_PROFILE})")  

    name = st.text_input("Your Name")  
    email = st.text_input("Your Email")  
    message = st.text_area("Your Message")  

    if st.button("Send Message"):  
        st.success("Message Sent Successfully!")
