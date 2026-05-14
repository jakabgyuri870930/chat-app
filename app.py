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

col1, col2 = st.columns(2)

with col1:
    # Changed the label to (₱) and the default starting value to 30000
    price = st.number_input("Price (₱)", min_value=0, value=30000)

with col2:
    lifespan = st.number_input(
        "Expected Lifespan (Years)", min_value=1, value=10)

# 4. THE REVIEW BOX
st.subheader("Customer Reviews")
reviews_text = st.text_area(
    "Paste a batch of customer reviews here:", height=150)

# 5. THE ACTION BUTTON
if st.button("Calculate Value & Analyze"):

    st.divider()
    st.subheader("📊 Analysis Results")

    # --- 1. THE MATH ENGINE ---
    # A simple calculation: How much does this appliance cost per year of its life?
    cost_per_year = price / lifespan

    st.info(
        f"**Value Score:** This {appliance_type} will cost you roughly **₱{cost_per_year:.2f}** per year of its expected lifespan.")

    # --- 2. THE AI ENGINE ---
    if reviews_text == "":
        st.warning("Please paste some reviews for the AI to analyze!")
    else:
        with st.spinner("The AI is reading the reviews..."):
            try:
                # We use the Streamlit secrets vault for the API key
                from google import genai
                client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

                # We give the AI a very specific job description
                prompt = f"""
                You are an expert shopping assistant. Read these customer reviews for a {appliance_type}.
                Provide a quick, punchy summary.
                Include:
                1. An overall consensus out of 5 stars based on the tone.
                2. A bulleted list of the top 3 Pros.
                3. A bulleted list of the top 3 Cons.
                
                Here are the reviews:
                {reviews_text}
                """

                # Make the call to the model
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )

                # Print the AI's answer on the screen
                st.success("Analysis Complete!")
                st.write(response.text)

            except Exception as error_message:
                st.error(
                    f"Something went wrong with the AI connection: {error_message}")
