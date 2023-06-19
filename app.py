import numpy as np 
import pandas as pd 
import streamlit as st 
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
import seaborn as sns 
from streamlit_lottie import st_lottie
import requests
from pathlib import Path
import json


# ---- PAGE SETTING ----
st.set_page_config(
    page_icon=":mag_right:",
    page_title="EDA App",
    layout='wide'
)



# ----PATH SETTING ------
current_dir = Path('__file__').parent if '__file__' in locals() else Path.cwd()

css_file = current_dir / 'main.css'
data = current_dir/'lottie'/'data_analysis.json'


@st.cache_data
def load_lottie(path):
    with open(path, 'r') as file:
        url = json.load(file)
        return url

data = load_lottie(data)

@st.cache_data
def load_css(filepath):
    with open(filepath) as f:
        css = f.read()
        return f"<style>{css}</style>"

css = load_css(css_file)
st.markdown(css, unsafe_allow_html=True)




            
col1, col2 = st.columns(2, gap='small')
with col1:
    st.markdown('''
    # **The Exploratory Data Analysis App**
    Data Analysis: Unlocking Insights for Your Business

    As businesses generate more data than ever before, it's essential to know how to make sense of it all. By learning data visualization techniques, you can extract relevant insights and make impactful decisions. Let's dive in!
    ''')
    st.write("Email me for more info....")
    st.markdown(":email: felixkuria12@gmail.com")

@st.cache_data
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
data_analysis = load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_bdlrkrqv.json')

with col2:
    st_lottie(data, height=260)
                




with st.sidebar:
    st.markdown('# Upload your CSV')
    upload_file = st.sidebar.file_uploader("Upload your input csv")


if upload_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(upload_file)
        return csv
    
    df = load_csv()
    profile = ProfileReport(df, explorative=True)
    st.header("**Input DataFrame**")
    st.write(df)
    st.divider()
    st.header('**pandas profiling report**')
    st_profile_report(profile)

else:
    st.info('Awaiting for CSV file to be uploaded')
    if st.button("Press to use Example Dataset"):
        df = sns.load_dataset('iris')
        profile = ProfileReport(df)
        st.header("**Input DataFrame** ")
        st.divider()
        st.header('**Pandas Profiling Report**')
        st_profile_report(profile)
