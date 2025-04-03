import streamlit as st
import requests

# Configure the page
st.set_page_config(
    page_title="Food Nutrition Analyzer 🍏",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header
st.title("Food Nutrition Analyzer 🍏")
st.markdown("#### Your AI-Powered Food Nutrition Assistant 🤖")
st.markdown("---")

# Sidebar Navigation
st.sidebar.header("Navigation")
app_mode = st.sidebar.radio("Select an Option", ["Analyze Food", "Ask Nutrition Question"])

API_BASE_URL = "http://127.0.0.1:8000"  # Update if your FastAPI backend is hosted elsewhere

if app_mode == "Analyze Food":
    st.header("🍎 Analyze Food Nutrition Details")
    st.markdown("Enter a food item to fetch detailed nutrition information.")
    
    food_item = st.text_input("Food Item:", placeholder="e.g., Apple, Broccoli, Almonds")
    if st.button("Analyze 🍽️"):
        if food_item:
            with st.spinner("Fetching nutrition info... ⏳"):
                try:
                    # Call the FastAPI endpoint for analyzing food nutrition
                    response = requests.get(f"{API_BASE_URL}/analyze/{food_item}")
                    if response.status_code == 200:
                        data = response.json()
                        st.success("Nutrition info retrieved successfully! 🎉")
                        st.markdown("### Nutrition Details:")
                        st.write(data.get("nutrition_info", "No details available."))
                    else:
                        st.error("Error fetching nutrition info. Please try again. 🚨")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("⚠️ Please enter a food item.")

elif app_mode == "Ask Nutrition Question":
    st.header("💡 Ask a Nutrition Question")
    st.markdown("Pose any food or nutrition-related question and get expert insights!")
    
    question = st.text_area("Your Question:", placeholder="e.g., What are the best sources of Vitamin B12?")
    if st.button("Get Answer 🤖"):
        if question:
            with st.spinner("Querying knowledge base... ⏳"):
                try:
                    # Call the FastAPI endpoint for answering nutrition questions
                    response = requests.get(f"{API_BASE_URL}/ask/{question}")
                    if response.status_code == 200:
                        data = response.json()
                        st.success("Answer retrieved successfully! 🎉")
                        st.markdown("### Answer:")
                        st.write(data.get("answer", "No answer available."))
                    else:
                        st.error("Error fetching answer. Please try again. 🚨")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("⚠️ Please enter your question.")

# Footer / Sidebar Info
st.sidebar.markdown("---")
st.sidebar.info("This app is powered by FastAPI and Streamlit.\nBuilt with ❤️ by Your Praveen.")
st.sidebar.markdown("© 2025 Food Nutrition Analyzer")
