import streamlit as st
import pandas as pd
from agent import recommend
from notify import slack_notify
from logger import log_action

st.title("🚨 Employee Risk Dashboard")



# # Mock data
# df = pd.DataFrame({
#     "EmployeeID": [101, 102],
#     "Name": ["Alice", "Bob"],
#     "Risk": ["High", "Medium"],
#     "Reason": ["Burnout", "No recent promotion"],
#     "Recommended Action": ["Reduce workload", "Assign mentor"],
#     "Status": ["Notified", "Pending"]
# })


df = pd.read_csv("explained.csv")

for i, row in df.iterrows():
    with st.expander(f"Employee {row['EmployeeNumber']}"):
        st.write(row)
        action = recommend(row)
        st.markdown(f"**Recommended Action:** {action}")
        if st.button(f"Notify for Employee {row['EmployeeNumber']}"):
            slack_notify(f"Emp-{row['EmployeeNumber']}", row['Reason'], action)
            log_action(row['EmployeeNumber'], f"Emp-{row['EmployeeNumber']}", row['Reason'], action)
            st.success("Notification sent & logged.")
