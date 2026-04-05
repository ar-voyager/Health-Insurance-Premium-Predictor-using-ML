# import streamlit 
import streamlit as st
# import pandas
import pandas as pd
# import time
import time
# get 'predict from prediction_helper
from prediction_helper import predict

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Insurance Calculator",
    page_icon= "https://img.icons8.com/fluency/48/doctors-bag.png",
    layout="wide"
)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header">
    <h1>Insurance Cost Calculator</h1>
    <blockquote>Let the young know they will never find a more interesting, 
            more instructive book than the patient himself. — Giorgio Baglivi.</blockquote>
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Settings")
st.sidebar.info("Fill details → Get prediction → Analyze risk")

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs(["📋 Input", "📊 Insights", "📄 Report"])

# ---------------- INPUT TAB ----------------
with tab1:

    st.markdown("### Personal Information")

    col1, col2, col3, col4 = st.columns(4)

    age = col1.number_input("Age", 18, 100, 25)
    income = col2.number_input("Income (₹ Lakhs)", 0, 200, 5)
    dependants = col3.number_input("Dependants", 0, 10, 0)
    genetical_risk = col4.slider("Genetic Risk", 0, 5, 1)

    st.markdown("### Health & Lifestyle")

    col5, col6, col7, col8 = st.columns(4)

    bmi = col5.selectbox("BMI", ["Normal", "Overweight", "Obesity", "Underweight"])
    smoking = col6.selectbox("Smoking", ["No Smoking", "Occasional", "Regular"])
    medical = col7.selectbox("Medical History", ["No Disease", "Diabetes", "Heart disease"])
    gender = col8.selectbox("Gender", ["Male", "Female"])

    st.markdown("### Insurance Details")

    col9, col10, col11 = st.columns(3)

    plan = col9.selectbox("Plan", ["Bronze", "Silver", "Gold"])
    employment = col10.selectbox("Employment", ["Salaried", "Self-Employed", "Freelancer"])
    region = col11.selectbox("Region", ["Northwest", "Southeast", "Northeast", "Southwest"])

    predict_btn = st.button("Predict Premium")

# ---------------- LOGIC ----------------
if predict_btn:

    input_dict = {
        'Age': age,
        'Number of Dependants': dependants,
        'Income in Lakhs': income,
        'Genetical Risk': genetical_risk,
        'Insurance Plan': plan,
        'Employment Status': employment,
        'Gender': gender,
        'Marital Status': "Unmarried",
        'BMI Category': bmi,
        'Smoking Status': smoking,
        'Region': region,
        'Medical History': medical
    }

    # Loading....
    with st.spinner("Analyzing your profile..."):
        time.sleep(1.2)
        # generate insurance premium cost.
        prediction = predict(input_dict)
    
    # let us print a success message after generating cost.
    with st.spinner("Priting Message ..."):
        time.sleep(1.2)
        st.success(f"""
                ### 💙 You're Covered!

                Great news! Based on your details, your estimated insurance premium is:

                ## ₹ {predict(input_dict):,.2f}

                You're taking an important step toward securing your health and financial well-being.
                We're here to support you on your journey to a healthier life and better planning.🌿
            """)

    amount = prediction[0] if isinstance(prediction, (list, tuple)) else prediction

    # Risk logic
    risk = genetical_risk * 15
    if smoking == "Regular":
        risk += 25
    if bmi == "Obesity":
        risk += 20
    if medical != "No Disease":
        risk += 20
    risk = min(risk, 100)

    # ---------------- INSIGHTS TAB ----------------
    with tab2:

        st.markdown("## 📊 Key Insights")

        colA, colB, colC = st.columns(3)

        colA.metric("💰 Premium", f"₹ {round(amount,2)}")
        colB.metric("⚠️ Risk Score", f"{risk}/100")
        colC.metric("📈 Plan", plan)

        st.markdown("### Risk Distribution")

        chart_data = pd.DataFrame({
            "Factor": ["Genetics", "Lifestyle", "Medical"],
            "Impact": [genetical_risk*10, 30 if smoking!="No Smoking" else 10, 40 if medical!="No Disease" else 5]
        })

        st.bar_chart(chart_data.set_index("Factor"))

    # ---------------- REPORT TAB ----------------
    with tab3:

        st.markdown("## 📄 Detailed Report")

        st.markdown(f"""
        ### 💰 Estimated Premium
        **₹ {round(amount,2)}**
        <br />
        ### ⚠️ Risk Score
        **{risk}/100**

        ### 🧾 Summary
        - Age: {age}
        - Income: {income} Lakhs
        - Plan: {plan}
        - Smoking: {smoking}
        - BMI: {bmi}
        """)

        report = f"""
        INSURANCE REPORT

        Premium: ₹ {round(amount,2)}
        Risk Score: {risk}

        Age: {age}
        Income: {income}
        Plan: {plan}
        """

        st.download_button("⬇️ Download Report", report)

# ---------------- CSS ----------------
st.markdown("""
<style>

/* Header */
.header {
    text-align: center;
    padding: 20px;
    background: linear-gradient(90deg, #3a7bd5, #00d2ff);
    border-radius: 15px;
    color: white;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

/* Cards spacing */ 
.block-container {
    padding-top: 2rem;
}

/* Buttons */
button[kind="secondary"] {
    background: linear-gradient(90deg,#ff9966,#ff5e62);
    color:white;
    border-radius:10px;
    font-weight:bold;
}

/* Metric cards */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 10px;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    font-size:16px;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)