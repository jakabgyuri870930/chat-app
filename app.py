import streamlit as st

# 1. PAGE SETUP
st.set_page_config(page_title="Family Shopping Assistant", page_icon="🏠")

st.title("🏠 Family Shopping Assistant")
st.write("Compare items, calculate true value, and get instant AI consensus.")
st.divider()

# 2. THE DROPDOWN MENU
# Updated to reflect your custom list!
appliance_type = st.selectbox(
    "What are we shopping for?",
    ["Refrigerator", "Washing Machine", "Tablet", "Mobile Phone", "Dishwasher"]
)

# 3. THE ITEM SEARCH (The new, clean UX)
st.subheader(f"Find a {appliance_type}")
model_name = st.text_input(f"Enter the Brand and Model (e.g., Samsung Bespoke, iPad Air):")

# 4. THE INPUT BOXES
col1, col2 = st.columns(2)

with col1:
    price = st.number_input("Price (₱)", min_value=0, value=30000)
    
with col2:
    lifespan = st.number_input("Expected Lifespan (Years)", min_value=1, value=10)

# 5. THE ACTION BUTTON
if st.button("Calculate Value & Analyze"):
    
    # We add a quick check to make sure she actually typed a name!
    if model_name == "":
        st.warning("Please enter a brand and model first!")
    else:
        st.divider()
        st.subheader("📊 Analysis Results")
        
        # --- 1. THE MATH ENGINE ---
        cost_per_year = price / lifespan
        st.info(f"**Value Score:** This {appliance_type} will cost roughly **₱{cost_per_year:.2f}** per year of its expected lifespan.")
        
        # --- 2. THE AI ENGINE ---
        with st.spinner("The AI is scanning consumer consensus..."):
            try:
                from google import genai
                
                client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
                
                # The new, highly targeted prompt
                prompt = f"""
                You are an expert consumer shopping assistant. 
                Search your knowledge base for the {appliance_type} model: "{model_name}". 
                Based on general consumer consensus, provide:
                1. An overall rating out of 5 stars.
                2. A bulleted list of the top 3 Pros.
                3. A bulleted list of the top 3 Cons.
                Keep it punchy, accurate, and easy to read on a mobile phone screen.
                """
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )
                
                st.success(f"Consensus for: {model_name}")
                st.write(response.text)
                
            except Exception as error_message:
                st.error(f"Something went wrong with the AI connection: {error_message}")