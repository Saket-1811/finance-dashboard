import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Finance Dashboard", layout="centered")

st.title("💰 Advanced Financial Dashboard")

option = st.sidebar.selectbox(
    "Choose Calculator",
    ["Compound Interest", "Loan EMI"]
)

# ---------------- COMPOUND INTEREST ----------------
if option == "Compound Interest":

    st.header("📈 Compound Interest")

    P = st.number_input("Principal (₹)", min_value=0.0)
    r = st.number_input("Interest Rate (%)", min_value=0.0)
    t = st.number_input("Time (Years)", min_value=1)

    if st.button("Calculate"):

        years = []
        amounts = []

        # ARRAY usage
        for i in range(1, int(t)+1):
            A = P * (1 + r/100) ** i
            years.append(i)
            amounts.append(A)

        st.success(f"Final Amount: ₹{round(amounts[-1], 2)}")

        # 📈 Graph
        fig, ax = plt.subplots()
        ax.plot(years, amounts, marker='o')
        ax.set_xlabel("Years")
        ax.set_ylabel("Amount (₹)")
        ax.set_title("Investment Growth")

        st.pyplot(fig)

        # 📅 Table
        st.subheader("📅 Year-wise Data")
        for i in range(len(years)):
            st.write(f"Year {years[i]} → ₹{round(amounts[i], 2)}")

# ---------------- EMI CALCULATOR ----------------
elif option == "Loan EMI":

    st.header("🏦 EMI Calculator")

    P = st.number_input("Loan Amount (₹)", min_value=0.0)
    r = st.number_input("Interest Rate (%)", min_value=0.0)
    n = st.number_input("Months", min_value=1)

    if st.button("Calculate EMI"):

        r_monthly = r / (12 * 100)

        EMI = (P * r_monthly * (1 + r_monthly)**n) / ((1 + r_monthly)**n - 1)

        st.success(f"Monthly EMI: ₹{round(EMI, 2)}")

        total_payment = EMI * n
        interest = total_payment - P

        st.info(f"Total Payment: ₹{round(total_payment, 2)}")
        st.info(f"Total Interest: ₹{round(interest, 2)}")

        # 📊 EMI Breakdown (ARRAY)
        labels = ["Principal", "Interest"]
        values = [P, interest]

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%')

        st.pyplot(fig)

        # ⚠️ Smart Suggestion
        if r > 12:
            st.warning("⚠️ High interest rate! Consider other options.")
