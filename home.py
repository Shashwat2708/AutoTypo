import streamlit as st

# Display an image at the top of the page
# st.image('your_image_path_here.jpg', caption='Login Page')

st.title("AutoTypo Login Page")
# Create placeholders for email and password inputs
email = st.text_input("Email")
password = st.text_input("Password", type="password")

# Create a button for submitting the login form
if st.button('Login'):
    st.success('Logged in successfully!')
    # Here you would typically handle the login logic
else:
    st.write('Please enter your email and password.')
