import streamlit as st

st.set_page_config(page_title="Financial Calculator", layout="centered")

st.title("💰 Financial Calculator Dashboard")

# ---------------- MENU ----------------
option = st.sidebar.selectbox(
    "Select Calculator",
    ["Compound Interest", "Loan EMI"]
)

# ---------------- COMPOUND INTEREST ----------------
if option == "Compound Interest":

    st.header("📈 Compound Interest Calculator")

    P = st.number_input("Enter Principal (₹)", min_value=0.0)
    r = st.number_input("Enter Annual Interest Rate (%)", min_value=0.0)
    n = st.number_input("Times Compounded per Year", min_value=1, step=1)
    t = st.number_input("Time (Years)", min_value=0.0)

    if st.button("Calculate Compound Interest"):

        # Formula
        A = P * (1 + (r/100)/n) ** (n * t)

        st.success(f"Final Amount: ₹{round(A, 2)}")
        st.info(f"Interest Earned: ₹{round(A - P, 2)}")

# ---------------- EMI CALCULATOR ----------------
elif option == "Loan EMI":

    st.header("🏦 Loan EMI Calculator")

    P = st.number_input("Enter Loan Amount (₹)", min_value=0.0)
    r = st.number_input("Enter Annual Interest Rate (%)", min_value=0.0)
    n = st.number_input("Enter Loan Duration (Months)", min_value=1, step=1)

    if st.button("Calculate EMI"):

        r_monthly = r / (12 * 100)

        EMI = (P * r_monthly * (1 + r_monthly)**n) / ((1 + r_monthly)**n - 1)

        st.success(f"Monthly EMI: ₹{round(EMI, 2)}")
        st.info(f"Total Payment: ₹{round(EMI*n, 2)}")