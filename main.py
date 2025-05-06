import streamlit as st
from prediction_helper import predict
# Set page configuration
st.set_page_config(page_title="Loan Risk Calculator", layout="centered")

# Define CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f6f9fc;
        }
        .stApp {
            font-family: 'Arial', sans-serif;
        }
        .label {
            color: #1f77b4;
            font-weight: 600;
        }
        .block-container {
            padding: 2rem 1rem;
        }
        
        .stButton>button {
            background-color:  #1f77b4;
            color: white;
            border: None;
            border-radius: 8px;
            padding: 0.5em 1em;
        }
        .stButton>button:hover {
            background-color: #145a86;
        }
        .box {
            background-color: #ffffff;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Credit Risk Model")

with st.container():
    with st.form("loan_form"):
        #st.markdown('<div class="box">', unsafe_allow_html=True)

        # Inputs in 3 columns layout
        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.number_input("Age", 18, 100, step=1)
            loan_tenure_months = st.number_input("Loan Tenure (months)", 1, 360, value=36, step=1)
            delinquency_ratio = st.slider("Delinquency Ratio", 0, 100, 30)
            residence_type = st.selectbox("Residence Type", ["Owned", "Rented", "Mortgaged"])

        with col2:
            income = st.number_input("Income", 0, 10000000, value=1200000, step=10000)
            avg_dpd_per_delinquency = st.number_input("Avg DPD", 0, 100, value=20, step=1)
            credit_utilization_ratio = st.slider("Credit Utilization Ratio", 0, 100, 30)
            loan_purpose = st.selectbox("Loan Purpose", ["Education", "Personal", "Home", "Auto"])

        with col3:
            loan_amount = st.number_input("Loan Amount", 0, 10000000, value=2560000, step=10000)
            num_open_accounts = st.number_input("Open Loan Accounts", 0, 20, value=2, step=1)
            loan_type = st.selectbox("Loan Type", ["Secured", "Unsecured"])

        loan_to_income = round(loan_amount / income, 2) if income > 0 else 0.0
        st.markdown(f'<p class="label">Loan to Income Ratio:</p><p><b>{loan_to_income}</b></p>', unsafe_allow_html=True)

        submitted = st.form_submit_button("Calculate Risk")

        st.markdown('</div>', unsafe_allow_html=True)

    if submitted:
        # Risk calculation placeholder
        probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months,
                                                    avg_dpd_per_delinquency,
                                                    delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                                                    residence_type, loan_purpose, loan_type)

        # Display the results
        # Styled result box
        st.markdown("#### 🧾 Credit Assessment Summary")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(label="📉 Default Probability", value=f"{probability:.2%}")
        with col2:
            st.metric(label="📈 Credit Score", value=f"{credit_score}")
        with col3:
            st.metric(label="⭐ Rating", value=rating)

        # Progress bar visual
        st.markdown("#### 📊 Credit Score Position")
        st.progress(min(credit_score / 900, 1.0))

        # Feedback based on score
        with st.container():
            if rating == "Poor":
                st.error(
                    "🔴 High Risk: Applicant exhibits significant credit concerns and elevated default probability.")
            elif rating == "Average":
                st.warning(
                    "🟠 Moderate Risk: Applicant has average credit indicators; careful consideration recommended.")
            elif rating == "Good":
                st.info("🟡 Low to Moderate Risk: Applicant shows generally positive credit behavior.")
            elif rating == "Excellent":
                st.success(
                    "🟢 Very Low Risk: Applicant demonstrates strong creditworthiness and stable repayment history.")