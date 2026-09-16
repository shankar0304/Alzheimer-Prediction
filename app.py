import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AlzheimerAI | Cognitive Health Screening",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==================================================
# MODERN 2026 AI INTERFACE
# ==================================================

st.markdown(
    r"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --bg: #07111f;
        --panel: #0d1b2e;
        --panel2: #12233a;
        --border: rgba(148,163,184,.18);
        --text: #eef6ff;
        --muted: #9fb0c3;
        --cyan: #6ee7f9;
        --purple: #a78bfa;
        --green: #34d399;
        --red: #fb7185;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 10% 5%, rgba(34,211,238,.10), transparent 27%),
            radial-gradient(circle at 90% 12%, rgba(139,92,246,.12), transparent 30%),
            radial-gradient(circle at 50% 100%, rgba(59,130,246,.07), transparent 35%),
            var(--bg);
        color: var(--text);
    }

    [data-testid="stHeader"] {
        background: rgba(7,17,31,.72);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #081322, #060f1d);
        border-right: 1px solid var(--border);
    }

    [data-testid="stSidebar"] * {
        color: #dbeafe;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 1.8rem;
        padding-bottom: 3rem;
    }

    .hero {
        position: relative;
        overflow: hidden;
        padding: 32px 36px;
        border: 1px solid rgba(110,231,249,.18);
        border-radius: 28px;
        background:
            linear-gradient(135deg, rgba(17,37,61,.94), rgba(12,24,43,.82));
        box-shadow: 0 24px 70px rgba(0,0,0,.28);
        margin-bottom: 26px;
    }

    .hero::after {
        content: "";
        position: absolute;
        width: 240px;
        height: 240px;
        right: -75px;
        top: -90px;
        border-radius: 50%;
        background: rgba(110,231,249,.07);
        filter: blur(7px);
    }

    .eyebrow {
        color: var(--cyan);
        font-size: .74rem;
        font-weight: 800;
        letter-spacing: .17em;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .hero-title {
        font-size: clamp(2.1rem, 4vw, 3.7rem);
        line-height: 1.04;
        font-weight: 800;
        letter-spacing: -.045em;
        margin: 0;
        color: #f8fbff;
    }

    .hero-title span {
        background: linear-gradient(90deg, #dffbff, #6ee7f9, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        color: var(--muted);
        font-size: 1rem;
        line-height: 1.7;
        max-width: 900px;
        margin: 14px 0 0;
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        margin-top: 20px;
        padding: 8px 13px;
        border-radius: 999px;
        border: 1px solid rgba(52,211,153,.20);
        background: rgba(52,211,153,.08);
        color: #a7f3d0;
        font-size: .77rem;
        font-weight: 700;
    }

    .status-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: var(--green);
        box-shadow: 0 0 12px rgba(52,211,153,.9);
    }

    .section-title {
        font-size: 1.55rem;
        font-weight: 800;
        letter-spacing: -.025em;
        color: #f8fbff;
        margin: 8px 0 4px;
    }

    .section-subtitle {
        color: var(--muted);
        margin-bottom: 20px;
        line-height: 1.6;
    }

    .glass-card {
        border: 1px solid var(--border);
        background: linear-gradient(145deg, rgba(20,37,60,.84), rgba(12,24,42,.74));
        border-radius: 22px;
        padding: 22px;
        box-shadow: 0 16px 50px rgba(0,0,0,.18);
        margin-bottom: 18px;
    }

    .metric-card {
        border: 1px solid var(--border);
        background: linear-gradient(145deg, rgba(19,36,59,.82), rgba(11,24,42,.76));
        border-radius: 20px;
        padding: 19px;
        min-height: 112px;
        box-shadow: 0 12px 35px rgba(0,0,0,.12);
    }

    .mini-label {
        color: #8ea5bb;
        font-size: .73rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: .12em;
    }

    .mini-value {
        color: #f8fbff;
        font-size: 1.34rem;
        font-weight: 800;
        margin-top: 6px;
    }

    .metric-number {
        font-size: 1.8rem;
        font-weight: 800;
        color: #f8fbff;
        margin-top: 5px;
    }

    .metric-caption {
        color: #8ea5bb;
        font-size: .79rem;
        margin-top: 3px;
    }

    .feature-chip {
        display: inline-block;
        margin: 5px 5px 0 0;
        padding: 8px 11px;
        border-radius: 12px;
        background: rgba(110,231,249,.07);
        border: 1px solid rgba(110,231,249,.13);
        color: #c8f8ff;
        font-size: .77rem;
        font-weight: 600;
    }

    .result-card {
        border-radius: 26px;
        padding: 28px;
        margin-top: 22px;
        border: 1px solid rgba(110,231,249,.18);
        background: linear-gradient(145deg, rgba(20,37,60,.92), rgba(10,24,43,.88));
        box-shadow: 0 24px 65px rgba(0,0,0,.25);
    }

    .result-card.diagnosis {
        border-color: rgba(251,113,133,.28);
        background: linear-gradient(145deg, rgba(70,25,45,.56), rgba(20,24,43,.92));
    }

    .result-card.clear {
        border-color: rgba(52,211,153,.23);
        background: linear-gradient(145deg, rgba(12,55,55,.48), rgba(10,29,43,.92));
    }

    .result-kicker {
        color: #8ea5bb;
        font-size: .75rem;
        text-transform: uppercase;
        letter-spacing: .14em;
        font-weight: 800;
    }

    .result-title {
        font-size: 2rem;
        font-weight: 800;
        margin: 8px 0 4px;
        color: #fff;
    }

    .result-note {
        color: #aebdcb;
        line-height: 1.6;
        margin: 0;
    }

    .gauge-wrap {
        width: 205px;
        height: 205px;
        border-radius: 50%;
        display: grid;
        place-items: center;
        margin: 0 auto;
        background:
            conic-gradient(#6ee7f9 0deg, #a78bfa var(--gauge-angle), rgba(148,163,184,.12) var(--gauge-angle), rgba(148,163,184,.12) 360deg);
        position: relative;
        box-shadow: 0 0 45px rgba(110,231,249,.08);
    }

    .gauge-wrap::before {
        content: "";
        position: absolute;
        inset: 12px;
        border-radius: 50%;
        background: #091727;
        border: 1px solid rgba(148,163,184,.13);
    }

    .gauge-content {
        position: relative;
        z-index: 1;
        text-align: center;
    }

    .gauge-value {
        font-size: 2.35rem;
        font-weight: 800;
        color: #f8fbff;
        letter-spacing: -.04em;
    }

    .gauge-label {
        color: #8ea5bb;
        font-size: .73rem;
        text-transform: uppercase;
        letter-spacing: .1em;
        font-weight: 700;
    }

    .meter {
        height: 10px;
        border-radius: 999px;
        overflow: hidden;
        background: rgba(148,163,184,.14);
        margin-top: 12px;
    }

    .meter-fill {
        height: 100%;
        border-radius: 999px;
        background: linear-gradient(90deg, #22d3ee, #8b5cf6);
    }

    .history-row {
        padding: 13px 0;
        border-bottom: 1px solid rgba(148,163,184,.10);
    }

    .history-row:last-child {
        border-bottom: none;
    }

    .history-time {
        color: #7f95aa;
        font-size: .72rem;
    }

    .history-result {
        color: #f1f5f9;
        font-weight: 700;
        margin-top: 3px;
    }

    .workflow-step {
        display: flex;
        gap: 14px;
        align-items: flex-start;
        padding: 15px 0;
        border-bottom: 1px solid rgba(148,163,184,.10);
    }

    .workflow-step:last-child {
        border-bottom: none;
    }

    .step-number {
        min-width: 34px;
        height: 34px;
        display: grid;
        place-items: center;
        border-radius: 11px;
        background: rgba(110,231,249,.08);
        border: 1px solid rgba(110,231,249,.13);
        color: #a5f3fc;
        font-weight: 800;
    }

    .step-text strong {
        color: #f1f5f9;
    }

    .step-text span {
        display: block;
        color: #8ea5bb;
        font-size: .83rem;
        margin-top: 3px;
    }

    .sidebar-brand {
        padding: 8px 4px 22px;
    }

    .sidebar-brand .name {
        color: #f8fbff;
        font-size: 1.25rem;
        font-weight: 800;
    }

    .sidebar-brand .tag {
        color: #7f95aa;
        font-size: .72rem;
        margin-top: 3px;
    }

    .footer {
        text-align: center;
        color: #6f8298;
        font-size: .75rem;
        padding: 30px 0 8px;
    }

    div.stButton > button {
        border: 1px solid rgba(110,231,249,.25);
        border-radius: 14px;
        min-height: 48px;
        font-weight: 800;
        background: linear-gradient(90deg, rgba(34,211,238,.16), rgba(139,92,246,.18));
        color: #effcff;
        box-shadow: 0 10px 30px rgba(0,0,0,.18);
        transition: all .2s ease;
    }

    div.stButton > button:hover {
        border-color: rgba(110,231,249,.55);
        transform: translateY(-1px);
        box-shadow: 0 14px 34px rgba(34,211,238,.10);
    }

    [data-testid="stNumberInput"] input,
    [data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        border-radius: 12px !important;
        border-color: rgba(148,163,184,.20) !important;
        background: rgba(8,18,32,.60) !important;
    }

    [data-testid="stDataFrame"] {
        border: 1px solid var(--border);
        border-radius: 18px;
        overflow: hidden;
    }

    @media (max-width: 800px) {
        .hero { padding: 24px 20px; border-radius: 22px; }
        .block-container { padding-top: 1rem; }
        .result-title { font-size: 1.6rem; }
        .gauge-wrap { width: 175px; height: 175px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==================================================
# MODEL LOADING
# ==================================================

@st.cache_resource
def load_model():
    model = joblib.load("model/random_forest_model.pkl")
    selected_features = joblib.load("model/selected_features.pkl")
    return model, selected_features


model, selected_features = load_model()

# ==================================================
# SESSION STATE
# ==================================================

defaults = {
    "functional_assessment": 5.0,
    "adl": 6.0,
    "mmse": 20.0,
    "memory_complaints": 0,
    "behavioral_problems": 0,
    "diet_quality": 7.0,
    "cholesterol_triglycerides": 150.0,
    "cholesterol_hdl": 50.0,
    "bmi": 24.0,
    "cholesterol_ldl": 100.0,
    "last_prediction": None,
    "prediction_history": [],
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def reset_inputs():
    for key in [
        "functional_assessment",
        "adl",
        "mmse",
        "memory_complaints",
        "behavioral_problems",
        "diet_quality",
        "cholesterol_triglycerides",
        "cholesterol_hdl",
        "bmi",
        "cholesterol_ldl",
    ]:
        st.session_state[key] = defaults[key]
    st.session_state["last_prediction"] = None


def clear_history():
    st.session_state["prediction_history"] = []
    st.session_state["last_prediction"] = None


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand">
            <div class="name">🧠 AlzheimerAI</div>
            <div class="tag">ML-powered research interface</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Workspace")

    page = st.radio(
        "Navigate",
        [
            "Prediction",
            "AI Insights",
            "Model Information",
            "About Project",
        ],
        label_visibility="collapsed",
    )

    st.markdown("---")

    st.markdown(
        f"""
        <div class="glass-card" style="padding:16px;">
            <div class="mini-label">Deployed model</div>
            <div class="mini-value">Random Forest</div>
            <div style="color:#8ea5bb;font-size:.78rem;margin-top:5px;">
                {len(selected_features)} selected input features
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    history_count = len(st.session_state["prediction_history"])

    st.markdown(
        f"""
        <div class="metric-card" style="min-height:90px;padding:15px;">
            <div class="mini-label">Session activity</div>
            <div class="mini-value">{history_count}</div>
            <div class="metric-caption">Predictions this session</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption("Academic • Educational • Research")

# ==================================================
# GLOBAL HERO
# ==================================================

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">AI / MACHINE LEARNING • RESEARCH INTERFACE</div>
        <h1 class="hero-title">Alzheimer<span>AI</span></h1>
        <p class="hero-subtitle">
            A modern machine-learning interface for exploring Alzheimer's
            disease classification using the deployed Random Forest model.
        </p>
        <div class="status-pill">
            <span class="status-dot"></span>
            Model loaded • Ready for inference
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==================================================
# PREDICTION PAGE
# ==================================================

if page == "Prediction":

    st.markdown(
        '<div class="section-title">AI Prediction Workspace</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Enter the model inputs below and run an inference. '
        'Results are displayed for educational and research purposes.'
        '</div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns(2, gap="large")

    with left:
        st.markdown("#### 🧠 Cognitive & Functional Profile")

        st.number_input(
            "Functional Assessment",
            min_value=0.0,
            max_value=10.0,
            step=0.1,
            key="functional_assessment",
            help="Input feature used by the trained model.",
        )

        st.number_input(
            "ADL",
            min_value=0.0,
            max_value=10.0,
            step=0.1,
            key="adl",
            help="Input feature used by the trained model.",
        )

        st.number_input(
            "MMSE",
            min_value=0.0,
            max_value=30.0,
            step=0.1,
            key="mmse",
            help="Input feature used by the trained model.",
        )

        st.selectbox(
            "Memory Complaints",
            [0, 1],
            format_func=lambda x: "No (0)" if x == 0 else "Yes (1)",
            key="memory_complaints",
        )

        st.selectbox(
            "Behavioral Problems",
            [0, 1],
            format_func=lambda x: "No (0)" if x == 0 else "Yes (1)",
            key="behavioral_problems",
        )


    with right:
        st.markdown("#### 🧬 Health & Lifestyle Profile")

        st.number_input(
            "Diet Quality",
            min_value=0.0,
            max_value=10.0,
            step=0.1,
            key="diet_quality",
            help="Input feature used by the trained model.",
        )

        st.number_input(
            "Cholesterol Triglycerides",
            min_value=0.0,
            max_value=500.0,
            step=0.1,
            key="cholesterol_triglycerides",
            help="Input feature used by the trained model.",
        )

        st.number_input(
            "Cholesterol HDL",
            min_value=0.0,
            max_value=150.0,
            step=0.1,
            key="cholesterol_hdl",
            help="Input feature used by the trained model.",
        )

        st.number_input(
            "BMI",
            min_value=0.0,
            max_value=100.0,
            step=0.1,
            key="bmi",
            help="Input feature used by the trained model.",
        )

        st.number_input(
            "Cholesterol LDL",
            min_value=0.0,
            max_value=300.0,
            step=0.1,
            key="cholesterol_ldl",
            help="Input feature used by the trained model.",
        )


    action1, action2 = st.columns([3, 1])

    with action1:
        run_prediction = st.button(
            "⚡ Run AI Inference",
            use_container_width=True,
        )

    with action2:
        st.button(
            "↻ New Input",
            use_container_width=True,
            on_click=reset_inputs,
        )

    if run_prediction:

        input_data = pd.DataFrame(
            [[
                st.session_state["functional_assessment"],
                st.session_state["adl"],
                st.session_state["mmse"],
                st.session_state["memory_complaints"],
                st.session_state["behavioral_problems"],
                st.session_state["diet_quality"],
                st.session_state["cholesterol_triglycerides"],
                st.session_state["cholesterol_hdl"],
                st.session_state["bmi"],
                st.session_state["cholesterol_ldl"],
            ]],
            columns=selected_features,
        )

        # Existing deployed-model prediction logic.
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        if prediction == 1:
            result_class = "diagnosis"
            icon = "⚠️"
            result_text = "Diagnosis"
            result_note = (
                "The deployed model classified this input as the Diagnosis class."
            )
        else:
            result_class = "clear"
            icon = "✓"
            result_text = "No Diagnosis"
            result_note = (
                "The deployed model classified this input as the No Diagnosis class."
            )

        timestamp = datetime.now().strftime("%d %b %Y • %I:%M %p")

        result_record = {
            "time": timestamp,
            "prediction": result_text,
            "probability": float(probability),
        }

        st.session_state["last_prediction"] = {
            "prediction": result_text,
            "probability": float(probability),
            "input_data": input_data.copy(),
            "time": timestamp,
        }

        st.session_state["prediction_history"].insert(0, result_record)
        st.session_state["prediction_history"] = (
            st.session_state["prediction_history"][:10]
        )

    # --------------------------------------------------
    # Latest result
    # --------------------------------------------------

    if st.session_state["last_prediction"] is not None:

        result = st.session_state["last_prediction"]
        probability = result["probability"]
        result_text = result["prediction"]

        if result_text == "Diagnosis":
            result_class = "diagnosis"
            icon = "⚠️"
            note = (
                "The deployed model classified this input as the Diagnosis class."
            )
        else:
            result_class = "clear"
            icon = "✓"
            note = (
                "The deployed model classified this input as the No Diagnosis class."
            )

        gauge_angle = max(0, min(360, probability * 360))

        result_col, gauge_col = st.columns([1.25, .85], gap="large")

        with result_col:
            st.markdown("### Latest Model Inference")

            if result_text == "Diagnosis":
                st.error(f"⚠️ **{result_text}**")
            else:
                st.success(f"✓ **{result_text}**")

            st.caption(note)

            st.markdown("**Diagnosis probability**")
            st.markdown(
                f'<div style="font-size:2.8rem;font-weight:800;letter-spacing:-.04em;">'
                f'{probability * 100:.2f}%</div>',
                unsafe_allow_html=True,
            )
            st.progress(float(probability))
            st.caption(
                "Random Forest estimated probability for the Diagnosis class."
            )

        with gauge_col:
            st.markdown("### Probability Gauge")

            # A robust native Streamlit gauge-style visualization.
            st.progress(float(probability))

            gauge_col1, gauge_col2, gauge_col3 = st.columns(3)
            with gauge_col1:
                st.metric("0%", "Low")
            with gauge_col2:
                st.metric("Current", f"{probability * 100:.1f}%")
            with gauge_col3:
                st.metric("100%", "High")

            st.caption(
                "Visual representation of the model's estimated "
                "Diagnosis-class probability."
            )

        st.markdown("<br>", unsafe_allow_html=True)

        r1, r2, r3, r4 = st.columns(4)

        summary_cards = [
            (r1, "Prediction", result_text, "Model output class"),
            (r2, "Probability", f"{probability * 100:.2f}%", "Diagnosis probability"),
            (r3, "Features", str(len(selected_features)), "Inputs supplied"),
            (r4, "Model", "Random Forest", "Deployed classifier"),
        ]

        for col, label, value, caption in summary_cards:
            with col:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="mini-label">{label}</div>
                        <div class="mini-value">{value}</div>
                        <div class="metric-caption">{caption}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        # --------------------------------------------------
        # Individual prediction input snapshot
        # --------------------------------------------------

        st.markdown("<br>", unsafe_allow_html=True)

        snapshot_col, history_col = st.columns([1.25, .75], gap="large")

        with snapshot_col:
            st.markdown(
                '<div class="glass-card">',
                unsafe_allow_html=True,
            )
            st.markdown("#### 🔎 Current Input Analysis")

            snapshot = result["input_data"].T.reset_index()
            snapshot.columns = ["Feature", "Value"]

            st.dataframe(
                snapshot,
                use_container_width=True,
                hide_index=True,
            )

            st.markdown(
                """
                <div style="
                    color:#8298ad;
                    font-size:.75rem;
                    line-height:1.6;
                    margin-top:8px;
                ">
                    This table shows the exact values supplied to the
                    deployed model for the latest inference.
                </div>
                """,
                unsafe_allow_html=True,
            )

    
        with history_col:
            st.markdown(
                '<div class="glass-card">',
                unsafe_allow_html=True,
            )
            st.markdown("#### 🕘 Session History")

            history = st.session_state["prediction_history"]

            if history:
                for item in history:
                    history_icon = (
                        "⚠️"
                        if item["prediction"] == "Diagnosis"
                        else "✓"
                    )

                    st.markdown(
                        f"""
                        <div class="history-row">
                            <div class="history-time">
                                {item["time"]}
                            </div>
                            <div class="history-result">
                                {history_icon} {item["prediction"]}
                                · {item["probability"] * 100:.2f}%
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                st.markdown("<br>", unsafe_allow_html=True)

                if st.button(
                    "Clear Session History",
                    use_container_width=True,
                ):
                    clear_history()
                    st.rerun()

            else:
                st.markdown(
                    """
                    <div style="
                        color:#8298ad;
                        line-height:1.7;
                        padding:18px 0;
                    ">
                        No predictions have been recorded in this session yet.
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    
        st.info(
            "This application is for educational and research purposes only. "
            "It is not a medical diagnosis or a substitute for professional medical advice."
        )

# ==================================================
# AI INSIGHTS
# ==================================================

elif page == "AI Insights":

    st.markdown(
        '<div class="section-title">AI Insights</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Explore how the deployed Random Forest model uses the selected '
        'features during classification.'
        '</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    cards = [
        (c1, "Model", "Random Forest", "Deployed classifier"),
        (c2, "Input Features", str(len(selected_features)), "Selected model features"),
        (c3, "Test Accuracy", "95.12%", "Reported test-set accuracy"),
    ]

    for col, label, value, caption in cards:
        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="mini-label">{label}</div>
                    <div class="metric-number">{value}</div>
                    <div class="metric-caption">{caption}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="glass-card">',
        unsafe_allow_html=True,
    )

    st.markdown("#### 🧩 Feature Importance")

    st.markdown(
        """
        <div style="
            color:#9fb0c3;
            line-height:1.7;
            margin-bottom:15px;
        ">
            These values show the Random Forest model's feature importance
            across its trained trees. They describe model-level contribution
            and should not be interpreted as medical causation or as an
            individual clinical explanation.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if hasattr(model, "feature_importances_"):

        importance_df = pd.DataFrame(
            {
                "Feature": selected_features,
                "Importance": model.feature_importances_,
            }
        ).sort_values(
            "Importance",
            ascending=False,
        )

        st.bar_chart(
            importance_df.set_index("Feature"),
            use_container_width=True,
        )

        display_df = importance_df.copy()
        display_df["Importance"] = (
            display_df["Importance"] * 100
        ).round(2)

        display_df = display_df.rename(
            columns={"Importance": "Importance (%)"}
        )

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
        )

    else:
        st.warning(
            "Feature importance is not available for the loaded model."
        )

    st.markdown("</div>", unsafe_allow_html=True)

    insight1, insight2 = st.columns(2, gap="large")

    with insight1:
        st.markdown(
            """
            <div class="glass-card">
                <div class="mini-label">Inference pipeline</div>
                <div class="mini-value">
                    Input → Random Forest → Probability → Classification
                </div>
                <div style="
                    color:#9fb0c3;
                    line-height:1.7;
                    margin-top:10px;
                ">
                    The application collects the selected features,
                    sends them to the deployed model, obtains the
                    predicted class and estimated probability, and
                    displays the result in the Prediction workspace.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with insight2:
        st.markdown(
            """
            <div class="glass-card">
                <div class="mini-label">Explainability note</div>
                <div class="mini-value">
                    Model-level insight
                </div>
                <div style="
                    color:#9fb0c3;
                    line-height:1.7;
                    margin-top:10px;
                ">
                    Feature importance indicates how the trained model
                    uses variables across the dataset. It does not
                    establish that a feature independently causes
                    Alzheimer's disease.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ==================================================
# MODEL INFORMATION
# ==================================================

elif page == "Model Information":

    st.markdown(
        '<div class="section-title">Model Intelligence</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Evaluation metrics and the feature set used by the deployed classifier.'
        '</div>',
        unsafe_allow_html=True,
    )

    results = pd.DataFrame(
        {
            "Model": [
                "Random Forest",
                "Decision Tree",
                "SVM",
                "KNN",
                "Logistic Regression",
            ],
            "Accuracy": [.9512, .9465, .8698, .8372, .8163],
            "Precision": [.9456, .9329, .8243, .7770, .7386],
            "Recall": [.9145, .9145, .8026, .7566, .7434],
            "F1-Score": [.9298, .9236, .8133, .7667, .7410],
            "ROC-AUC": [.9415, .9362, .9249, .8914, .8894],
        }
    )

    rf = results.iloc[0]

    cols = st.columns(4)

    for col, label in zip(
        cols,
        ["Accuracy", "Precision", "Recall", "ROC-AUC"],
    ):
        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="mini-label">{label}</div>
                    <div class="metric-number">
                        {rf[label] * 100:.2f}%
                    </div>
                    <div class="metric-caption">
                        Random Forest test metric
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2 = st.columns([1.45, 1], gap="large")

    with c1:
        st.markdown(
            '<div class="glass-card">',
            unsafe_allow_html=True,
        )

        st.markdown("#### 📊 Model Evaluation")

        st.dataframe(
            results.style.format(
                {
                    c: "{:.2%}"
                    for c in [
                        "Accuracy",
                        "Precision",
                        "Recall",
                        "F1-Score",
                        "ROC-AUC",
                    ]
                }
            ),
            use_container_width=True,
            hide_index=True,
        )


    with c2:
        st.markdown(
            '<div class="glass-card">',
            unsafe_allow_html=True,
        )

        st.markdown("#### 🧩 Selected Features")

        for feature in selected_features:
            st.markdown(
                f'<span class="feature-chip">{feature}</span>',
                unsafe_allow_html=True,
            )


    st.markdown(
        """
        <div class="glass-card">
            <div class="mini-label">Deployed architecture</div>
            <div class="mini-value">Random Forest Classifier</div>
            <div style="
                color:#8ea5bb;
                margin-top:7px;
                line-height:1.6;
            ">
                The final deployed model is loaded from
                <code>model/random_forest_model.pkl</code>.
                Test-set accuracy reported by the project:
                <strong style="color:#dffbff;">95.12%</strong>.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==================================================
# ABOUT PROJECT
# ==================================================

elif page == "About Project":

    st.markdown(
        '<div class="section-title">Inside the Project</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-subtitle">'
        'A clean view of the project workflow, algorithms, and deployment.'
        '</div>',
        unsafe_allow_html=True,
    )

    about_left, about_right = st.columns([1.1, 1], gap="large")

    with about_left:

        st.markdown(
            """
            <div class="glass-card">
                <div class="mini-label">Project overview</div>
                <div class="mini-value">
                    Alzheimer's Disease Classification
                </div>
                <p style="
                    color:#9fb0c3;
                    line-height:1.7;
                    margin-top:12px;
                ">
                    This project applies machine learning techniques to
                    classify Alzheimer's disease diagnosis using selected
                    patient-related features.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        workflow = [
            ("01", "Data Collection", "Gather the project dataset."),
            ("02", "Data Inspection", "Inspect structure and variables."),
            ("03", "Missing Value Analysis", "Review missing-value patterns."),
            ("04", "Data Cleaning", "Prepare the dataset for modeling."),
            ("05", "Exploratory Data Analysis", "Explore patterns in the data."),
            ("06", "Correlation Analysis", "Study feature relationships."),
            ("07", "Feature Selection", "Select model input features."),
            ("08", "Train-Test Split", "Separate data for evaluation."),
            ("09", "Model Building", "Train classification algorithms."),
            ("10", "Model Comparison", "Compare evaluation metrics."),
            ("11", "Final Model Evaluation", "Evaluate the final classifier."),
            ("12", "Model Saving", "Save trained model artifacts."),
            ("13", "Streamlit Deployment", "Deploy the interactive application."),
        ]

        st.markdown(
            '<div class="glass-card"><h4>🔄 Project Workflow</h4>',
            unsafe_allow_html=True,
        )

        for number, title, description in workflow:
            st.markdown(
                f"""
                <div class="workflow-step">
                    <div class="step-number">{number}</div>
                    <div class="step-text">
                        <strong>{title}</strong>
                        <span>{description}</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


    with about_right:

        st.markdown(
            """
            <div class="glass-card">
                <div class="mini-label">Algorithms evaluated</div>
                <div style="margin-top:12px;">
                    <span class="feature-chip">Logistic Regression</span>
                    <span class="feature-chip">Decision Tree</span>
                    <span class="feature-chip">Random Forest</span>
                    <span class="feature-chip">K-Nearest Neighbors</span>
                    <span class="feature-chip">Support Vector Machine</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="glass-card">
                <div class="mini-label">Deployment stack</div>
                <div class="mini-value">Python + Streamlit</div>
                <div style="
                    color:#8ea5bb;
                    line-height:1.7;
                    margin-top:9px;
                ">
                    Model artifact:
                    <code>random_forest_model.pkl</code><br>
                    Feature artifact:
                    <code>selected_features.pkl</code><br>
                    Input features:
                    <strong style="color:#dffbff;">
                        {len(selected_features)}
                    </strong>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="glass-card">
                <div class="mini-label">Important note</div>
                <div style="
                    color:#cbd5e1;
                    line-height:1.7;
                    margin-top:9px;
                ">
                    This application is intended for academic and
                    educational purposes. It is not a medical diagnosis
                    or a substitute for professional medical advice.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ==================================================
# FOOTER
# ==================================================

st.markdown(
    """
    <div class="footer">
        AlzheimerAI • Machine Learning Research Interface • Built with Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
