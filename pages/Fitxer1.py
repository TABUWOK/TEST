import streamlit as st

# Sidebar content
st.sidebar.header("Sidebar Title")
st.sidebar.subheader("Subheading")
st.sidebar.write("Sidebar content goes here.")

# Main content
st.title("Main Content")
st.write("Welcome to my Streamlit app!")
st.write("This is the main content area.")

# JS code to modify te decoration on top
st.components.v1.html(
    """
    <script>
    
    // Adjust sizes
    outputsize();
    decoration.style.height = "3.0rem";
    decoration.style.right = "45px";

    // Adjust image decorations
    decoration.style.backgroundImage = "url(https://www.les-corts.com/wp-content/uploads/cache/images/2-logo-pb-collblanc-rgb-1/2-logo-pb-collblanc-rgb-1-139828099.png)";
    decoration.style.backgroundSize = "contain";
    </script>        
    """, width=0, height=0)