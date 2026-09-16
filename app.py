import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="AlzheimerAI | Cognitive Health Screening",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Modern 2026 AI interface ----------
st.markdown(r'''<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
:root{--bg:#07111f;--border:rgba(148,163,184,.18);--text:#eef6ff;--muted:#9fb0c3;--accent:#6ee7f9;}
html,body,[class*="css"]{font-family:'Inter',sans-serif}.stApp{background:radial-gradient(circle at 12% 8%,rgba(110,231,249,.11),transparent 28%),radial-gradient(circle at 88% 18%,rgba(139,92,246,.12),transparent 30%),radial-gradient(circle at 55% 100%,rgba(59,130,246,.08),transparent 35%),var(--bg);color:var(--text)}
[data-testid="stHeader"]{background:rgba(7,17,31,.72)}[data-testid="stSidebar"]{background:linear-gradient(180deg,rgba(8,19,34,.98),rgba(7,14,27,.98));border-right:1px solid var(--border)}[data-testid="stSidebar"] *{color:#dbeafe}.block-container{max-width:1450px;padding-top:2rem;padding-bottom:3rem}
.hero{position:relative;overflow:hidden;padding:30px 34px;border:1px solid rgba(110,231,249,.18);border-radius:28px;background:linear-gradient(135deg,rgba(17,37,61,.92),rgba(15,23,42,.72));box-shadow:0 24px 70px rgba(0,0,0,.28);margin-bottom:24px}.hero:after{content:"";position:absolute;width:220px;height:220px;right:-70px;top:-80px;border-radius:50%;background:rgba(110,231,249,.08);filter:blur(8px)}
.eyebrow{color:var(--accent);font-size:.76rem;font-weight:800;letter-spacing:.16em;text-transform:uppercase;margin-bottom:10px}.hero-title{font-size:clamp(2rem,4vw,3.6rem);line-height:1.05;font-weight:800;letter-spacing:-.04em;margin:0;color:#f8fbff}.hero-title span{background:linear-gradient(90deg,#dffbff,#6ee7f9,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent}.hero-subtitle{color:var(--muted);font-size:1rem;line-height:1.7;max-width:850px;margin-top:14px}.status-pill{display:inline-flex;align-items:center;gap:8px;margin-top:20px;padding:8px 13px;border-radius:999px;border:1px solid rgba(52,211,153,.2);background:rgba(52,211,153,.08);color:#a7f3d0;font-size:.78rem;font-weight:700}.status-dot{width:8px;height:8px;border-radius:50%;background:#34d399;box-shadow:0 0 12px rgba(52,211,153,.9)}
.section-title{font-size:1.55rem;font-weight:800;letter-spacing:-.02em;color:#f8fbff;margin:10px 0 4px}.section-subtitle{color:var(--muted);margin-bottom:20px}.glass-card{border:1px solid var(--border);background:linear-gradient(145deg,rgba(20,37,60,.82),rgba(12,24,42,.70));border-radius:22px;padding:22px;box-shadow:0 16px 50px rgba(0,0,0,.18);margin-bottom:18px}.mini-label{color:#8ea5bb;font-size:.74rem;font-weight:700;text-transform:uppercase;letter-spacing:.12em}.mini-value{color:#f8fbff;font-size:1.35rem;font-weight:800;margin-top:6px}.feature-chip{display:inline-block;margin:5px 5px 0 0;padding:8px 11px;border-radius:12px;background:rgba(110,231,249,.07);border:1px solid rgba(110,231,249,.13);color:#c8f8ff;font-size:.78rem;font-weight:600}
.result-card{border-radius:26px;padding:28px;margin-top:22px;border:1px solid rgba(110,231,249,.18);background:linear-gradient(145deg,rgba(20,37,60,.92),rgba(10,24,43,.86));box-shadow:0 24px 65px rgba(0,0,0,.25)}.result-card.diagnosis{border-color:rgba(251,113,133,.25);background:linear-gradient(145deg,rgba(70,25,45,.58),rgba(20,24,43,.90))}.result-card.clear{border-color:rgba(52,211,153,.22);background:linear-gradient(145deg,rgba(12,55,55,.48),rgba(10,29,43,.90))}.result-kicker{color:#8ea5bb;font-size:.76rem;text-transform:uppercase;letter-spacing:.14em;font-weight:800}.result-title{font-size:2rem;font-weight:800;margin:8px 0 4px;color:#fff}.result-note{color:#aebdcb;line-height:1.6}.probability{font-size:3rem;font-weight:800;letter-spacing:-.05em;color:#eafcff}.meter{height:10px;border-radius:999px;overflow:hidden;background:rgba(148,163,184,.14);margin-top:12px}.meter-fill{height:100%;border-radius:999px;background:linear-gradient(90deg,#22d3ee,#8b5cf6)}
.metric-card{border:1px solid var(--border);background:linear-gradient(145deg,rgba(19,36,59,.80),rgba(11,24,42,.72));border-radius:20px;padding:19px;min-height:115px}.metric-number{font-size:1.8rem;font-weight:800;color:#f8fbff;margin-top:5px}.metric-caption{color:#8ea5bb;font-size:.8rem}.workflow-step{display:flex;gap:14px;align-items:flex-start;padding:15px 0;border-bottom:1px solid rgba(148,163,184,.10)}.workflow-step:last-child{border-bottom:none}.step-number{min-width:34px;height:34px;display:grid;place-items:center;border-radius:11px;background:rgba(110,231,249,.08);border:1px solid rgba(110,231,249,.13);color:#a5f3fc;font-weight:800}.step-text strong{color:#f1f5f9}.step-text span{display:block;color:#8ea5bb;font-size:.83rem;margin-top:3px}.footer{text-align:center;color:#6f8298;font-size:.76rem;padding:30px 0 8px}
div.stButton>button{border:1px solid rgba(110,231,249,.25);border-radius:14px;min-height:48px;font-weight:800;background:linear-gradient(90deg,rgba(34,211,238,.16),rgba(139,92,246,.18));color:#effcff;box-shadow:0 10px 30px rgba(0,0,0,.18)}div.stButton>button:hover{border-color:rgba(110,231,249,.55);transform:translateY(-1px)}[data-testid="stNumberInput"] input,[data-testid="stSelectbox"] div[data-baseweb="select"]>div{border-radius:12px!important;border-color:rgba(148,163,184,.20)!important;background:rgba(8,18,32,.60)!important}[data-testid="stDataFrame"]{border:1px solid var(--border);border-radius:18px;overflow:hidden}.sidebar-brand{padding:8px 4px 22px}.sidebar-brand .name{color:#f8fbff;font-size:1.25rem;font-weight:800}.sidebar-brand .tag{color:#7f95aa;font-size:.72rem;margin-top:3px}
@media(max-width:800px){.hero{padding:24px 20px;border-radius:22px}.block-container{padding-top:1rem}.result-title{font-size:1.6rem}.probability{font-size:2.4rem}}
</style>''', unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model = joblib.load("model/random_forest_model.pkl")
    selected_features = joblib.load("model/selected_features.pkl")
    return model, selected_features

model, selected_features = load_model()

with st.sidebar:
    st.markdown('''<div class="sidebar-brand"><div class="name">🧠 AlzheimerAI</div><div class="tag">ML-powered research interface</div></div>''', unsafe_allow_html=True)
    st.markdown("### Workspace")
    page = st.radio("Navigate", ["Prediction", "AI Insights", "Model Information", "About Project"], label_visibility="collapsed")
    st.markdown("---")
    st.markdown(f'''<div class="glass-card" style="padding:16px;"><div class="mini-label">Deployed model</div><div class="mini-value">Random Forest</div><div style="color:#8ea5bb;font-size:.78rem;margin-top:5px;">{len(selected_features)} selected input features</div></div>''', unsafe_allow_html=True)
    st.caption("Academic • Educational • Research")

st.markdown('''<div class="hero"><div class="eyebrow">AI / MACHINE LEARNING • RESEARCH INTERFACE</div><h1 class="hero-title">Alzheimer<span>AI</span></h1><p class="hero-subtitle">A modern machine-learning interface for exploring Alzheimer's disease classification using the deployed Random Forest model.</p><div class="status-pill"><span class="status-dot"></span>Model loaded • Ready for inference</div></div>''', unsafe_allow_html=True)

if page == "Prediction":
    st.markdown('<div class="section-title">Cognitive & Health Inputs</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Enter the same feature values used by the trained model, then run an inference.</div>', unsafe_allow_html=True)
    left, right = st.columns(2, gap="large")
    with left:
        st.markdown("#### 🧠 Cognitive & Functional Profile")
        functional_assessment = st.number_input("Functional Assessment", min_value=0.0, max_value=10.0, value=5.0, step=0.1, help="Input feature used by the trained model.")
        adl = st.number_input("ADL", min_value=0.0, max_value=10.0, value=6.0, step=0.1, help="Input feature used by the trained model.")
        mmse = st.number_input("MMSE", min_value=0.0, max_value=30.0, value=20.0, step=0.1, help="Input feature used by the trained model.")
        memory_complaints = st.selectbox("Memory Complaints", [0, 1], format_func=lambda x: "No (0)" if x == 0 else "Yes (1)")
        behavioral_problems = st.selectbox("Behavioral Problems", [0, 1], format_func=lambda x: "No (0)" if x == 0 else "Yes (1)")
    with right:
        st.markdown("#### 🧬 Health & Lifestyle Profile")
        diet_quality = st.number_input("Diet Quality", min_value=0.0, max_value=10.0, value=7.0, step=0.1, help="Input feature used by the trained model.")
        cholesterol_triglycerides = st.number_input("Cholesterol Triglycerides", min_value=0.0, max_value=500.0, value=150.0, step=0.1, help="Input feature used by the trained model.")
        cholesterol_hdl = st.number_input("Cholesterol HDL", min_value=0.0, max_value=150.0, value=50.0, step=0.1, help="Input feature used by the trained model.")
        bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=24.0, step=0.1, help="Input feature used by the trained model.")
        cholesterol_ldl = st.number_input("Cholesterol LDL", min_value=0.0, max_value=300.0, value=100.0, step=0.1, help="Input feature used by the trained model.")

    if st.button("⚡ Run AI Inference", use_container_width=True):
        input_data = pd.DataFrame([[functional_assessment, adl, mmse, memory_complaints, behavioral_problems, diet_quality, cholesterol_triglycerides, cholesterol_hdl, bmi, cholesterol_ldl]], columns=selected_features)
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        if prediction == 1:
            result_class, icon, result_text = "diagnosis", "⚠️", "Diagnosis"
            result_note = "The deployed model classified this input as the Diagnosis class."
        else:
            result_class, icon, result_text = "clear", "✓", "No Diagnosis"
            result_note = "The deployed model classified this input as the No Diagnosis class."
        st.markdown(f'''<div class="result-card {result_class}"><div class="result-kicker">Model inference complete</div><div class="result-title">{icon} {result_text}</div><p class="result-note">{result_note}</p><div style="height:18px"></div><div class="mini-label">Diagnosis probability</div><div class="probability">{probability*100:.2f}%</div><div class="meter"><div class="meter-fill" style="width:{probability*100:.2f}%"></div></div><div style="color:#8298ad;font-size:.76rem;margin-top:10px">Random Forest estimated probability for the Diagnosis class.</div></div>''', unsafe_allow_html=True)
        r1, r2, r3 = st.columns(3)
        with r1: st.markdown(f'''<div class="metric-card"><div class="mini-label">Prediction</div><div class="mini-value">{result_text}</div><div class="metric-caption">Model output class</div></div>''', unsafe_allow_html=True)
        with r2: st.markdown(f'''<div class="metric-card"><div class="mini-label">Probability</div><div class="mini-value">{probability*100:.2f}%</div><div class="metric-caption">Diagnosis class probability</div></div>''', unsafe_allow_html=True)
        with r3: st.markdown(f'''<div class="metric-card"><div class="mini-label">Features</div><div class="mini-value">{len(selected_features)}</div><div class="metric-caption">Inputs supplied to model</div></div>''', unsafe_allow_html=True)
        st.info("This application is for educational and research purposes only. It is not a medical diagnosis or a substitute for professional medical advice.")

elif page == "Model Information":
    st.markdown('<div class="section-title">Model Intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Evaluation metrics and the feature set used by the deployed classifier.</div>', unsafe_allow_html=True)
    results = pd.DataFrame({"Model":["Random Forest","Decision Tree","SVM","KNN","Logistic Regression"],"Accuracy":[.9512,.9465,.8698,.8372,.8163],"Precision":[.9456,.9329,.8243,.7770,.7386],"Recall":[.9145,.9145,.8026,.7566,.7434],"F1-Score":[.9298,.9236,.8133,.7667,.7410],"ROC-AUC":[.9415,.9362,.9249,.8914,.8894]})
    rf = results.iloc[0]
    cols = st.columns(4)
    for col, label in zip(cols, ["Accuracy","Precision","Recall","ROC-AUC"]):
        with col: st.markdown(f'''<div class="metric-card"><div class="mini-label">{label}</div><div class="metric-number">{rf[label]*100:.2f}%</div><div class="metric-caption">Random Forest test metric</div></div>''', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([1.45,1], gap="large")
    with c1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True); st.markdown("#### 📊 Model Evaluation")
        st.dataframe(results.style.format({c:"{:.2%}" for c in ["Accuracy","Precision","Recall","F1-Score","ROC-AUC"]}), use_container_width=True, hide_index=True); st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True); st.markdown("#### 🧩 Selected Features")
        for feature in selected_features: st.markdown(f'<span class="feature-chip">{feature}</span>', unsafe_allow_html=True)
    st.markdown(f'''<div class="glass-card"><div class="mini-label">Deployed architecture</div><div class="mini-value">Random Forest Classifier</div><div style="color:#8ea5bb;margin-top:7px;line-height:1.6">The final deployed model is loaded from <code>model/random_forest_model.pkl</code>. Test-set accuracy reported by the project: <strong style="color:#dffbff">95.12%</strong>.</div></div>''', unsafe_allow_html=True)

elif page == "AI Insights":
    st.markdown('<div class="section-title">AI Insights</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Explore how the deployed Random Forest model uses the selected features during classification.</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    cards = [
        (c1, "Model", "Random Forest", "Deployed classifier"),
        (c2, "Input Features", str(len(selected_features)), "Selected model features"),
        (c3, "Test Accuracy", "95.12%", "Reported test-set accuracy"),
    ]
    for col, label, value, caption in cards:
        with col:
            st.markdown(f'<div class="metric-card"><div class="mini-label">{label}</div><div class="metric-number">{value}</div><div class="metric-caption">{caption}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("#### 🧩 Feature Importance")
    st.markdown("""<div style="color:#9fb0c3;line-height:1.7;margin-bottom:15px;">These values show the Random Forest model's feature importance across its trained trees. They describe model-level contribution and should not be interpreted as medical causation or as an individual clinical explanation.</div>""", unsafe_allow_html=True)

    if hasattr(model, "feature_importances_"):
        importance_df = pd.DataFrame({"Feature": selected_features, "Importance": model.feature_importances_}).sort_values("Importance", ascending=False)
        st.bar_chart(importance_df.set_index("Feature"), use_container_width=True)
        display_df = importance_df.copy()
        display_df["Importance"] = (display_df["Importance"] * 100).round(2)
        display_df = display_df.rename(columns={"Importance": "Importance (%)"})
        st.dataframe(display_df, use_container_width=True, hide_index=True)
    else:
        st.warning("Feature importance is not available for the loaded model.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""<div class="glass-card"><div class="mini-label">Inference pipeline</div><div class="mini-value">Input → Random Forest → Probability → Classification</div><div style="color:#9fb0c3;line-height:1.7;margin-top:10px;">The application collects the selected features, sends them to the deployed model, obtains the predicted class and estimated probability, and displays the result in the Prediction workspace.</div></div>""", unsafe_allow_html=True)

    st.markdown("""<div class="glass-card"><div class="mini-label">Explainability note</div><div class="mini-value">Model-level insight, not medical advice</div><div style="color:#9fb0c3;line-height:1.7;margin-top:10px;">Feature importance indicates how the trained model uses variables across the dataset. It does not establish that a feature independently causes Alzheimer's disease.</div></div>""", unsafe_allow_html=True)

else:
    st.markdown('<div class="section-title">Inside the Project</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">A clean view of the project workflow, algorithms, and deployment.</div>', unsafe_allow_html=True)
    about_left, about_right = st.columns([1.1,1], gap="large")
    with about_left:
        st.markdown('''<div class="glass-card"><div class="mini-label">Project overview</div><div class="mini-value">Alzheimer's Disease Classification</div><p style="color:#9fb0c3;line-height:1.7;margin-top:12px">This project applies machine learning techniques to classify Alzheimer's disease diagnosis using selected patient-related features.</p></div>''', unsafe_allow_html=True)
        workflow=[("01","Data Collection","Gather the project dataset."),("02","Data Inspection","Inspect structure and variables."),("03","Missing Value Analysis","Review missing-value patterns."),("04","Data Cleaning","Prepare the dataset for modeling."),("05","Exploratory Data Analysis","Explore patterns in the data."),("06","Correlation Analysis","Study feature relationships."),("07","Feature Selection","Select model input features."),("08","Train-Test Split","Separate data for evaluation."),("09","Model Building","Train classification algorithms."),("10","Model Comparison","Compare evaluation metrics."),("11","Final Model Evaluation","Evaluate the final classifier."),("12","Model Saving","Save trained model artifacts."),("13","Streamlit Deployment","Deploy the interactive application.")]
        st.markdown('<div class="glass-card"><h4>🔄 Project Workflow</h4>', unsafe_allow_html=True)
        for n,t,d in workflow: st.markdown(f'<div class="workflow-step"><div class="step-number">{n}</div><div class="step-text"><strong>{t}</strong><span>{d}</span></div></div>', unsafe_allow_html=True)
    with about_right:
        st.markdown('''<div class="glass-card"><div class="mini-label">Algorithms evaluated</div><div style="margin-top:12px"><span class="feature-chip">Logistic Regression</span><span class="feature-chip">Decision Tree</span><span class="feature-chip">Random Forest</span><span class="feature-chip">K-Nearest Neighbors</span><span class="feature-chip">Support Vector Machine</span></div></div>''', unsafe_allow_html=True)
        st.markdown(f'''<div class="glass-card"><div class="mini-label">Deployment stack</div><div class="mini-value">Python + Streamlit</div><div style="color:#8ea5bb;line-height:1.7;margin-top:9px">Model artifact: <code>random_forest_model.pkl</code><br>Feature artifact: <code>selected_features.pkl</code><br>Input features: <strong style="color:#dffbff">{len(selected_features)}</strong></div></div>''', unsafe_allow_html=True)
        st.markdown('''<div class="glass-card"><div class="mini-label">Important note</div><div style="color:#cbd5e1;line-height:1.7;margin-top:9px">This application is intended for academic and educational purposes. It is not a medical diagnosis or a substitute for professional medical advice.</div></div>''', unsafe_allow_html=True)

st.markdown('<div class="footer">AlzheimerAI • Machine Learning Research Interface • Built with Streamlit</div>', unsafe_allow_html=True)
