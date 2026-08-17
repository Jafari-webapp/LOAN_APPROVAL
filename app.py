# ============================================================
# LOANPREDICT AI
# LOAN REPAYMENT PREDICTION SYSTEM
# Streamlit + Gradient Boosting
# ============================================================

import os
import joblib
import pandas as pd
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="LoanPredict AI",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

CUSTOM_CSS = """
<style>

.stApp {
    background:
        radial-gradient(
            circle at top right,
            rgba(37, 99, 235, 0.08),
            transparent 35%
        ),
        #f5f7fb;
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}


/* =========================================================
   SIDEBAR
   ========================================================= */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #07111f 0%,
        #0f172a 45%,
        #172554 100%
    );

    border-right: 1px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.sidebar-logo {
    text-align: center;
    padding: 10px 5px 20px;
}

.sidebar-logo .icon {
    width: 68px;
    height: 68px;
    margin: auto;

    border-radius: 18px;

    display: flex;
    align-items: center;
    justify-content: center;

    background: linear-gradient(
        135deg,
        #2563eb,
        #06b6d4
    );

    font-size: 32px;

    box-shadow:
        0 10px 30px
        rgba(37, 99, 235, 0.35);
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

    border: 1px solid
        rgba(255,255,255,0.08);

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


/* =========================================================
   MAIN HEADER
   ========================================================= */

.main-header {
    position: relative;
    overflow: hidden;

    background: linear-gradient(
        135deg,
        #07111f 0%,
        #172554 45%,
        #1d4ed8 100%
    );

    padding: 32px 35px;

    border-radius: 22px;

    color: white;

    margin-bottom: 28px;

    box-shadow:
        0 15px 40px
        rgba(15, 23, 42, 0.18);
}

.main-header:after {
    content: "";

    position: absolute;

    width: 240px;
    height: 240px;

    right: -70px;
    top: -90px;

    border-radius: 50%;

    background:
        rgba(6, 182, 212, 0.18);
}

.main-header h1 {
    position: relative;
    z-index: 2;

    margin: 0;

    font-size: 36px;
    font-weight: 800;
}

.main-header p {
    position: relative;
    z-index: 2;

    margin-top: 8px;

    color: #bfdbfe;

    font-size: 15px;
}

.header-badge {
    position: relative;
    z-index: 2;

    display: inline-block;

    margin-top: 15px;

    padding: 7px 13px;

    border-radius: 20px;

    background:
        rgba(255,255,255,0.10);

    border: 1px solid
        rgba(255,255,255,0.15);

    font-size: 12px;

    color: #e0f2fe;
}


/* =========================================================
   SECTION TITLES
   ========================================================= */

.section-title {
    color: #0f172a;

    font-size: 22px;

    font-weight: 800;

    margin-top: 10px;
    margin-bottom: 18px;
}

.section-subtitle {
    color: #64748b;

    font-size: 13px;

    margin-top: -12px;
    margin-bottom: 20px;
}


/* =========================================================
   KPI CARDS
   ========================================================= */

.metric-card {
    position: relative;
    overflow: hidden;

    background:
        rgba(255,255,255,0.95);

    padding: 22px;

    min-height: 145px;

    border-radius: 18px;

    border: 1px solid
        rgba(226,232,240,0.9);

    box-shadow:
        0 8px 25px
        rgba(15,23,42,0.06);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}

.metric-card:hover {
    transform: translateY(-4px);

    box-shadow:
        0 14px 35px
        rgba(15,23,42,0.11);
}

.metric-icon {
    width: 43px;
    height: 43px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 12px;

    background:
        linear-gradient(
            135deg,
            #dbeafe,
            #cffafe
        );

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
    color: #0f172a;

    font-size: 27px;

    font-weight: 800;

    margin-top: 4px;
}

.metric-description {
    color: #94a3b8;

    font-size: 11px;

    margin-top: 4px;
}


/* =========================================================
   CARDS
   ========================================================= */

.glass-card {
    background:
        rgba(255,255,255,0.95);

    border:
        1px solid rgba(226,232,240,0.9);

    border-radius: 18px;

    padding: 25px;

    box-shadow:
        0 8px 25px
        rgba(15,23,42,0.06);

    margin-bottom: 20px;
}

.model-card {
    background: white;

    padding: 25px;

    border-radius: 18px;

    border:
        1px solid #e2e8f0;

    box-shadow:
        0 8px 25px
        rgba(15,23,42,0.06);
}

.about-card {
    background: white;

    border-radius: 18px;

    padding: 28px;

    border:
        1px solid #e2e8f0;

    box-shadow:
        0 8px 25px
        rgba(15,23,42,0.06);

    line-height: 1.7;
}


/* =========================================================
   FORM HEADER
   ========================================================= */

.form-header {
    display: flex;

    align-items: center;

    gap: 12px;

    margin-bottom: 20px;
}

.form-icon {
    width: 45px;
    height: 45px;

    border-radius: 12px;

    display: flex;

    align-items: center;
    justify-content: center;

    background:
        linear-gradient(
            135deg,
            #2563eb,
            #06b6d4
        );

    color: white;

    font-size: 21px;

    box-shadow:
        0 7px 20px
        rgba(37,99,235,0.25);
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


/* =========================================================
   INPUTS
   ========================================================= */

div[data-baseweb="input"] {
    border-radius: 10px;
}

div[data-baseweb="select"] {
    border-radius: 10px;
}

input {
    border-radius: 10px !important;
}


/* =========================================================
   BUTTON
   ========================================================= */

.stButton > button {
    width: 100%;

    border: none;

    border-radius: 12px;

    padding: 14px 20px;

    font-size: 15px;

    font-weight: 800;

    color: white;

    background:
        linear-gradient(
            135deg,
            #1d4ed8,
            #2563eb,
            #0891b2
        );

    box-shadow:
        0 8px 20px
        rgba(37,99,235,0.25);

    transition:
        all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 12px 28px
        rgba(37,99,235,0.35);

    color: white;
}


/* =========================================================
   PREDICTION CARD
   ========================================================= */

.prediction-card {
    position: relative;

    overflow: hidden;

    background:
        linear-gradient(
            135deg,
            #0f172a,
            #1d4ed8,
            #0891b2
        );

    padding: 35px;

    border-radius: 22px;

    color: white;

    text-align: center;

    margin-top: 25px;

    box-shadow:
        0 15px 40px
        rgba(37,99,235,0.25);
}

.prediction-card h2 {
    font-size: 30px;

    font-weight: 800;

    margin-bottom: 8px;
}

.prediction-card p {
    color: #dbeafe;

    font-size: 14px;
}

.prediction-status {
    display: inline-block;

    margin-top: 10px;

    padding: 8px 18px;

    border-radius: 20px;

    background:
        rgba(255,255,255,0.12);

    border:
        1px solid
        rgba(255,255,255,0.15);

    font-weight: 700;

    font-size: 13px;
}


/* =========================================================
   RESULT
   ========================================================= */

.result-approved {
    background:
        linear-gradient(
            135deg,
            #064e3b,
            #059669
        );

    padding: 35px;

    border-radius: 22px;

    color: white;

    text-align: center;

    margin-top: 25px;

    box-shadow:
        0 15px 40px
        rgba(5,150,105,0.25);
}

.result-rejected {
    background:
        linear-gradient(
            135deg,
            #7f1d1d,
            #dc2626
        );

    padding: 35px;

    border-radius: 22px;

    color: white;

    text-align: center;

    margin-top: 25px;

    box-shadow:
        0 15px 40px
        rgba(220,38,38,0.25);
}

.result-title {
    font-size: 30px;

    font-weight: 800;

    margin-bottom: 8px;
}

.result-probability {
    font-size: 17px;

    margin-top: 15px;
}


/* =========================================================
   INFO BOX
   ========================================================= */

.info-box {
    background:
        linear-gradient(
            135deg,
            #eff6ff,
            #ecfeff
        );

    border-left:
        4px solid #2563eb;

    padding: 18px;

    border-radius: 12px;

    color: #334155;

    font-size: 13px;

    line-height: 1.6;
}


/* =========================================================
   STATUS
   ========================================================= */

.status-online {
    display: inline-block;

    padding: 6px 12px;

    border-radius: 20px;

    background: #dcfce7;

    color: #166534;

    font-size: 12px;

    font-weight: 700;
}

.status-offline {
    display: inline-block;

    padding: 6px 12px;

    border-radius: 20px;

    background: #fee2e2;

    color: #991b1b;

    font-size: 12px;

    font-weight: 700;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    text-align: center;

    color: #94a3b8;

    padding:
        35px 10px 15px;

    font-size: 12px;

    border-top:
        1px solid #e2e8f0;

    margin-top: 40px;
}

.footer strong {
    color: #2563eb;
}

</style>
"""

st.markdown(
    CUSTOM_CSS,
    unsafe_allow_html=True
)


# ============================================================
# MODEL FILES
# ============================================================

MODEL_PATH = "gradient_boosting_model.pkl"
PREPROCESSOR_PATH = "preprocessor.pkl"
FEATURES_PATH = "selected_features.pkl"
INDICES_PATH = "selected_indices.pkl"


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model_files():

    model = None
    preprocessor = None
    selected_features = None
    selected_indices = None

    errors = []

    # ---------------- MODEL ----------------

    if os.path.exists(MODEL_PATH):

        try:
            model = joblib.load(MODEL_PATH)

        except Exception as e:
            errors.append(
                f"Model loading error: {e}"
            )

    else:

        errors.append(
            f"{MODEL_PATH} not found"
        )

    # ---------------- PREPROCESSOR ----------------

    if os.path.exists(PREPROCESSOR_PATH):

        try:
            preprocessor = joblib.load(
                PREPROCESSOR_PATH
            )

        except Exception as e:

            errors.append(
                f"Preprocessor loading error: {e}"
            )

    else:

        errors.append(
            f"{PREPROCESSOR_PATH} not found"
        )

    # ---------------- SELECTED FEATURES ----------------

    if os.path.exists(FEATURES_PATH):

        try:

            selected_features = joblib.load(
                FEATURES_PATH
            )

        except Exception:

            selected_features = None

    # ---------------- SELECTED INDICES ----------------

    if os.path.exists(INDICES_PATH):

        try:

            selected_indices = joblib.load(
                INDICES_PATH
            )

        except Exception:

            selected_indices = None

    return (
        model,
        preprocessor,
        selected_features,
        selected_indices,
        errors
    )


(
    model,
    preprocessor,
    selected_features,
    selected_indices,
    load_errors
) = load_model_files()


MODEL_READY = (
    model is not None
    and preprocessor is not None
)


# ============================================================
# MODEL METRICS
# ============================================================

MODEL_METRICS = {

    "Accuracy": "90.28%",

    "Precision": "89.58%",

    "Recall": "99.41%",

    "F1 Score": "94.24%",

    "ROC-AUC": "88.34%",

    "Cross-Validation F1": "94.12%"
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def metric_card(
    icon,
    title,
    value,
    description=""
):

    return f"""
    <div class="metric-card">

        <div class="metric-icon">
            {icon}
        </div>

        <div class="metric-title">
            {title}
        </div>

        <div class="metric-value">
            {value}
        </div>

        <div class="metric-description">
            {description}
        </div>

    </div>
    """


def page_header(
    title,
    description,
    badge
):

    st.markdown(
        f"""
        <div class="main-header">

            <h1>{title}</h1>

            <p>{description}</p>

            <span class="header-badge">
                {badge}
            </span>

        </div>
        """,
        unsafe_allow_html=True
    )


def form_header(
    icon,
    title,
    description
):

    st.markdown(
        f"""
        <div class="glass-card">

            <div class="form-header">

                <div class="form-icon">
                    {icon}
                </div>

                <div>

                    <div class="form-title">
                        {title}
                    </div>

                    <div class="form-description">
                        {description}
                    </div>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-logo">

            <div class="icon">
                💳
            </div>

            <h2>
                LoanPredict AI
            </h2>

            <p>
                Intelligent Loan Prediction
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    page = st.radio(
        "MAIN MENU",
        [
            "🏠 Dashboard",
            "🔮 Loan Prediction",
            "📊 Model Information",
            "ℹ️ About"
        ]
    )

    st.markdown("---")

    if MODEL_READY:

        st.markdown(
            """
            <span class="status-online">
                🟢 MODEL ONLINE
            </span>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <span class="status-offline">
                🔴 MODEL OFFLINE
            </span>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="sidebar-info">

            <div class="sidebar-info-title">
                🤖 AI MODEL
            </div>

            <div class="sidebar-info-text">

                Gradient Boosting Classifier

                <br><br>

                Machine learning system
                designed to support
                intelligent loan repayment
                prediction.

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    page_header(
        "💳 Loan Prediction System",
        "Intelligent machine learning platform for predicting loan repayment outcomes.",
        "● AI MODEL ONLINE"
    )

    st.markdown(
        '<div class="section-title">📊 System Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-subtitle">
            Performance overview of the trained Gradient Boosting model.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(
            metric_card(
                "🤖",
                "Model",
                "GB",
                "Gradient Boosting"
            ),
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            metric_card(
                "🎯",
                "Accuracy",
                "90.28%",
                "Overall prediction accuracy"
            ),
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            metric_card(
                "📈",
                "F1 Score",
                "94.24%",
                "Balanced model performance"
            ),
            unsafe_allow_html=True
        )

    with col4:

        st.markdown(
            metric_card(
                "🚀",
                "ROC-AUC",
                "88.34%",
                "Classification capability"
            ),
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="glass-card">

                <div class="form-header">

                    <div class="form-icon">
                        🔮
                    </div>

                    <div>

                        <div class="form-title">
                            Loan Prediction
                        </div>

                        <div class="form-description">
                            Predict applicant loan repayment outcome
                        </div>

                    </div>

                </div>

                <div class="info-box">

                    Enter applicant financial,
                    credit and personal information
                    to generate an AI-powered prediction.

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        status_text = (
            "🟢 Model Ready"
            if MODEL_READY
            else "🔴 Model Files Missing"
        )

        st.markdown(
            f"""
            <div class="glass-card">

                <div class="form-header">

                    <div class="form-icon">
                        🛡️
                    </div>

                    <div>

                        <div class="form-title">
                            Model Status
                        </div>

                        <div class="form-description">
                            Current AI system status
                        </div>

                    </div>

                </div>

                <div class="info-box">

                    <strong>
                        {status_text}
                    </strong>

                    <br><br>

                    Gradient Boosting Classifier
                    is configured for prediction.

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # ---------------- MODEL FILE STATUS ----------------

    st.markdown(
        '<div class="section-title">📁 Model Files</div>',
        unsafe_allow_html=True
    )

    file_col1, file_col2, file_col3, file_col4 = st.columns(4)

    files_status = [
        (
            MODEL_PATH,
            model is not None
        ),
        (
            PREPROCESSOR_PATH,
            preprocessor is not None
        ),
        (
            FEATURES_PATH,
            selected_features is not None
        ),
        (
            INDICES_PATH,
            selected_indices is not None
        )
    ]

    for column, (filename, exists) in zip(
        [
            file_col1,
            file_col2,
            file_col3,
            file_col4
        ],
        files_status
    ):

        with column:

            if exists:

                st.success(
                    f"✓ {filename}"
                )

            else:

                st.warning(
                    f"○ {filename}"
                )


# ============================================================
# LOAN PREDICTION
# ============================================================

elif page == "🔮 Loan Prediction":

    page_header(
        "🔮 Loan Prediction",
        "Enter applicant information to generate an intelligent loan repayment prediction.",
        "AI-POWERED ASSESSMENT"
    )

    st.markdown(
        '<div class="section-title">👤 Applicant Information</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-subtitle">
            Provide accurate applicant information for better predictions.
        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # PERSONAL INFORMATION
    # ========================================================

    st.markdown(
        """
        <div class="glass-card">

            <div class="form-header">

                <div class="form-icon">
                    👤
                </div>

                <div>

                    <div class="form-title">
                        Personal & Financial Details
                    </div>

                    <div class="form-description">
                        Applicant demographic and financial information
                    </div>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=30
        )

        income = st.number_input(
            "Annual Income",
            min_value=0.0,
            value=50000.0,
            step=1000.0
        )

        monthly_income = st.number_input(
            "Monthly Income",
            min_value=0.0,
            value=4000.0,
            step=100.0
        )

        credit_score = st.number_input(
            "Credit Score",
            min_value=300,
            max_value=850,
            value=650
        )

        loan_amount = st.number_input(
            "Loan Amount",
            min_value=0.0,
            value=10000.0,
            step=500.0
        )

    with col2:

        loan_term = st.number_input(
            "Loan Term (Months)",
            min_value=1,
            max_value=120,
            value=36
        )

        dti = st.number_input(
            "Debt-to-Income Ratio",
            min_value=0.0,
            max_value=100.0,
            value=20.0
        )

        interest_rate = st.number_input(
            "Interest Rate (%)",
            min_value=0.0,
            max_value=100.0,
            value=10.0
        )

        installment = st.number_input(
            "Installment",
            min_value=0.0,
            value=500.0,
            step=50.0
        )

        open_accounts = st.number_input(
            "Open Accounts",
            min_value=0,
            max_value=100,
            value=5
        )

    with col3:

        credit_limit = st.number_input(
            "Total Credit Limit",
            min_value=0.0,
            value=20000.0,
            step=500.0
        )

        balance = st.number_input(
            "Current Balance",
            min_value=0.0,
            value=5000.0,
            step=100.0
        )

        delinquency = st.number_input(
            "Delinquency History",
            min_value=0,
            max_value=100,
            value=0
        )

        delinquencies = st.number_input(
            "Number of Delinquencies",
            min_value=0,
            max_value=100,
            value=0
        )

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female"
            ]
        )

    # ========================================================
    # LOAN DETAILS
    # ========================================================

    st.markdown(
        """
        <div class="glass-card">

            <div class="form-header">

                <div class="form-icon">
                    📋
                </div>

                <div>

                    <div class="form-title">
                        Loan Application Details
                    </div>

                    <div class="form-description">
                        Information related to the loan application
                    </div>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        marital = st.selectbox(
            "Marital Status",
            [
                "Single",
                "Married",
                "Divorced",
                "Widowed"
            ]
        )

    with col2:

        education = st.selectbox(
            "Education Level",
            [
                "High School",
                "Bachelor",
                "Master",
                "PhD"
            ]
        )

    with col3:

        employment = st.selectbox(
            "Employment Status",
            [
                "Employed",
                "Self-employed",
                "Unemployed"
            ]
        )

    col1, col2 = st.columns(2)

    with col1:

        purpose = st.selectbox(
            "Loan Purpose",
            [
                "Debt Consolidation",
                "Home",
                "Education",
                "Business",
                "Medical",
                "Personal"
            ]
        )

    with col2:

        grade = st.selectbox(
            "Loan Grade",
            [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G"
            ]
        )

    # ========================================================
    # PREDICTION
    # ========================================================

    st.markdown("<br>", unsafe_allow_html=True)

    predict_button = st.button(
        "🔮  PREDICT LOAN REPAYMENT"
    )

    if predict_button:

        if not MODEL_READY:

            st.error(
                "❌ Model files are not ready. "
                "Please make sure gradient_boosting_model.pkl "
                "and preprocessor.pkl are inside the project folder."
            )

        else:

            try:

                # ====================================================
                # CREATE INPUT DATA
                # ====================================================

                input_data = pd.DataFrame({

                    "age": [age],

                    "income": [income],

                    "monthly_income": [
                        monthly_income
                    ],

                    "credit_score": [
                        credit_score
                    ],

                    "loan_amount": [
                        loan_amount
                    ],

                    "loan_term": [
                        loan_term
                    ],

                    "dti": [dti],

                    "interest_rate": [
                        interest_rate
                    ],

                    "installment": [
                        installment
                    ],

                    "open_accounts": [
                        open_accounts
                    ],

                    "credit_limit": [
                        credit_limit
                    ],

                    "balance": [
                        balance
                    ],

                    "delinquency": [
                        delinquency
                    ],

                    "delinquencies": [
                        delinquencies
                    ],

                    "gender": [
                        gender
                    ],

                    "marital": [
                        marital
                    ],

                    "education": [
                        education
                    ],

                    "employment": [
                        employment
                    ],

                    "purpose": [
                        purpose
                    ],

                    "grade": [
                        grade
                    ]
                })


                # ====================================================
                # USE SELECTED FEATURES IF AVAILABLE
                # ====================================================

                if (
                    selected_features is not None
                    and hasattr(
                        selected_features,
                        "__iter__"
                    )
                ):

                    available_features = [
                        feature
                        for feature in selected_features
                        if feature in input_data.columns
                    ]

                    if len(available_features) > 0:

                        input_data = input_data[
                            available_features
                        ]


                # ====================================================
                # PREPROCESS
                # ====================================================

                processed_data = preprocessor.transform(
                    input_data
                )


                # ====================================================
                # SELECT INDICES IF AVAILABLE
                # ====================================================

                if selected_indices is not None:

                    try:

                        processed_data = processed_data[
                            :,
                            selected_indices
                        ]

                    except Exception:

                        pass


                # ====================================================
                # PREDICTION
                # ====================================================

                prediction = model.predict(
                    processed_data
                )

                prediction_value = prediction[0]


                # ====================================================
                # PROBABILITY
                # ====================================================

                probability = None

                if hasattr(
                    model,
                    "predict_proba"
                ):

                    probabilities = model.predict_proba(
                        processed_data
                    )

                    probability = (
                        max(probabilities[0])
                        * 100
                    )


                # ====================================================
                # RESULT
                # ====================================================

                prediction_text = str(
                    prediction_value
                ).lower()


                approved_values = [
                    "1",
                    "yes",
                    "approved",
                    "approve",
                    "paid",
                    "repaid",
                    "good",
                    "true"
                ]


                is_approved = (
                    prediction_text
                    in approved_values
                )


                # ====================================================
                # DISPLAY RESULT
                # ====================================================

                if is_approved:

                    probability_text = ""

                    if probability is not None:

                        probability_text = (
                            f"""
                            <div class="result-probability">
                                Prediction Confidence:
                                <strong>
                                    {probability:.2f}%
                                </strong>
                            </div>
                            """
                        )

                    st.markdown(
                        f"""
                        <div class="result-approved">

                            <div class="result-title">
                                ✅ LOAN REPAYMENT PREDICTED
                            </div>

                            <p>
                                The model predicts a
                                positive loan repayment outcome.
                            </p>

                            {probability_text}

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                else:

                    probability_text = ""

                    if probability is not None:

                        probability_text = (
                            f"""
                            <div class="result-probability">
                                Prediction Confidence:
                                <strong>
                                    {probability:.2f}%
                                </strong>
                            </div>
                            """
                        )

                    st.markdown(
                        f"""
                        <div class="result-rejected">

                            <div class="result-title">
                                ❌ LOAN REPAYMENT NOT PREDICTED
                            </div>

                            <p>
                                The model predicts a
                                negative loan repayment outcome.
                            </p>

                            {probability_text}

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                # ====================================================
                # SHOW INPUT SUMMARY
                # ====================================================

                st.markdown("<br>", unsafe_allow_html=True)

                with st.expander(
                    "📋 View Submitted Application Data"
                ):

                    st.dataframe(
                        input_data,
                        use_container_width=True,
                        hide_index=True
                    )


            except Exception as e:

                st.error(
                    "❌ Prediction Error"
                )

                st.warning(
                    "The model was loaded, but the input "
                    "columns/types do not match the format "
                    "used during training."
                )

                with st.expander(
                    "🔧 Technical Error"
                ):

                    st.code(
                        str(e)
                    )


# ============================================================
# MODEL INFORMATION
# ============================================================

elif page == "📊 Model Information":

    page_header(
        "📊 Model Information",
        "Performance evaluation of the trained Gradient Boosting classification model.",
        "GRADIENT BOOSTING CLASSIFIER"
    )

    st.markdown(
        '<div class="section-title">🤖 Model Performance</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            metric_card(
                "🎯",
                "Accuracy",
                MODEL_METRICS["Accuracy"],
                "Overall correctness"
            ),
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            metric_card(
                "⚡",
                "Precision",
                MODEL_METRICS["Precision"],
                "Positive prediction accuracy"
            ),
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            metric_card(
                "📈",
                "Recall",
                MODEL_METRICS["Recall"],
                "Detection capability"
            ),
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            metric_card(
                "🏆",
                "F1 Score",
                MODEL_METRICS["F1 Score"],
                "Balanced performance"
            ),
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            metric_card(
                "🚀",
                "ROC-AUC",
                MODEL_METRICS["ROC-AUC"],
                "Classification capability"
            ),
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            metric_card(
                "🔄",
                "CV F1",
                MODEL_METRICS["Cross-Validation F1"],
                "Cross-validation score"
            ),
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="model-card">

            <h3>
                📋 Evaluation Metrics
            </h3>

        </div>
        """,
        unsafe_allow_html=True
    )

    metrics_df = pd.DataFrame({
        "Metric": list(
            MODEL_METRICS.keys()
        ),

        "Score": list(
            MODEL_METRICS.values()
        )
    })

    st.dataframe(
        metrics_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.info(
        "The Gradient Boosting Classifier was selected "
        "because it achieved strong overall classification "
        "performance, including an F1 Score of 94.24%."
    )


# ============================================================
# ABOUT
# ============================================================

elif page == "ℹ️ About":

    page_header(
        "ℹ️ About LoanPredict AI",
        "Machine Learning Loan Repayment Prediction System",
        "DATA SCIENCE PROJECT"
    )

    st.markdown(
        """
        <div class="about-card">

            <h2>
                🎯 System Purpose
            </h2>

            <p>
                LoanPredict AI is a machine learning-based
                system designed to predict whether a loan
                applicant is likely to repay their loan.
            </p>

            <hr>

            <h2>
                🤖 Machine Learning Model
            </h2>

            <p>
                <strong>
                    Gradient Boosting Classifier
                </strong>
            </p>

            <p>
                The Gradient Boosting algorithm was selected
                based on its strong classification performance
                across the evaluated metrics.
            </p>

            <hr>

            <h2>
                📈 Model Performance
            </h2>

            <ul>

                <li>
                    Accuracy:
                    <strong>90.28%</strong>
                </li>

                <li>
                    Precision:
                    <strong>89.58%</strong>
                </li>

                <li>
                    Recall:
                    <strong>99.41%</strong>
                </li>

                <li>
                    F1 Score:
                    <strong>94.24%</strong>
                </li>

                <li>
                    ROC-AUC:
                    <strong>88.34%</strong>
                </li>

                <li>
                    Cross-validation F1:
                    <strong>94.12%</strong>
                </li>

            </ul>

            <hr>

            <h2>
                🛠 Technologies
            </h2>

            <p>
                Python • Pandas • NumPy • Scikit-learn •
                Joblib • Streamlit • Gradient Boosting
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        <strong>
            LoanPredict AI
        </strong>

        • Machine Learning Loan Prediction System

        <br>

        Built with Python & Streamlit

    </div>
    """,
    unsafe_allow_html=True
)
