import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Teste GPT")

st.title("✅ Teste de Conexão com a OpenAI")

# Chave da OpenAI
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Entrada do usuário
pergunta = st.text_input("💬 O que você quer perguntar para o GPT?")

if st.button("Perguntar"):
    if openai_api_key and pergunta:
        try:
            client = OpenAI(api_key=openai_api_key)
            resposta = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": pergunta}],
                temperature=0.7
            )
            st.subheader("🧠 Resposta do GPT:")
            st.write(resposta.choices[0].message.content)
        except Exception as e:
            st.error(f"❌ Erro: {e}")
    else:
        st.warning("Preencha a chave da OpenAI e a pergunta.")
