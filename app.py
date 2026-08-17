# ========================================
# LOAN PREDICTION SYSTEM - PROFESSIONAL UI
# ==========================================
# Fixed: HTML blocks are now flush-left (no leading indentation)
# Streamlit's markdown parser treats lines indented 4+ spaces as
# literal "code blocks", which is why the HTML tags were showing
# up as raw text on screen instead of being rendered. Removing the
# indentation solves that rendering bug everywhere in the app.

import streamlit as st

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="LoanPredict AI",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS
# ==========================================

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ===== GLOBAL ===== */
html, body, [class*="css"] {
font-family: 'Inter', 'Segoe UI', sans-serif;
}
.stApp {
background: radial-gradient(circle at top right, rgba(37, 99, 235, 0.10), transparent 40%), #eef2fb;
}
.block-container {
padding-top: 3.2rem;
padding-bottom: 2rem;
max-width: 1400px;
margin: 0 auto;
}

/* ===== SIDEBAR ===== */
[data-testid="stSidebar"] {
background: linear-gradient(180deg, #07111f 0%, #0f172a 45%, #172554 100%);
border-right: 1px solid rgba(255,255,255,0.08);
}
[data-testid="stSidebar"] * {
color: white !important;
}
.sidebar-logo {
text-align: center;
padding: 12px 5px 20px 5px;
}
.sidebar-logo .icon {
width: 65px;
height: 65px;
margin: auto;
border-radius: 18px;
display: flex;
align-items: center;
justify-content: center;
background: linear-gradient(135deg, #2563eb, #06b6d4);
font-size: 30px;
box-shadow: 0 10px 30px rgba(37, 99, 235, 0.35);
}
.sidebar-logo h2 {
margin-top: 12px;
margin-bottom: 3px;
font-size: 23px;
font-weight: 800;
}
.sidebar-logo p {
color: #94a3b8 !important;
font-size: 12px;
}
.sidebar-info {
background: rgba(255,255,255,0.06);
border: 1px solid rgba(255,255,255,0.08);
border-radius: 14px;
padding: 15px;
margin-top: 25px;
}
.sidebar-info-title {
font-weight: 700;
font-size: 13px;
margin-bottom: 8px;
}
.sidebar-info-text {
color: #cbd5e1 !important;
font-size: 12px;
line-height: 1.6;
}

/* ===== HEADER ===== */
.main-header {
position: relative;
overflow: hidden;
background: linear-gradient(135deg, #1e3a8a 0%, #1d4ed8 50%, #2563eb 100%);
padding: 38px 35px;
border-radius: 24px;
color: white;
margin-top: 18px;
margin-bottom: 32px;
text-align: center;
box-shadow: 0 20px 45px rgba(29, 78, 216, 0.22);
}
.main-header:after {
content: "";
position: absolute;
width: 230px;
height: 230px;
right: -70px;
top: -90px;
border-radius: 50%;
background: rgba(255,255,255,0.10);
}
.main-header h1 {
position: relative;
z-index: 2;
margin: 0;
font-size: 34px;
font-weight: 800;
letter-spacing: -0.5px;
}
.main-header p {
position: relative;
z-index: 2;
margin: 10px auto 0 auto;
max-width: 560px;
color: #dbeafe;
font-size: 15px;
}
.header-badge {
position: relative;
z-index: 2;
display: inline-block;
margin-top: 16px;
padding: 7px 16px;
border-radius: 20px;
background: rgba(255,255,255,0.15);
border: 1px solid rgba(255,255,255,0.22);
font-size: 12px;
font-weight: 600;
color: #eff6ff;
}

/* ===== SECTION TITLES ===== */
.section-title {
color: #0f172a;
font-size: 22px;
font-weight: 800;
margin-top: 10px;
margin-bottom: 6px;
text-align: center;
}
.section-subtitle {
color: #64748b;
font-size: 13px;
margin-top: 0;
margin-bottom: 24px;
text-align: center;
}

/* ===== KPI CARDS ===== */
.metric-card {
position: relative;
overflow: hidden;
background: linear-gradient(160deg, #ffffff, #eef4ff);
padding: 22px;
min-height: 145px;
border-radius: 20px;
border: 1px solid #dbeafe;
text-align: center;
box-shadow: 0 10px 28px rgba(29, 78, 216, 0.08);
transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.metric-card:hover {
transform: translateY(-4px);
box-shadow: 0 16px 38px rgba(29, 78, 216, 0.14);
}
.metric-icon {
width: 43px;
height: 43px;
display: flex;
align-items: center;
justify-content: center;
margin-left: auto;
margin-right: auto;
border-radius: 12px;
background: linear-gradient(135deg, #dbeafe, #cffafe);
font-size: 20px;
margin-bottom: 14px;
}
.metric-title {
color: #64748b;
font-size: 12px;
font-weight: 700;
text-transform: uppercase;
letter-spacing: 0.5px;
}
.metric-value {
color: #1d4ed8;
font-size: 27px;
font-weight: 800;
margin-top: 4px;
}
.metric-description {
color: #94a3b8;
font-size: 11px;
margin-top: 4px;
}

/* ===== GLASS CARD ===== */
.glass-card {
background: linear-gradient(160deg, #ffffff, #f0f5ff);
border: 1px solid #dbeafe;
border-radius: 20px;
padding: 26px;
box-shadow: 0 10px 28px rgba(29, 78, 216, 0.08);
margin-bottom: 22px;
}

/* ===== FORM CONTAINER ===== */
.form-header {
display: flex;
flex-direction: column;
align-items: center;
text-align: center;
gap: 10px;
margin-bottom: 22px;
}
.form-icon {
width: 48px;
height: 48px;
border-radius: 14px;
display: flex;
align-items: center;
justify-content: center;
background: linear-gradient(135deg, #2563eb, #06b6d4);
color: white;
font-size: 22px;
box-shadow: 0 8px 22px rgba(37,99,235,0.28);
}
.form-title {
font-size: 18px;
font-weight: 800;
color: #0f172a;
}
.form-description {
color: #64748b;
font-size: 12px;
}

/* ===== INPUTS ===== */
div[data-baseweb="input"] { border-radius: 10px; }
div[data-baseweb="select"] { border-radius: 10px; }
input { border-radius: 10px !important; }

/* ===== BUTTON ===== */
.stButton > button, .stFormSubmitButton > button {
width: 100%;
border: none;
border-radius: 14px;
padding: 15px 20px;
font-size: 15px;
font-weight: 800;
color: white;
background: linear-gradient(135deg, #1e3a8a, #2563eb, #0891b2);
box-shadow: 0 10px 26px rgba(37,99,235,0.30);
transition: all 0.25s ease;
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
transform: translateY(-2px);
box-shadow: 0 14px 32px rgba(37,99,235,0.40);
color: white;
}

/* ===== PREDICTION CARD ===== */
.prediction-card {
position: relative;
overflow: hidden;
background: linear-gradient(135deg, #1e3a8a, #1d4ed8, #0891b2);
padding: 42px 35px;
border-radius: 26px;
color: white;
text-align: center;
margin-top: 28px;
box-shadow: 0 20px 45px rgba(37,99,235,0.28);
}
.prediction-card.approved {
background: linear-gradient(135deg, #052e16, #16a34a, #059669);
box-shadow: 0 15px 40px rgba(22,163,74,0.30);
}
.prediction-card.rejected {
background: linear-gradient(135deg, #450a0a, #dc2626, #b91c1c);
box-shadow: 0 15px 40px rgba(220,38,38,0.30);
}
.prediction-card .prediction-icon {
font-size: 46px;
margin-bottom: 6px;
}
.prediction-card h2 {
font-size: 30px;
font-weight: 800;
margin-bottom: 8px;
}
.prediction-card p {
color: #e0f2fe;
font-size: 14px;
max-width: 520px;
margin: 0 auto;
line-height: 1.6;
}
.prediction-status {
display: inline-block;
margin-top: 16px;
padding: 8px 18px;
border-radius: 20px;
background: rgba(255,255,255,0.15);
border: 1px solid rgba(255,255,255,0.2);
font-weight: 700;
font-size: 13px;
letter-spacing: 0.4px;
}
.prediction-meta {
display: flex;
justify-content: center;
gap: 26px;
margin-top: 22px;
flex-wrap: wrap;
}
.prediction-meta-item {
background: rgba(255,255,255,0.10);
border: 1px solid rgba(255,255,255,0.15);
border-radius: 12px;
padding: 10px 18px;
min-width: 130px;
}
.prediction-meta-item .label {
font-size: 10px;
text-transform: uppercase;
letter-spacing: 0.5px;
color: #e0f2fe;
opacity: 0.85;
}
.prediction-meta-item .value {
font-size: 16px;
font-weight: 800;
margin-top: 2px;
}

/* ===== INFO BOX ===== */
.info-box {
background: linear-gradient(135deg, #eff6ff, #ecfeff);
border-left: 4px solid #2563eb;
padding: 18px;
border-radius: 12px;
color: #0f172a;
font-size: 13px;
line-height: 1.6;
}

/* ===== MODEL / ABOUT CARDS ===== */
.model-card {
background: linear-gradient(160deg, #ffffff, #f0f5ff);
padding: 26px;
border-radius: 20px;
border: 1px solid #dbeafe;
box-shadow: 0 10px 28px rgba(29, 78, 216, 0.08);
}
.model-card h3 {
text-align: center;
color: #0f172a;
}
.about-card {
background: linear-gradient(160deg, #ffffff, #f0f5ff);
border-radius: 20px;
padding: 30px;
border: 1px solid #dbeafe;
box-shadow: 0 10px 28px rgba(29, 78, 216, 0.08);
line-height: 1.7;
}
.about-card h2 {
font-size: 19px;
font-weight: 800;
color: #0f172a;
margin-bottom: 6px;
}
.about-card p {
color: #475569;
font-size: 14px;
}
.about-card ul {
color: #475569;
font-size: 14px;
margin: 0;
padding-left: 20px;
}
.about-card li {
margin-bottom: 6px;
}
.about-card hr {
border: none;
border-top: 1px solid #e2e8f0;
margin: 22px 0;
}
.tech-badges {
display: flex;
flex-wrap: wrap;
gap: 8px;
margin-top: 10px;
}
.tech-badge {
background: linear-gradient(135deg, #eff6ff, #ecfeff);
border: 1px solid #bfdbfe;
color: #1d4ed8;
font-size: 12px;
font-weight: 700;
padding: 6px 14px;
border-radius: 20px;
}
.steps-list {
counter-reset: step;
list-style: none;
padding-left: 0;
margin: 0;
}
.steps-list li {
counter-increment: step;
position: relative;
padding-left: 38px;
margin-bottom: 14px;
color: #475569;
font-size: 14px;
}
.steps-list li:before {
content: counter(step);
position: absolute;
left: 0;
top: -2px;
width: 26px;
height: 26px;
border-radius: 50%;
background: linear-gradient(135deg, #2563eb, #06b6d4);
color: white;
font-weight: 800;
font-size: 12px;
display: flex;
align-items: center;
justify-content: center;
}

/* ===== FOOTER ===== */
.footer {
text-align: center;
color: #94a3b8;
padding: 35px 10px 15px;
font-size: 12px;
border-top: 1px solid #e2e8f0;
margin-top: 40px;
}
.footer strong {
color: #2563eb;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ==========================================
# REUSABLE COMPONENT HELPERS
# ==========================================

def metric_card(icon: str, title: str, value: str, description: str = "") -> str:
    """Return HTML for a single KPI metric card."""
    return f"""<div class="metric-card">
<div class="metric-icon">{icon}</div>
<div class="metric-title">{title}</div>
<div class="metric-value">{value}</div>
<div class="metric-description">{description}</div>
</div>"""


def glass_card_header(icon: str, title: str, description: str) -> str:
    """Return HTML for a glass-card form header (call st.markdown, then
    add widgets, then close the div manually with '</div>')."""
    return f"""<div class="glass-card">
<div class="form-header">
<div class="form-icon">{icon}</div>
<div>
<div class="form-title">{title}</div>
<div class="form-description">{description}</div>
</div>
</div>"""


def evaluate_loan_application(
    credit_score: int,
    dti: float,
    delinquencies: int,
    employment: str,
    income: float,
    loan_amount: float,
) -> float:
    """Placeholder scoring rule that returns an approval probability (0-1).

    This is NOT the trained Gradient Boosting model — it is a simple,
    transparent stand-in so the form has a working end-to-end result.
    Replace the body of this function with a call to your saved model,
    e.g. `model.predict_proba(features)[0][1]`.
    """
    score = 0.5

    # Credit score contribution
    score += (credit_score - 650) / 600

    # Debt-to-income contribution (lower DTI is better)
    score -= (dti - 20) / 150

    # Delinquency history contribution
    score -= delinquencies * 0.07

    # Employment status contribution
    if employment == "Unemployed":
        score -= 0.20
    elif employment == "Self-employed":
        score -= 0.03

    # Loan-to-income contribution (smaller loans relative to income are safer)
    if income > 0:
        loan_to_income = loan_amount / income
        score -= max(0.0, loan_to_income - 0.3) * 0.4

    return max(0.0, min(1.0, score))


MODEL_METRICS = {
    "Accuracy": "90.28%",
    "Precision": "89.58%",
    "Recall": "99.41%",
    "F1 Score": "94.24%",
    "ROC-AUC": "88.34%",
    "Cross-Validation F1": "94.12%",
}


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:
    st.markdown(
        """<div class="sidebar-logo">
<div class="icon">💳</div>
<h2>LoanPredict AI</h2>
<p>Intelligent Loan Prediction</p>
</div>""",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    page = st.radio(
        "MAIN MENU",
        [
            "🏠 Dashboard",
            "🔮 Loan Prediction",
            "📊 Model Information",
            "ℹ️ About",
        ],
    )

    st.markdown(
        """<div class="sidebar-info">
<div class="sidebar-info-title">🤖 AI MODEL</div>
<div class="sidebar-info-text">
Gradient Boosting Classifier<br><br>
Designed to support intelligent loan repayment prediction.
</div>
</div>""",
        unsafe_allow_html=True,
    )


# ==========================================
# DASHBOARD
# ==========================================

if page == "🏠 Dashboard":

    st.markdown(
        """<div class="main-header">
<h1>💳 Loan Prediction System</h1>
<p>Intelligent machine learning platform for predicting loan repayment outcomes.</p>
<span class="header-badge">● AI MODEL ONLINE</span>
</div>""",
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">📊 System Overview</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Performance overview of the trained Gradient Boosting model.</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(metric_card("🤖", "Model", "GB", "Gradient Boosting"), unsafe_allow_html=True)
    with col2:
        st.markdown(metric_card("🎯", "Accuracy", "90.28%", "Overall prediction accuracy"), unsafe_allow_html=True)
    with col3:
        st.markdown(metric_card("📈", "F1 Score", "94.24%", "Balanced model performance"), unsafe_allow_html=True)
    with col4:
        st.markdown(metric_card("🚀", "ROC-AUC", "88.34%", "Classification capability"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.markdown(
            glass_card_header("🔮", "Loan Prediction", "Predict applicant loan repayment outcome")
            + """<div class="info-box">
Enter applicant financial, credit and personal information to generate an AI-powered prediction.
</div>
</div>""",
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            glass_card_header("🛡️", "Model Status", "Current AI system status")
            + """<div class="info-box">
🟢 <strong>Model Ready</strong><br>
Gradient Boosting Classifier is configured for prediction.
</div>
</div>""",
            unsafe_allow_html=True,
        )


# ==========================================
# LOAN PREDICTION
# ==========================================

elif page == "🔮 Loan Prediction":

    st.markdown(
        """<div class="main-header">
<h1>🔮 Loan Prediction</h1>
<p>Enter applicant information to generate an intelligent loan repayment prediction.</p>
<span class="header-badge">AI-POWERED ASSESSMENT</span>
</div>""",
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">👤 Applicant Information</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Fill in the single form below with accurate applicant information.</div>',
        unsafe_allow_html=True,
    )

    # ==================================================
    # SINGLE UNIFIED APPLICATION FORM
    # ==================================================
    with st.form("loan_application_form", clear_on_submit=False):

        # ---- Personal & financial details ----
        st.markdown(
            glass_card_header(
                "👤", "Personal & Financial Details", "Applicant demographic and financial information"
            ),
            unsafe_allow_html=True,
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.number_input("Age", min_value=18, max_value=100, value=30)
            income = st.number_input("Annual Income", min_value=0.0, value=50000.0, step=1000.0)
            monthly_income = st.number_input("Monthly Income", min_value=0.0, value=4000.0, step=100.0)
            credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
            loan_amount = st.number_input("Loan Amount", min_value=0.0, value=10000.0, step=500.0)

        with col2:
            loan_term = st.number_input("Loan Term (Months)", min_value=1, max_value=120, value=36)
            dti = st.number_input("Debt-to-Income Ratio", min_value=0.0, max_value=100.0, value=20.0)
            interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=100.0, value=10.0)
            installment = st.number_input("Installment", min_value=0.0, value=500.0, step=50.0)
            open_accounts = st.number_input("Open Accounts", min_value=0, max_value=100, value=5)

        with col3:
            credit_limit = st.number_input("Total Credit Limit", min_value=0.0, value=20000.0, step=500.0)
            balance = st.number_input("Current Balance", min_value=0.0, value=5000.0, step=100.0)
            delinquency = st.number_input("Delinquency History", min_value=0, max_value=100, value=0)
            delinquencies = st.number_input("Number of Delinquencies", min_value=0, max_value=100, value=0)
            gender = st.selectbox("Gender", ["Male", "Female"])

        st.markdown("</div>", unsafe_allow_html=True)

        # ---- Loan application details ----
        st.markdown(
            glass_card_header(
                "📋", "Loan Application Details", "Select information related to the loan application"
            ),
            unsafe_allow_html=True,
        )

        col1, col2, col3 = st.columns(3)
        with col1:
            marital = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
        with col2:
            education = st.selectbox("Education Level", ["High School", "Bachelor", "Master", "PhD"])
        with col3:
            employment = st.selectbox("Employment Status", ["Employed", "Self-employed", "Unemployed"])

        col1, col2 = st.columns(2)
        with col1:
            purpose = st.selectbox(
                "Loan Purpose",
                ["Debt Consolidation", "Home", "Education", "Business", "Medical", "Personal"],
            )
        with col2:
            grade = st.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F", "G"])

        st.markdown("</div>", unsafe_allow_html=True)

        # ---- Single submit control for the whole form ----
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🔮  PREDICT LOAN REPAYMENT")

    # ==================================================
    # RESULT (rendered once the single form is submitted)
    # ==================================================
    if submitted:

        approval_probability = evaluate_loan_application(
            credit_score=credit_score,
            dti=dti,
            delinquencies=delinquencies,
            employment=employment,
            income=income,
            loan_amount=loan_amount,
        )

        is_approved = approval_probability >= 0.5

        if is_approved:
            st.markdown(
                f"""<div class="prediction-card approved">
<div class="prediction-icon">🎉</div>
<h2>Congratulations!</h2>
<p>Your loan application has been <strong>APPROVED</strong>.</p>
<div class="prediction-status">APPROVAL CONFIDENCE • {approval_probability * 100:.1f}%</div>
<div class="prediction-meta">
<div class="prediction-meta-item"><div class="label">Loan Amount</div><div class="value">${loan_amount:,.0f}</div></div>
<div class="prediction-meta-item"><div class="label">Credit Score</div><div class="value">{credit_score}</div></div>
<div class="prediction-meta-item"><div class="label">Loan Grade</div><div class="value">{grade}</div></div>
</div>
</div>""",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""<div class="prediction-card rejected">
<div class="prediction-icon">😔</div>
<h2>We are sorry.</h2>
<p>Your loan application has <strong>NOT BEEN APPROVED</strong>.</p>
<div class="prediction-status">APPROVAL CONFIDENCE • {approval_probability * 100:.1f}%</div>
<div class="prediction-meta">
<div class="prediction-meta-item"><div class="label">Loan Amount</div><div class="value">${loan_amount:,.0f}</div></div>
<div class="prediction-meta-item"><div class="label">Credit Score</div><div class="value">{credit_score}</div></div>
<div class="prediction-meta-item"><div class="label">Loan Grade</div><div class="value">{grade}</div></div>
</div>
</div>""",
                unsafe_allow_html=True,
            )

        st.info(
            "This result is generated by a placeholder scoring rule. "
            "Connect your saved Gradient Boosting model in `evaluate_loan_application()` "
            "to produce real predictions."
        )


# ==========================================
# MODEL INFORMATION
# ==========================================

elif page == "📊 Model Information":

    st.markdown(
        """<div class="main-header">
<h1>📊 Model Information</h1>
<p>Performance evaluation of the trained Gradient Boosting classification model.</p>
<span class="header-badge">GRADIENT BOOSTING CLASSIFIER</span>
</div>""",
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">🤖 Model Performance</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(metric_card("🎯", "Accuracy", MODEL_METRICS["Accuracy"]), unsafe_allow_html=True)
    with col2:
        st.markdown(metric_card("⚡", "Precision", MODEL_METRICS["Precision"]), unsafe_allow_html=True)
    with col3:
        st.markdown(metric_card("📈", "Recall", MODEL_METRICS["Recall"]), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(metric_card("🏆", "F1 Score", MODEL_METRICS["F1 Score"]), unsafe_allow_html=True)
    with col2:
        st.markdown(metric_card("🚀", "ROC-AUC", MODEL_METRICS["ROC-AUC"]), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="model-card"><h3>📋 Evaluation Metrics</h3>', unsafe_allow_html=True)

    st.dataframe(
        {
            "Metric": list(MODEL_METRICS.keys()),
            "Score": list(MODEL_METRICS.values()),
        },
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# ABOUT
# ==========================================

elif page == "ℹ️ About":

    st.markdown(
        """<div class="main-header">
<h1>ℹ️ About LoanPredict AI</h1>
<p>Machine Learning Loan Repayment Prediction System</p>
<span class="header-badge">DATA SCIENCE PROJECT</span>
</div>""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """<div class="about-card">

<h2>🎯 System Purpose</h2>
<p>
LoanPredict AI is a machine learning-based decision-support system designed to
predict whether a loan applicant is likely to repay their loan. By analyzing an
applicant's financial history, credit behaviour, and demographic profile, the
system generates an instant, data-driven approval recommendation — helping
lenders assess risk faster and more consistently than manual review alone.
</p>

<hr>

<h2>⚙️ How It Works</h2>
<ol class="steps-list">
<li>The loan officer enters the applicant's personal, financial, and loan
application details into a single guided form.</li>
<li>The system validates and standardizes the inputs (income, credit score,
debt-to-income ratio, delinquency history, and more).</li>
<li>The trained Gradient Boosting model scores the profile and estimates the
probability of successful repayment.</li>
<li>A clear result — <strong>Approved</strong> or <strong>Not Approved</strong>
— is displayed instantly, along with a confidence score.</li>
</ol>

<hr>

<h2>🤖 Machine Learning Model</h2>
<p><strong>Gradient Boosting Classifier</strong></p>
<p>
Gradient Boosting builds an ensemble of decision trees sequentially, where each
new tree corrects the errors of the previous ones. This makes it especially
effective at capturing non-linear relationships between financial variables —
such as how credit score, debt-to-income ratio, and delinquency history
interact to influence repayment risk. It was selected for this project based
on its strong, well-balanced performance across all evaluated metrics.
</p>

<hr>

<h2>📈 Model Performance</h2>
<ul>
<li>Accuracy: <strong>90.28%</strong></li>
<li>Precision: <strong>89.58%</strong></li>
<li>Recall: <strong>99.41%</strong></li>
<li>F1 Score: <strong>94.24%</strong></li>
<li>ROC-AUC: <strong>88.34%</strong></li>
<li>Cross-validation F1: <strong>94.12%</strong></li>
</ul>

<hr>

<h2>🧾 Key Features</h2>
<ul>
<li>Single unified application form for fast, error-free data entry</li>
<li>Instant, easy-to-read approval / rejection result with a confidence score</li>
<li>Dashboard overview of model health and system status</li>
<li>Transparent, documented model performance metrics</li>
</ul>

<hr>

<h2>🛠 Technologies</h2>
<div class="tech-badges">
<span class="tech-badge">Python</span>
<span class="tech-badge">Pandas</span>
<span class="tech-badge">NumPy</span>
<span class="tech-badge">Scikit-learn</span>
<span class="tech-badge">Streamlit</span>
<span class="tech-badge">Gradient Boosting</span>
</div>

<hr>

<h2>👤 Project</h2>
<p>
Developed as a data science project to demonstrate an end-to-end machine
learning workflow — from data preparation and model training to deployment
in an interactive, production-style web interface.
</p>

</div>""",
        unsafe_allow_html=True,
    )


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    """<div class="footer">
<strong>LoanPredict AI</strong> • Machine Learning Loan Prediction System<br>
Built with Python & Streamlit
</div>""",
    unsafe_allow_html=True,
)
