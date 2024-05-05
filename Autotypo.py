import streamlit as st
import auto_typer
import remove_comments as rc
import remove_indentation as ri
import os
print(os.path.dirname(st.__file__))

st.title("CodeTantra Killer")

try:
    language = st.sidebar.selectbox("Language", ("JAVA", "Python","----Options----"))
    indentation = st.sidebar.selectbox("Is the code indented?", ("Yes", "No"))
    comments = st.sidebar.selectbox("Does the code have comments?", ("Yes", "No"))
except Exception:
    print("An error occured.")

#st.markdown("<iframe src='/AutoTypo/adsense_banner.html' width='728' height='90'></iframe>", unsafe_allow_html=True)

st.markdown("""
<style>
.container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)

with st.container():
    # Text area for pasting code with a unique key
    code_paste_key = "code_paste_area"
    code_paste = st.text_area("Paste your code here", height=300, key=code_paste_key)

    # Create a single column layout for the buttons
    col1, col2, = st.columns([1, 1])

    # Apply custom CSS to reduce the gap between the buttons
    st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock] {
        gap: 0rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Start Pasting button
    if col1.button('Start Pasting'):
        st.success('Code submitted successfully!')
        cleaned_code = rc.remove_comments(code_paste, language)
        not_intended = ri.remove_indentation(cleaned_code, indentation)
        auto_typer.stop_pasting = False  # Reset the stop flag
        auto_typer.auto_type_with_indentation(not_intended)

    # Stop Pasting button
    if col2.button('Stop Pasting'):
        auto_typer.stop_pasting = True
        st.warning('Pasting has been stopped.')

footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: black;
    color: white;
    text-align: center;
    padding: 10px;
}
</style>
<div class="footer">
    <p>Created by Shashwat Singh. Ideated by Shivansh Yadav.</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

