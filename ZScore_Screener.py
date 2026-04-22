import streamlit as st

st.set_page_config(page_title="Altman Z-Score Screener", layout="wide")

st.title("Financial Distress Screening with Altman Z-Score")
st.caption(
    "Estimate a firm's distress risk from five financial ratios and interpret the result "
    "using threshold-based screening zones."
)

def calculate_z_score(x1, x2, x3, x4, x5):
    return 1.2 * x1 + 1.4 * x2 + 3.3 * x3 + 0.6 * x4 + 1.0 * x5

def classify_z_score(z):
    if z < 1.81:
        return "Distress Zone", "High screening risk"
    elif z <= 2.99:
        return "Grey Zone", "Moderate caution"
    else:
        return "Safe Zone", "Relatively stronger financial position"

with st.expander("Adjust Financial Inputs", expanded=False):
    col1, col2 = st.columns(2)

    with col1:
        x1 = st.number_input("X1  Working Capital / Total Assets", value=0.10, step=0.01, format="%.2f")
        x2 = st.number_input("X2  Retained Earnings / Total Assets", value=0.15, step=0.01, format="%.2f")
        x3 = st.number_input("X3  EBIT / Total Assets", value=0.08, step=0.01, format="%.2f")

    with col2:
        x4 = st.number_input("X4  Equity / Total Liabilities", value=1.50, step=0.01, format="%.2f")
        x5 = st.number_input("X5  Sales / Total Assets", value=1.10, step=0.01, format="%.2f")

z = calculate_z_score(x1, x2, x3, x4, x5)
zone, interpretation = classify_z_score(z)

col1, col2, col3 = st.columns(3)
col1.metric("Z-Score", f"{z:.2f}")
col2.metric("Risk Zone", zone)
col3.metric("Interpretation", interpretation)

st.subheader("Thresholds")
st.write("Distress Zone: < 1.81")
st.write("Grey Zone: 1.81 to 2.99")
st.write("Safe Zone: > 2.99")

st.subheader("Interpretation")
st.write(
    f"The current score is **{z:.2f}**, which falls in the **{zone}**. "
    "This result should be interpreted as a preliminary screening signal rather than a full prediction outcome."
)

st.subheader("Model Notes")
st.write(
    "This dashboard is designed for educational and preliminary analytical use. "
    "If your variable definitions differ from the original Altman model, the output should be described as an "
    "adapted Altman-style screening result rather than a strict reconstruction."
)

st.subheader("Limitations")
st.write(
    "The result may vary with accounting definitions, firm type, and industry structure. "
    "It is less reliable when applied mechanically to firms that differ substantially from the original model setting."
)