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
    // Modify the decoration on top to reuse as a banner

    // Locate elements
    var decoration = window.parent.document.querySelectorAll('[data-testid="stDecoration"]')[0];
    var sidebar = window.parent.document.querySelectorAll('[data-testid="stSidebar"]')[0];

    // Observe sidebar size
    function outputsize() {
        decoration.style.left = `${sidebar.offsetWidth}px`;
    }

    new ResizeObserver(outputsize).observe(sidebar);

    // Adjust sizes
    outputsize();
    decoration.style.height = "3.0rem";
    decoration.style.right = "45px";

    // Adjust image decorations
    decoration.style.backgroundImage = "url(https://img.pokemondb.net/sprites/emerald/normal/pikachu.png)";
    decoration.style.backgroundSize = "contain";
    </script>        
    """, width=0, height=0)