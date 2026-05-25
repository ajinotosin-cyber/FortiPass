import streamlit as st
import re

st.set_page_config(
    page_title="FortiPass",
    page_icon="🔒",
    layout="centered"
)

# ---------- CSS ----------

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

:root{
--bg:#12141A;
--card:#1B1F27;
--accent:#4ADE80;
--text:#F3F4F6;
}

.stApp{
background:var(--bg);
}

.block-container{
max-width:850px;
padding-top:3rem;
}

/* HEADER */

.header-section{
text-align:center;
margin-bottom:40px;
}

.header-row{
display:flex;
justify-content:center;
align-items:center;
gap:8px;
}

.logo{
font-size:28px;
color:var(--accent);
}

.main-title{
font-size:42px;
font-weight:700;
color:white;
margin:0;
}

.subtitle{
margin-top:6px;
font-size:17px;
color:#C9CDD4;
}

/* INPUT LABEL */

.input-label{
color:var(--accent);
font-size:18px;
font-weight:600;
margin-bottom:12px;
}

/* FIX OVERLAP / DUPLICATE INPUT */

[data-testid="stTextInput"]{

width:100% !important;

position:relative !important;

overflow:hidden !important;
}

.stTextInput > div > div{

border:none !important;

background:transparent !important;

box-shadow:none !important;

padding:0 !important;

margin:0 !important;
}

[data-testid="stTextInput"] > div{

border:none !important;

background:transparent !important;

padding:0 !important;

margin:0 !important;

box-shadow:none !important;
}

/* PASSWORD FIELD */

[data-testid="stTextInput"] input{

background:#0F1115 !important;

border:1px solid rgba(74,222,128,.45) !important;

border-radius:12px !important;

padding:14px 18px !important;

font-size:17px !important;

color:white !important;

width:100% !important;

box-sizing:border-box !important;

outline:none !important;

overflow:hidden !important;
}

/* REMOVE EYE BUTTON */

[data-testid="stTextInput"] button{
display:none !important;
}

/* RESULT */

.result-box{

background:var(--card);

border:1px solid rgba(255,255,255,.08);

border-radius:18px;

padding:30px;

margin-top:35px;
}

.result-title{

text-align:center;

font-size:18px;

letter-spacing:2px;

color:#AEB4BE;
}

.result-text{

text-align:center;

font-size:52px;

font-weight:700;

color:var(--accent);

margin-top:12px;
}

.result-sub{

text-align:center;

color:#C9CDD4;

margin-top:10px;

font-size:16px;
}

/* FEATURE CARDS */

.criteria-row{

display:flex;

justify-content:center;

gap:12px;

flex-wrap:wrap;

margin-top:24px;
}

.criteria-card{

background:#11151B;

border:1px solid rgba(255,255,255,.08);

padding:12px 18px;

border-radius:10px;

color:white;
}

/* FOOTER */

hr{
margin-top:40px;
opacity:.2;
}

.footer{

text-align:center;

color:#C9CDD4;

font-size:15px;

margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.markdown("""
<div class="header-section">

<div class="header-row">

<div class="logo">🔒</div>

<div class="main-title">
FortiPass
</div>

</div>

<div class="subtitle">
Password Security Analyzer
</div>

</div>
""", unsafe_allow_html=True)

# ---------- INPUT ----------

st.markdown("""
<div class="input-label">
Enter Password
</div>
""", unsafe_allow_html=True)

password = st.text_input(
label="Password",
placeholder="Enter password",
label_visibility="collapsed",
type="password",
key="password_input"
)

# ---------- ANALYSIS ----------

if password:

    length = len(password) >= 8

    upper = bool(re.search(r"[A-Z]", password))

    numbers = bool(re.search(r"\d", password))

    symbols = bool(re.search(r"[^A-Za-z0-9]", password))

    variety = sum([
        upper,
        numbers,
        symbols
    ]) >= 2

    score = sum([
        length,
        upper,
        numbers,
        symbols,
        variety
    ])

    if score <= 2:
        strength = "WEAK"
        message = "Password is weak and vulnerable"

    elif score <= 4:
        strength = "MEDIUM"
        message = "Password can be improved"

    else:
        strength = "STRONG"
        message = "Password is strong and secure"

    st.markdown(f'''
    <div class="result-box">

    <div class="result-title">
    STRENGTH RESULT
    </div>

    <div class="result-text">
    {strength}
    </div>

    <div class="result-sub">
    {message}
    </div>

    </div>
    ''', unsafe_allow_html=True)

    st.markdown(f'''

<div class="criteria-row">

<div class="criteria-card">
{"✓" if length else "✗"} Length
</div>

<div class="criteria-card">
{"✓" if upper else "✗"} Uppercase
</div>

<div class="criteria-card">
{"✓" if numbers else "✗"} Numbers
</div>

<div class="criteria-card">
{"✓" if symbols else "✗"} Symbols
</div>

<div class="criteria-card">
{"✓" if variety else "✗"} Character Variety
</div>

</div>

''', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
Engineered by Oluwatosin Deborah Ajinomisan.
</div>
""", unsafe_allow_html=True)