import streamlit as st

# Configuração da Página (Design Clean)
st.set_page_config(page_title="Check-up Fiscal Médico", layout="centered")

# Título e Promessa
st.title("🩺 Check-up Fiscal Médico")
st.write("Descubra quanto dinheiro você deixa na mesa por não otimizar seu Livro Caixa.")
st.write("---")

# 1. Inputs (Dados do Médico)
st.subheader("1. Seus Rendimentos")
renda_mensal = st.number_input("Renda Média Mensal (PF/Plantões)", min_value=0.0, value=20000.0, step=1000.0)

st.subheader("2. Despesas que você tem (mas talvez não deduza)")
st.caption("Preencha com a média mensal aproximada:")

col1, col2 = st.columns(2)

with col1:
    crm = st.number_input("Mensalidade CRM / Associações", value=0.0)
    congressos = st.number_input("Cursos e Congressos Médicos", value=0.0)
    livros = st.number_input("Livros Técnicos/Softwares Médicos", value=0.0)

with col2:
    consultorio = st.number_input("Aluguel/Condomínio Consultório", value=0.0)
    vestuario = st.number_input("Vestuário (Jaleco/Branco)", value=0.0)
    outros = st.number_input("Outras despesas dedutíveis", value=0.0)

# Cálculo Simples (Lógica Tributária Resumida para Demo)
# Tabela progressiva IR 2024/2025 (simplificada para o exemplo)
def calcular_ir(base_calculo):
    deducao = 0
    aliquota = 0
    
    if base_calculo <= 2259.20:
        return 0
    elif base_calculo <= 2826.65:
        aliquota = 0.075
        deducao = 169.44
    elif base_calculo <= 3751.05:
        aliquota = 0.15
        deducao = 381.44
    elif base_calculo <= 4664.68:
        aliquota = 0.225
        deducao = 662.77
    else:
        aliquota = 0.275
        deducao = 896.00
    
    return (base_calculo * aliquota) - deducao

# Cenário 1: Sem dedução
imposto_sem_deducao = calcular_ir(renda_mensal)

# Cenário 2: Com dedução (Livro Caixa Otimizado)
total_deducoes = crm + congressos + livros + consultorio + vestuario + outros
base_otimizada = renda_mensal - total_deducoes
if base_otimizada < 0: base_otimizada = 0
imposto_com_deducao = calcular_ir(base_otimizada)

# Resultados
economia_mensal = imposto_sem_deducao - imposto_com_deducao
economia_anual = economia_mensal * 12

st.write("---")
if st.button("CALCULAR MINHA ECONOMIA 💰", type="primary"):
    st.success(f"Possível Economia Anual: R$ {economia_anual:,.2f}")
    
    col_a, col_b = st.columns(2)
    col_a.metric(label="Imposto Atual (Estimado)", value=f"R$ {imposto_sem_deducao:,.2f}")
    col_b.metric(label="Imposto Otimizado", value=f"R$ {imposto_com_deducao:,.2f}", delta=f"- R$ {economia_mensal:,.2f}")

    st.warning("**Atenção, Doutor(a):** Esses valores poderiam estar no seu bolso legalmente via Carnê-Leão.")
    
    # Call to Action (Onde você vende)
    st.info("Quer o Guia Passo a Passo de como lançar isso e a Lista Completa de 50 itens dedutíveis para médicos?")
    st.markdown("[👉 **Baixar o Kit Blindagem Médica por R$ 47,00**](#)")
