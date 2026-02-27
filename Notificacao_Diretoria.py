import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Configuração da página para visual executivo
st.set_page_config(
    page_title="Repositório de Notificações Executivas - Ecossistema MV", 
    layout="wide", 
    page_icon="🏢"
)

# --- CONEXÃO E CARREGAMENTO DE DADOS ---
# O Streamlit tentará conectar ao Sheets via secrets; se falhar, usaremos a simulação.
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
except Exception:
    # --- SIMULAÇÃO COM DADOS REAIS DO PROJETO INS (Para teste visual) ---
    df = pd.DataFrame([
        {
            "Programa": "INS Costa Rica",
            "Data_Notificacao": "2025-09-12",
            "Status": "CRÍTICO 🔴",
            "Resumo_Situacao": "Cancelamento do Go Live de 16/09 devido a erros no OnePass e falta de homologação do cliente[cite: 88, 110].",
            "Evasao_Receita": "R$ 12.100.000,00.",
            "Prazo": "24/11/25[cite: 112].",
            "Receita_Atual": "R$ 314.000,00[cite: 111].",
            "Custo_Total": "R$ 2.5 MM (Est.)",
            "Atrasado": "SIM",
            "Recomendacao_1": "Elaborar resposta formal para assegurar resguardo legal da MV[cite: 174, 193].",
            "Recomendacao_2": "Suspensão imediata em caso de novos pedidos que gerem retrabalho.",
            "Grau_Impacto": "CRÍTICO",
            "O_Que_Impacta": "Faturamento de 50% da subscrição e módulos CeosGo[cite: 63, 167].",
            "Resumo_Consolidado": "Go Live de 16/09 cancelado. Evasão de receita acumulada em R$ 12.1M por falhas recorrentes no OnePass[cite: 92, 106]."
        },
        {
            "Programa": "INS Costa Rica",
            "Data_Notificacao": "2025-10-31",
            "Status": "SUSPENSO 🟡",
            "Resumo_Situacao": "Identificado erro na funcionalidade OnePass License, resultando no cancelamento dos Go Lives previstos para outubro[cite: 141].",
            "Evasao_Receita": "R$ 12.100.000,00[cite: 147].",
            "Prazo": "TBD",
            "Receita_Atual": "R$ 314.000,00",
            "Custo_Total": "R$ 2.5 MM",
            "Atrasado": "SIM",
            "Recomendacao_1": "Notificar cliente formalmente pelo atraso na validação das documentações[cite: 138].",
            "Recomendacao_2": "Priorizar nova homologação com o GAAT para assinatura final[cite: 144].",
            "Grau_Impacto": "ALTO",
            "O_Que_Impacta": "Faturamento da subscrição Flowti e CeosGo[cite: 142, 147].",
            "Resumo_Consolidado": "Replanejamento de Go-Live devido a erros de licença; faturamento de outubro não realizado[cite: 141, 142]."
        }
    ])

# --- INTERFACE ---
st.title("📊 Repositório de Notificações para Diretoria")
st.markdown("Consulta histórica de programas e monitoramento de impactos financeiros.")

# --- SIDEBAR: FILTROS E INDICADORES FIXOS ---
st.sidebar.header("🔍 Filtros de Consulta")
programas_disponiveis = df["Programa"].unique()
programa_selecionado = st.sidebar.selectbox("Selecione o Programa:", programas_disponiveis)

# Filtragem Dinâmica
dados_programa = df[df["Programa"] == programa_selecionado].sort_values(by="Data_Notificacao", ascending=False)

if not dados_programa.empty:
    recente = dados_programa.iloc[0]
    
    # Sidebar Metrics
    st.sidebar.divider()
    st.sidebar.markdown(f"**Data da Última Notificação:** {recente['Data_Notificacao']}")
    st.sidebar.markdown(f"**Responsável Técnico:** José Alexandre [cite: 207]")

    # --- PAINEL DE CONTROLE (INDICADORES SUPERIORES) ---
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Status Atual", recente["Status"])
    with col2:
        atrasado_label = "🚨 SIM" if str(recente["Atrasado"]).upper() == "SIM" else "✅ NÃO"
        st.metric("Atrasado?", atrasado_label)
    with col3:
        st.metric("Evasão de Receita", recente["Evasao_Receita"])
    with col4:
        st.metric("Grau de Impacto", recente["Grau_Impacto"])

    # --- CONTEÚDO DA NOTIFICAÇÃO ---
    st.divider()
    c1, c2 = st.columns([2, 1])

    with c1:
        st.subheader("📝 Resumo Consolidado para Diretoria")
        st.info(recente["Resumo_Consolidado"])
        
        st.markdown("### 🔍 Detalhamento da Situação")
        st.write(recente["Resumo_Situacao"])
        
        st.markdown(f"**Impacto Principal:** {recente['O_Que_Impacta']}")

    with c2:
        st.markdown("### 💰 Resumo Financeiro")
        st.write(f"**Receita Mensal em Risco:** {recente['Receita_Atual']} [cite: 111, 152]")
        st.write(f"**Custo Estimado do Programa:** {recente['Custo_Total']}")
        st.write(f"**Prazo (Deadline):** {recente['Prazo']} [cite: 112, 153]")
        
        st.divider()
        st.markdown("### ⚖️ Decisões Recomendadas")
        st.warning(f"**1.** {recente['Recomendacao_1']}")
        st.warning(f"**2.** {recente['Recomendacao_2']}")

    # --- HISTÓRICO DE EVOLUÇÃO ---
    st.divider()
    with st.expander("📂 Histórico de Evolução (Consultar logs anteriores)"):
        st.dataframe(
            dados_programa[["Data_Notificacao", "Status", "Evasao_Receita", "Resumo_Consolidado"]],
            use_container_width=True, 
            hide_index=True
        )
else:
    st.error("Nenhum registro encontrado para este programa.")

st.sidebar.divider()
st.sidebar.caption("Sincronizado via Google Sheets | Dados Projeto INS")
