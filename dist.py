import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('EXPONENTIAL AND POISSON DISTRIBUTION')

with st.sidebar:
    tipe = st.radio('Pilih Tipe',['Exponential Dist','Poisson Dist'])

with st.expander('Pilih Parameter'):
    with st.form('Pilih Parameter'):
        if tipe == 'Exponential Dist':
            lambd = st.number_input('Lambda', min_value=0.01, value=1.0, step=0.01)
        elif tipe == 'Poisson Dist':
            lam = st.number_input('Lambda', min_value=0.01, value=1.0, step=0.01)
        submit = st.form_submit_button('Submit Parameter')

if tipe == 'Exponential Dist':
    n = st.number_input('Jumlah data', min_value=1, value=100, step=1)
    data = np.random.exponential(scale=1/lambd, size=n)
    df = pd.DataFrame({'Data': data})

    st.write('Data Exponential Distribution:')
    st.write(df)

    st.write('Histogram:')
    plt.hist(data, bins='auto', density=True)
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.title('Exponential Distribution')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

elif tipe == 'Poisson Dist':
    n = st.number_input('Jumlah data', min_value=1, value=100, step=1)
    data = np.random.poisson(lam=lam, size=n)
    df = pd.DataFrame({'Data': data})

    st.write('Data Poisson Distribution:')
    st.write(df)

    st.write('Histogram:')
    plt.hist(data, bins='auto', density=True)
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.title('Poisson Distribution')
    st.pyplot()
