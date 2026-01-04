import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURAÇÃO DA PÁGINA (Deve ser sempre a primeira linha de comando Streamlit) ---
st.set_page_config(page_title="Gestão Comercial", layout="wide")
st.title("📊 Sistema de Gestão Integrado")

# --- 2. CONFIGURAÇÃO DE ARQUIVOS ---
ARQUIVO_STOCK = 'stock.csv'
ARQUIVO_VENDAS = 'vendas.csv'
ARQUIVO_CLIENTES = 'clientes.csv'

# --- 3. FUNÇÕES UTILITÁRIAS (O Cérebro) ---
def carregar_dados(arquivo, colunas_padrao):
    if os.path.exists(arquivo):
        return pd.read_csv(arquivo)
    return pd.DataFrame(columns=colunas_padrao)

# --- 4. MENU LATERAL ---
menu = st.sidebar.selectbox("Navegar", 
    ["Gestão de Stock", "Registar Venda", "Clientes", "Calculadora"])

# ==================================================
# BLOCO 1: GESTÃO DE STOCK
# ==================================================
if menu == "Gestão de Stock":
    st.header("📦 Inventário")
    
    # Carregar dados
    df_stock = carregar_dados(ARQUIVO_STOCK, ['Produto', 'Quantidade', 'Preco'])
    
    # Inputs (Substitui o 'input' do terminal)
    c1, c2, c3 = st.columns(3)
    prod = c1.text_input("Produto")
    qtd = c2.number_input("Qtd", min_value=1, step=1)
    preco = c3.number_input("Preço (€)", min_value=0.0, format="%.2f")

    # Botão de Ação
    if st.button("Salvar Produto"):
        if prod: # Verifica se escreveu um nome
            novo = pd.DataFrame({'Produto': [prod], 'Quantidade': [qtd], 'Preco': [preco]})
            df_stock = pd.concat([df_stock, novo], ignore_index=True)
            df_stock.to_csv(ARQUIVO_STOCK, index=False)
            st.success("Produto guardado!") # Correção: era st.sucess
            st.rerun()
        else:
            st.warning("O nome do produto é obrigatório.")
        
    st.dataframe(df_stock, use_container_width=True)

# ==================================================
# BLOCO 2: VENDAS (Com Dashboard Corrigido)
# ==================================================
elif menu == "Registar Venda":
    st.header("🛒 Caixa Registadora")
    
    df_stock = carregar_dados(ARQUIVO_STOCK, ['Produto', 'Quantidade', 'Preco'])
    df_vendas = carregar_dados(ARQUIVO_VENDAS, ['Produto', 'Qtd_Venda', 'Total', 'Data'])
    
    # --- DASHBOARD (Correção: Faltava mostrar os números) ---
    if not df_vendas.empty:
        total_ganho = df_vendas['Total'].sum()
        total_qtd = df_vendas['Qtd_Venda'].sum()
        
        m1, m2 = st.columns(2)
        m1.metric("Receita Total", f"{total_ganho:.2f} €")
        m2.metric("Produtos Vendidos", f"{total_qtd:.0f}")
        st.divider()
    # -------------------------------------------------------

    if df_stock.empty:
        st.warning("O stock está vazio. Adiciona produtos primeiro!")
    else:
        # Seleção do produto
        lista_produtos = df_stock['Produto'].unique()
        produto_selecionado = st.selectbox("Escolha o Produto", lista_produtos)
        
        # Procura automática de preço (Lógica de Integração)
        filtro_linha = df_stock[df_stock['Produto'] == produto_selecionado]
        preco_unitario = filtro_linha['Preco'].values[0]

        st.info(f"Preço Unitário: **{preco_unitario:.2f} €**")

        qtd_venda = st.number_input("Quantidade a Vender", min_value=1)

        total = preco_unitario * qtd_venda
        st.write(f"### Total a Receber: {total:.2f} €")
        
        if st.button("Confirmar Venda"):
            nova_venda = pd.DataFrame({
                'Produto': [produto_selecionado], 
                'Qtd_Venda': [qtd_venda], 
                'Total': [total], 
                'Data': [pd.Timestamp.now()]
            })
            
            df_vendas = pd.concat([df_vendas, nova_venda], ignore_index=True)
            df_vendas.to_csv(ARQUIVO_VENDAS, index=False)
            st.success("Venda registada!")
            st.rerun()

    st.subheader("Histórico de Vendas")
    st.dataframe(df_vendas, use_container_width=True)

# ==================================================
# BLOCO 3: CLIENTES
# ==================================================
elif menu == "Clientes":
    st.header("👥 Carteira de Clientes")
    
    df_clientes = carregar_dados(ARQUIVO_CLIENTES, ['Nome', 'Telefone', 'Email', 'Obs'])
    
    with st.form("form_cliente"):
        st.write("### Adicionar Novo Cliente")
        c_nome = st.text_input("Nome Completo")
        c1, c2 = st.columns(2)
        c_tel = c1.text_input("Telefone")
        c_email = c2.text_input("Email")
        c_obs = st.text_area("Observações")
        
        enviado = st.form_submit_button("Guardar Cliente")
        
        if enviado:
            if c_nome == "": 
                st.error("O nome é obrigatório!")
            else:
                novo_cliente = pd.DataFrame([{
                    'Nome': c_nome, 'Telefone': c_tel, 'Email': c_email, 'Obs': c_obs
                }])
                df_clientes = pd.concat([df_clientes, novo_cliente], ignore_index=True)
                df_clientes.to_csv(ARQUIVO_CLIENTES, index=False)
                st.success("Cliente adicionado!")
                st.rerun()
                
    st.dataframe(df_clientes, use_container_width=True)

# ==================================================
# BLOCO 4: CALCULADORA
# ==================================================
elif menu == "Calculadora":
    st.header("🧮 Simulação de Preços")
    # Aqui integramos a tua primeira função 'def calculadora()', mas visualmente
    
    col1, col2 = st.columns(2)
    with col1:
        custo = st.number_input("Custo do Produto (€)", min_value=0.0, value=10.0)
    with col2:
        margem = st.number_input("Margem (%)", min_value=0.0, value=30.0)
    
    st.divider()
    
    # A tua lógica matemática original:
    preco_venda = custo * (1 + (margem / 100))
    lucro = preco_venda - custo
    
    c1, c2 = st.columns(2)
    c1.metric("Preço de Venda", f"{preco_venda:.2f} €")
    c2.metric("Lucro Previsto", f"{lucro:.2f} €", delta="Lucro")