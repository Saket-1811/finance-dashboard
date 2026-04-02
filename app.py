import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Finance Dashboard", layout="centered")

st.title("💰 Advanced Financial Dashboard")

option = st.sidebar.selectbox(
    "Choose Calculator",
    ["Compound Interest", "Loan EMI", "Investment Goal"]
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
        profits = []

        for i in range(1, int(t)+1):
            A = P * (1 + r/100) ** i
            years.append(i)
            amounts.append(A)
            profits.append(A - P)

        st.success(f"Final Amount: ₹{round(amounts[-1], 2)}")

        # 📈 Growth Graph
        fig, ax = plt.subplots()
        ax.plot(years, amounts, marker='o', label="Total Amount")
        ax.plot(years, profits, linestyle='--', label="Profit")
        ax.legend()
        ax.set_xlabel("Years")
        ax.set_ylabel("Amount (₹)")
        ax.set_title("Investment Growth")

        st.pyplot(fig)

        # 📅 Table
        st.subheader("📅 Year-wise Data")
        for i in range(len(years)):
            st.write(f"Year {years[i]} → ₹{round(amounts[i], 2)}")

        # 💡 Suggestion
        if r < 5:
            st.warning("⚠️ Low return investment")
        elif r > 12:
            st.success("🔥 High return investment")

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

        # 📊 Pie Chart
        labels = ["Principal", "Interest"]
        values = [P, interest]

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        st.pyplot(fig)

        # 📉 Monthly Breakdown (ARRAY)
        st.subheader("📉 Monthly Breakdown")

        balance = P
        principal_list = []
        interest_list = []

        for i in range(n):
            interest_payment = balance * r_monthly
            principal_payment = EMI - interest_payment
            balance -= principal_payment

            principal_list.append(principal_payment)
            interest_list.append(interest_payment)

        # 📊 Graph
        fig2, ax2 = plt.subplots()
        ax2.plot(principal_list, label="Principal Paid")
        ax2.plot(interest_list, label="Interest Paid")
        ax2.legend()
        ax2.set_title("Loan Payment Breakdown")

        st.pyplot(fig2)

        # 💡 Suggestion
        if r > 12:
            st.warning("⚠️ High interest loan!")

# ---------------- INVESTMENT GOAL ----------------
elif option == "Investment Goal":

    st.header("🎯 Investment Goal Calculator")

    target = st.number_input("Target Amount (₹)", min_value=0.0)
    r = st.number_input("Interest Rate (%)", min_value=0.0)
    t = st.number_input("Time (Years)", min_value=1)

    if st.button("Calculate Required Investment"):

        r = r / 100

        required = target / ((1 + r) ** t)

        st.success(f"Required Investment Today: ₹{round(required, 2)}")

        # Growth simulation (ARRAY)
        years = []
        values = []

        for i in range(t+1):
            val = required * (1 + r) ** i
            years.append(i)
            values.append(val)

        fig, ax = plt.subplots()
        ax.plot(years, values, marker='o')
        ax.set_title("Goal Growth Projection")

        st.pyplot(fig)
