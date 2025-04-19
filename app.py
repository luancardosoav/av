import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="VOID Assistant", layout="wide")
st.title("📋 VOID Assistant – Roteirista Inteligente")

# Chave API via secrets (não aparece na interface)
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Função auxiliar para campos com "Outro"
def handle_outro(selecao, label):
    if selecao == "Outro":
        return st.text_input(f"✍️ Especifique o {label.lower()}")
    return selecao

# Formulário de briefing
st.subheader("Preencha o briefing para gerar 3 roteiros diferentes")
tema = st.text_input("🎯 Tema do vídeo")
objetivo_raw = st.selectbox("🎯 Objetivo do vídeo", ["Gerar autoridade", "Converter em vendas", "Engajamento", "Outro"])
objetivo = handle_outro(objetivo_raw, "objetivo")

tom_raw = st.selectbox("🗣️ Tom da comunicação", ["Inspirador", "Confiante", "Leve", "Direto", "Outro"])
tom = handle_outro(tom_raw, "tom")

publico = st.text_input("👥 Público-alvo")

formato_raw = st.selectbox("🎬 Formato do vídeo", ["Reels", "Story", "YouTube Shorts", "Institucional", "Outro"])
formato = handle_outro(formato_raw, "formato")

tempo_raw = st.selectbox("⏱️ Duração estimada", ["Até 30s", "1 minuto", "2-3 minutos", "Outro"])
tempo = handle_outro(tempo_raw, "duração")

# Geração de roteiros via OpenRouter
def gerar_roteiros():
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openai_api_key
    )

    prompt = f"""
Tu é um roteirista experiente chamado VideoCraft, especialista em vídeos curtos com alta conversão para empresas e marcas pessoais.
Teu estilo mistura storytelling, linguagem acessível e autoridade, com foco nos seguintes blocos:
🎯 Gancho / 💥 Dor / 🧠 Autoridade / 🧩 Micro-story / 🛒 CTA.

Gere 3 versões diferentes de roteiros com base neste briefing:

Tema: {tema}
Objetivo: {objetivo}
Tom: {tom}
Público-alvo: {publico}
Formato: {formato}
Duração estimada: {tempo}

Cada versão deve ser direta, com frases curtas e impacto emocional. Use emojis e títulos para destacar os blocos.
"""

    resposta = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )

    return resposta.choices[0].message.content

# Botão de gerar
if st.button("🎬 Gerar Roteiros"):
    if all([openai_api_key, tema, objetivo, tom, publico, formato, tempo]):
        with st.spinner("Criando roteiros com VideoCraft..."):
            try:
                resultado = gerar_roteiros()
                st.markdown("### 🧠 Roteiros Gerados")
                st.markdown(resultado)
            except Exception as e:
                st.error(f"Erro ao gerar roteiros: {e}")
    else:
        st.warning("Preencha todos os campos antes de gerar.")
