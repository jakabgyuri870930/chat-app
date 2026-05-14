import streamlit as st

# 1. PAGE SETUP
st.set_page_config(page_title="Family Appliance Assistant", page_icon="🏠")

st.title("🏠 Family Appliance Assistant")
st.write("Compare appliances, calculate true value, and summarize reviews instantly.")
st.divider()

# 2. THE DROPDOWN MENU
appliance_type = st.selectbox(
    "What are we shopping for?",
    ["Refrigerator", "Washing Machine", "Tablet", "Mobile Phone"]
)

# 3. THE INPUT BOXES (Using columns for a clean layout)
st.subheader(f"Enter {appliance_type} Details")

# This splits the screen into two equal columns
col1, col2 = st.columns(2)

with col1:
    price = st.number_input("Price ($)", min_value=0, value=500)

with col2:
    lifespan = st.number_input(
        "Expected Lifespan (Years)", min_value=1, value=10)

# 4. THE REVIEW BOX
st.subheader("Customer Reviews")
reviews_text = st.text_area(
    "Paste a batch of customer reviews here:", height=150)

# 5. THE ACTION BUTTON
# Everything indented under this button only happens when it is clicked!
if st.button("Calculate Value & Analyze"):

    st.divider()
    st.subheader("📊 Analysis Results")

    # We are just putting placeholder text here for now until we add the real code!
    st.info(f"The math logic for the {price} {appliance_type} will go here.")
    st.success("The AI summary of the reviews will go here.")
