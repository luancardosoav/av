import streamlit as st

st.set_page_config(page_title="VOID Assistant", layout="wide")

st.title("🎬 VOID Assistant – Ferramenta Interna")

menu = st.sidebar.radio("Escolha uma funcionalidade:", ["🧾 Orçamentos", "📘 Playbook", "📋 Roteiros"])

# Aba: Orçamentos
if menu == "🧾 Orçamentos":
    st.header("Gerador de Orçamentos Automáticos")
    st.write("Cole abaixo o texto ou transcrição do áudio enviado pelo cliente. O sistema vai gerar um orçamento baseado em exemplos anteriores.")
    client_input = st.text_area("📥 Texto enviado pelo cliente:")
    if st.button("Gerar orçamento"):
        st.success("🔧 Em breve: Geração automática via GPT com base nos orçamentos armazenados.")

# Aba: Playbook
elif menu == "📘 Playbook":
    st.header("Respostas para Dúvidas e Objeções")
    st.write("Insira a dúvida, objeção ou pergunta do cliente. A ferramenta vai responder como se fosse você.")
    question_input = st.text_area("💬 Dúvida do cliente:")
    if st.button("Gerar resposta"):
        st.success("🔧 Em breve: Resposta baseada no playbook personalizado.")

# Aba: Roteiros
elif menu == "📋 Roteiros":
    st.header("Criação de Roteiros com Perguntas Guiadas")
    st.write("Responda às perguntas abaixo para gerar um roteiro com base no estilo VOID.")
    tema = st.text_input("🎯 Qual o tema do vídeo?")
    objetivo = st.selectbox("🎯 Qual o objetivo do vídeo?", ["Gerar autoridade", "Converter em vendas", "Engajamento", "Outro"])
    tom = st.selectbox("🗣️ Qual o tom da comunicação?", ["Inspirador", "Confiante", "Leve", "Direto", "Outro"])
    publico = st.text_input("👥 Quem é o público-alvo?")
    if st.button("Gerar roteiro"):
        st.success("🔧 Em breve: Roteiro gerado com base nas respostas.")
