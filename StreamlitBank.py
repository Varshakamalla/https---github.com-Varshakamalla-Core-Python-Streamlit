import streamlit as st

class Bank:
    def __init__(self):
        if 'acc_balance' not in st.session_state:
            st.session_state.acc_balance = 1000
        if 'attempt_count' not in st.session_state:
            st.session_state.attempt_count = 0

    def validation(self):
        if st.session_state.attempt_count >= 3:
            st.error("Maximum attempts completed. Exiting.")
            return

        if 'pin_verified' not in st.session_state or not st.session_state.pin_verified:
            pin = st.text_input("Enter your PIN", type="password")

            if st.button("Submit PIN"):
                if pin == "1234":
                    st.session_state.pin_verified = True
                    self.viewOptions()
                else:
                    st.session_state.attempt_count += 1
                    st.error(f"Invalid PIN. Attempt {st.session_state.attempt_count} of 3")
        else:
            self.viewOptions()

    def viewOptions(self):
        st.title("Banking System")

        deposit_amount = st.number_input("Enter the deposit amount:", min_value=100, max_value=50000, step=100)
        if st.button("Deposit"):
            if 100 <= deposit_amount <= 50000:
                st.session_state.acc_balance += deposit_amount
                st.success(f'Amount Deposited successfully. The account balance is {st.session_state.acc_balance}')
            else:
                st.error("Deposit amount must be between 100 and 50000 and a multiple of 100.")

        withdraw_amount = st.number_input("Enter the withdraw amount:", min_value=100, max_value=20000, step=100)
        if st.button("Withdraw"):
            if 100 <= withdraw_amount <= 20000 and withdraw_amount % 100 == 0:
                if withdraw_amount <= st.session_state.acc_balance and st.session_state.acc_balance >= 500:
                    st.session_state.acc_balance -= withdraw_amount
                    st.success(f'The account balance after withdrawal is {st.session_state.acc_balance}')
                else:
                    st.error("Insufficient balance or withdrawal amount exceeds limit.")
            else:
                st.error("Withdrawal amount must be a multiple of 100 and between 100 and 20000.")

        if st.button("Balance Enquiry"):
            st.info(f'Your current balance is {st.session_state.acc_balance}')

        if st.button("Exit"):
            st.session_state.pin_verified = False
            st.info("Exiting... Goodbye!")

obj = Bank()
obj.validation()
