import streamlit as st

# Configuração da página para um visual profissional e largo
st.set_page_config(page_title="Guia de Comunicação Executiva MV", layout="wide", page_icon="📈")

# Estilo customizado para os "Cards de Farol"
st.markdown("""
    <style>
    .report-card { padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 1px solid #ddd; }
    .critical { background-color: #ffe6e6; border-left: 10px solid #ff4b4b; }
    .success { background-color: #e6ffed; border-left: 10px solid #28a745; }
    .warning { background-color: #fff9e6; border-left: 10px solid #ffc107; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏆 Mentor de Comunicação: Projetos de Implantação MV")
st.markdown("---")

# Painel Lateral - Dashboard de Contexto Real (Projeto INS)
st.sidebar.header("📊 Painel de Controle (Dados Reais)")
st.sidebar.error("🚨 Evasão de Receita: R$ 12.1 MM [cite: 106]")
st.sidebar.warning("🕒 Atraso no Go-Live: 164 dias [cite: 200]")
st.sidebar.info("📅 Próximo Marco: 12/01/26 (Subprojeto Green) [cite: 202]")

# Menu de Seleção de Cenários baseados no documento
cenario = st.selectbox(
    "Selecione o Cenário de Crise para ver o Guia de Notificação:",
    [
        "1. Atraso Crítico no Go-Live (OnePass/Financeiro)",
        "2. Retrabalho e Pedidos Fora de Escopo",
        "3. Ofensor Interno (Universidade MV)",
        "4. Pendência de Escopo e Documentação (EFs/Fábrica)",
        "5. Impasse Técnico em Mercado Internacional"
    ]
)

# Renderização dos Cenários
if cenario == "1. Atraso Crítico no Go-Live (OnePass/Financeiro)":
    st.header("Cenário: Falha Técnica impedindo o Faturamento")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("❌ Abordagem 'Analista de Sistemas'")
        st.markdown("""
        **Assunto:** Erros no OnePass e Gaat.
        
        "O OnePass apresentou erros recorrentes na homologação do cliente[cite: 110, 151]. O GAAT não validou as telas devido a inconsistências na versão[cite: 130, 141]. 
        Precisamos que a fábrica corrija para tentarmos o Go-Live de novo."
        """)
        
    with col2:
        st.subheader("✅ Abordagem 'Gerente de Negócio'")
        st.markdown(f"""
        **Assunto: [STATUS: CRÍTICO 🔴] Suspensão de Receita R$ 12M | Bloqueio OnePass**
        
        **Impacto Financeiro:** Perda de faturamento de **R$ 314 mil/mês**[cite: 91, 134]. Evasão acumulada atingiu **R$ 12.1 milhões**[cite: 106].
        
        **O Problema:** Reincidência de erros técnicos no OnePass impediu a assinatura do aceite pelo cliente (GAAT)[cite: 110, 141].
        
        **Ação Requerida:** Priorização máxima na Fábrica para correção até 14/11, garantindo o faturamento de Dezembro[cite: 112].
        """)

elif cenario == "2. Retrabalho e Pedidos Fora de Escopo":
    st.header("Cenário: Cliente solicitando mudanças após homologação")
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("⚠️ O que evitar: Aceitar sem notificar o custo.")
        st.markdown("O cliente pediu para mudar o Centro de Custo na funcionalidade CeosGo[cite: 10, 24]. Vamos tentar atender para não atrasar.")
        
    with col2:
        st.success("💎 Prática Recomendada: Suspensão por Retrabalho")
        st.markdown("""
        **Comunicação:** "Informamos a suspensão imediata das atividades de configuração devido a novas exigências do cliente que geram retrabalho e perda de horas[cite: 204]. 
        Retomaremos mediante aprovação de novo acordo comercial ou pagamento adicional[cite: 204]."
        """)

elif cenario == "3. Ofensor Interno (Universidade MV)":
    st.header("Cenário: Dependência de outras áreas da MV")
    st.warning("Aqui o analista deve dar visibilidade ao 'gargalo' interno sem ser evasivo.")
    st.markdown(f"""
    **Estrutura de Notificação:**
    * **O Ofensor:** Universidade MV[cite: 205].
    * **O Conflito:** Necessidade de plataforma em espanhol vs. Prazo de entrega apenas para Junho/26[cite: 205].
    * **Impacto:** Inviabiliza o cronograma de treinamento do projeto INS[cite: 205].
    * **Escalada:** Reunião extraordinária entre Gestão de Projetos e Reitoria da Universidade para alinhamento[cite: 211].
    """)

elif cenario == "4. Pendência de Escopo e Documentação (EFs/Fábrica)":
    st.header("Cenário: Atraso na entrega de Especificações Funcionais (EFs)")
    st.markdown(f"""
    **Como reportar a 'Bola de Neve' de TI:**
    1. **Fato:** Existem 17 pacotes de especificações técnicas para envio até 28/11[cite: 47].
    2. **Status:** Atraso na validação e devolução por parte da Fábrica[cite: 206].
    3. **Risco:** Impacto direto no cronograma geral e multa por descumprimento de prazos da licitação[cite: 72, 209].
    """)

elif cenario == "5. Impasse Técnico em Mercado Internacional":
    st.header("Cenário: Divergência de Escopo e Notificação Formal (Costa Rica)")
    st.markdown(f"""
    **Análise de Crise (One Pass License):**
    * **O Impasse:** Cliente recusa liberar pagamento por falta da tela de 'Gerenciamento de Usuários'[cite: 166].
    * **A Divergência:** Protótipo de Junho/25 previa a tela, mas a TI atual alega inviabilidade[cite: 168].
    * **Impacto:** Retenção imediata de **US$ 177 mil**[cite: 171].
    * **Solução:** O time de Tecnologia deve analisar a divergência e o jurídico (Jean Karr) deve emitir resposta formal para resguardo legal[cite: 173, 174].
    """)

# Seção de Melhores Práticas de Mercado
st.divider()
st.header("📚 Referências Bibliográficas e Boas Práticas")
cols = st.columns(5)
refs = [
    ("The Minto Pyramid", "Hierarquia de ideias: Resposta primeiro, detalhes depois."),
    ("PMBOK 7th Ed", "Foco na entrega de VALOR, não apenas em tarefas."),
    ("Crucial Conversations", "Como tratar impasses de US$ 177k sem romper a relação."),
    ("HBR Guide to PM", "Comunicação visual de riscos financeiros para C-Levels."),
    ("Radical Candor", "Franqueza direta: Diga a verdade sobre o atraso de 164 dias.")
]
for i, (title, desc) in enumerate(refs):
    cols[i].info(f"**{title}**\n\n{desc}")