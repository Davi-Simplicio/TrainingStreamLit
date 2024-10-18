import streamlit as st
import pandas as pd
from itensCompras import getDataFrame
import plotly.express as px

df = pd.read_excel('C:/Users/davii/Itens.xlsx' )

def main():
    st.write(df.head())

def conclusionBarChart():
    bar = px.histogram(df, x='CONCLUSÃO', y='VALOR TOTAL',)
    return bar

st.write(df["MOTOR"].value_counts())


df["COUNT"] = 1

pie = px.pie(df, values='COUNT', names='STATUS', title='Motor Status', labels={'COUNT':'Motor', 'STATUS':'Status'},hover_data='VALOR TOTAL')


df['MOTOR'] = df['MOTOR'].astype(str)
st.write(df['MOTOR'].value_counts())

bar2 = px.histogram(df, x='CREATED', y='VALOR TOTAL', title='Motor Value', color='STATUS', barmode='group')
bar3 = px.histogram(df, x='MOTOR', y='COUNT', title='Motor Value', color='STATUS', labels={'COUNT':'Total de Motores'})

col1,col2 = st.columns(2)

tab1,tab2,tab3,tab4 = st.tabs(["tab 1", "tab 2", "tab 3","tab 4"])

tab1.write(conclusionBarChart())
tab2.write(pie)
tab3.write(bar2)
tab4.write(bar3)

st.sidebar.write('This is a sidebar')