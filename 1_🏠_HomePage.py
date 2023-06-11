import mysql.connector
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Dash Madamy",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def criarDash():
    st.header("🎉 Bem-vindo ao Dashboard da Madamy Acessórios! 🛍️")
    st.markdown("---")

    st.markdown(
        "🎉🛍️ Bem-vindo(a) à Madamy Acessórios! 🛍️🎉\n\n"
        "Aqui na Madamy, sabemos que os acessórios certos podem transformar um visual comum em algo verdadeiramente extraordinário! ✨\n\n"
        "📊 Com o nosso exclusivo Dashboard, você poderá acompanhar todas as informações essenciais sobre as suas lojas e produtos. Com estatísticas atualizadas em tempo real, monitorar o desempenho de vendas nunca foi tão intuitivo e eficiente. 📈\n\n"
        "Nossos gráficos interativos fornecem uma visão abrangente das vendas diárias, semanais e mensais, ajudando você a identificar tendências e oportunidades de crescimento.\n\n"
        "💻🚀 O Dashboard da Madamy Acessórios foi desenvolvido com a mais alta tecnologia para oferecer uma experiência de usuário excepcional. Com uma interface amigável e responsiva, você pode acessar os dados da sua loja de qualquer lugar, a qualquer momento. Basta alguns cliques para desbloquear insights valiosos e tomar decisões estratégicas embasadas em dados concretos!"
    )


criarDash()
