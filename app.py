import pandas as pd
import streamlit as st
import plotly.express as px

# Título
st.title("📊 Dashboard de Vendas")

# Carregar dados
df = pd.read_csv("dados.csv")
df["data"] = pd.to_datetime(df["data"])

# KPIs
faturamento = df["valor"].sum()
st.metric("💰 Faturamento Total", f"R$ {faturamento}")

# Vendas por produto
vendas_produto = df.groupby("produto")["valor"].sum().reset_index()

fig_produto = px.bar(vendas_produto, x="produto", y="valor", title="Vendas por Produto")
st.plotly_chart(fig_produto)

# Vendas por mês
df["mes"] = df["data"].dt.to_period("M").astype(str)
vendas_mes = df.groupby("mes")["valor"].sum().reset_index()

fig_mes = px.line(vendas_mes, x="mes", y="valor", title="Vendas por Mês")
st.plotly_chart(fig_mes)
