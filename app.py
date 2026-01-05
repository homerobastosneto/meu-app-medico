import streamlit as st

st.set_page_config(page_title="Meu App Médico")

st.title("👨‍⚕️ App Médico no Ar!")
st.write("Se você está vendo isso, a configuração funcionou perfeitamente.")
st.success("Parabéns pelo primeiro deploy!")

if st.button("Clique aqui"):
    st.balloons()
