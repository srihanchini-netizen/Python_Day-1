import streamlit as st

# Set page configuration
st.set_page_config(page_title="My Streamlit App", layout="wide")

# Title and header
st.title("🎯 Welcome to My Streamlit App")
st.subheader("Interactive Data Dashboard")

# Sidebar for controls
st.sidebar.header("Controls")
name = st.sidebar.text_input("Enter your name:", "User")
age = st.sidebar.slider("Select your age:", 0, 100, 25)
city = st.sidebar.selectbox("Choose a city:", ["New York", "London", "Tokyo", "Paris", "Sydney"])

# Display user info
st.write(f"Hello, **{name}**! You are **{age}** years old and from **{city}**.")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.header("📊 Data Visualization")
    # Sample data
    days = [1, 2, 3, 4, 5, 6, 7]
    sales = [250, 180, 320, 450, 200, 380, 490]
    
    st.line_chart({"Days": days, "Sales": sales})

with col2:
    st.header("📈 Statistics")
    st.metric("Total Sales", "$45,231", "+15%")
    st.metric("Total Visits", "12,543", "+8%")
    st.metric("Conversion Rate", "3.2%", "-0.5%")

# Divider
st.divider()

# Input form
st.header("📝 Feedback Form")
with st.form("feedback_form"):
    comment = st.text_area("Share your feedback:")
    rating = st.radio("Rate your experience:", ["Poor", "Average", "Good", "Excellent"])
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        if comment:
            st.success(f"✅ Thank you! Your feedback: '{comment}' (Rating: {rating})")
        else:
            st.warning("⚠️ Please enter some feedback!")

# Footer
st.divider()
st.caption("Made with ❤️ using Streamlit")
