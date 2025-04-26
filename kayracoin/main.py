import streamlit as st
import requests

Response=requests.get("https://api.coinlore.net/api/tickers/")

veri=Response.json()

coinlist=veri["data"]

coinler={}

for coin in coinlist:

  coinler.update({coin["symbol"]:float(coin["price_usd"])})

coinisimleri=list(coinler.keys())#coin isimleri aldım
coin1=st.sidebar.selectbox("elinizdeki coin",coinisimleri)#eldeki coin i seçtim
adet=st.sidebar.number_input("elinizdeki miktar")#adet girdim
coin2=st.sidebar.selectbox("hedef coin",coinisimleri)#hedef coin seçtim
coin1fiyat=coinler[coin1]#
coin2fiyat=coinler[coin2]

sonuc=(coin1fiyat/coin2fiyat)*adet

st.write(adet,"adet",coin1,sonuc,"adet",coin2,"değerindedir")
