import streamlit as st
import yfinance as yf 
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen
from email.mime import image

imageB3 = Image.open(urlopen('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/B3_logo.png/250px-B3_logo.png'))
st.image(imageB3)

st.title('Comparando ações de três grandes bancos da B3')
st.subheader('Selecione o banco desejado')

opcoes = st.selectbox(
    'Qual ação deseja escolher?',
    ('Banco do Brasil', 'BTG Pactual', 'Bradesco','Compare os três'))
st.write('You selected:', opcoes)

if opcoes == "Banco do Brasil":
    imageBB = Image.open(urlopen('https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Banco_do_Brasil_logo.svg/250px-Banco_do_Brasil_logo.svg.png'))
    st.image(imageBB)
    BB = yf.Ticker("BBAS3.SA")
    hist_bb = BB.history(start="2022-01-01",end="2022-09-23")['Close']
    norm_bb = hist_bb/hist_bb.iloc[10]

    st.subheader('Preço da ação')
    st.area_chart(hist_bb)
    st.subheader('Valorização da ação')
    st.line_chart(norm_bb)
    st.subheader('Tabela geral da ação - mês de setembro')
    st.table(hist_bb)

if opcoes == "BTG Pactual":
    imageBTG = Image.open(urlopen('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Btg-logo-blue.svg/200px-Btg-logo-blue.svg.png'))
    st.image(imageBTG)
    btg = yf.Ticker("BPAC3.SA")
    hist_btg = btg.history(start="2022-01-01",end="2022-09-23")['Close']
    norm_btg = hist_btg/hist_btg.iloc[10]

    st.subheader('Preço da ação')
    st.area_chart(hist_btg)
    st.subheader('Valorização da ação')
    st.line_chart(norm_btg)
    st.subheader('Tabela geral da ação - mês de setembro')
    st.table(hist_btg)

if opcoes == "Bradesco":
    imageBTG = Image.open(urlopen('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Banco_Bradesco_logo_%28horizontal%29.png/250px-Banco_Bradesco_logo_%28horizontal%29.png'))
    st.image(imageBTG)
    Bradesco = yf.Ticker("BBDC3.SA")
    hist_bradesco = Bradesco.history(start="2022-01-01",end="2022-09-23")['Close']
    norm_brad = hist_bradesco/hist_bradesco.iloc[10]

    st.subheader('Preço da ação')
    st.area_chart(hist_bradesco)
    st.subheader('Valorização da ação')
    st.line_chart(norm_brad)
    st.subheader('Tabela geral da ação - mês de setembro')
    st.table(hist_bradesco)
    
if opcoes == "Compare os três":
    acoes = ['BBDC3.SA','BPAC3.SA','BBAS3.SA']

    data = yf.download(acoes,start="2022-01-01",end="2022-09-23")['Close']
    normalizado = data/data.iloc[0]

    st.subheader('Gráfico dos valores nominais')
    st.area_chart(data)
    st.subheader('Gráfico dos valores normalizados')
    st.line_chart(normalizado)
    st.subheader('Tabela Geral do mês de setembro')
    st.table(data)