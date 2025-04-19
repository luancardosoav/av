import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="VOID Assistant – VideoCraft", layout="centered")
st.title("🎬 VOID Assistant – Roteirista Profissional")

st.markdown("Crie roteiros estratégicos para vídeos de alto impacto. Preencha o briefing abaixo:")

# Chave da API (via secrets)
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Utilitário para lidar com a opção "Outro"
def handle_outro(opcao, label):
    if opcao == "Outro":
        return st.text_input(f"✍️ Especifique o {label.lower()}")
    return opcao

# Formulário
with st.form("briefing_form"):
    tema = st.text_input("🎯 Tema central do vídeo")

    objetivo_raw = st.selectbox("🎯 Objetivo principal do vídeo", [
        "Gerar autoridade", "Atrair novos clientes", "Educar o público",
        "Engajar seguidores", "Posicionar a marca", "Converter leads em clientes", "Outro"
    ])
    objetivo = handle_outro(objetivo_raw, "objetivo")

    tom_raw = st.selectbox("🗣️ Tom da comunicação", [
        "Confiante", "Inspirador", "Educativo", "Direto", "Provocador", "Divertido", "Emocional", "Outro"
    ])
    tom = handle_outro(tom_raw, "tom")

    publico = st.text_input("👥 Descreva brevemente o público-alvo")

    formato_raw = st.selectbox("🎬 Formato do vídeo", [
        "Reels (Instagram)", "Shorts (YouTube)", "Stories", "Vídeo institucional", "Anúncio (ads)", "VSL (vídeo de vendas)", "Outro"
    ])
    formato = handle_outro(formato_raw, "formato")

    duracao_raw = st.selectbox("⏱️ Duração estimada", [
        "Até 15 segundos", "Até 30 segundos", "1 minuto", "2-3 minutos", "Outro"
    ])
    duracao = handle_outro(duracao_raw, "duração")

    submit = st.form_submit_button("🎬 Gerar Roteiros")

# Função para gerar os roteiros com prompt aprimorado
def gerar_roteiros():
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openai_api_key
    )

    prompt = f"""
Você é um roteirista profissional chamado VideoCraft, especializado em criação de roteiros curtos e de alto impacto para vídeos voltados a empresas, marcas pessoais e criadores de conteúdo.

Todas as respostas devem ser escritas em português do Brasil, com linguagem acessível, estratégica e compatível com o público-alvo informado.

O roteiro deve seguir a seguinte estrutura:
🎯 Gancho – Uma frase forte que capture a atenção imediatamente.
💥 Dor – Um problema real ou comum do público.
🧠 Autoridade / Solução – Mostre domínio sobre o assunto e a proposta de valor.
🧩 Micro-story ou analogia – Um exemplo rápido, real ou simbólico, que ilustra a transformação.
🛒 Chamada para ação – Um CTA sutil, direto e persuasivo.

Instruções específicas:
- Crie 3 versões diferentes do roteiro, com variações no tom, construção ou abordagem.
- Use frases curtas e de fácil assimilação.
- Evite o uso exagerado de emojis (limite-se aos títulos dos blocos).
- A comunicação deve ser estratégica, pensada para conversão e engajamento.
- O texto final deve parecer escrito por um ser humano com domínio do tema.

Baseie-se neste briefing:

Tema: {tema}
Objetivo do vídeo: {objetivo}
Tom desejado: {tom}
Público-alvo: {publico}
Formato do vídeo: {formato}
Duração estimada: {duracao}
"""

    resposta = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )

    return resposta.choices[0].message.content

# Exibir resultado
if submit:
    if all([openai_api_key, tema, objetivo, tom, publico, formato, duracao]):
        with st.spinner("Gerando roteiros com VideoCraft..."):
            try:
                resultado = gerar_roteiros()
                st.markdown("### 🧠 Roteiros Gerados")
                st.markdown(resultado)
            except Exception as e:
                st.error(f"Erro ao gerar os roteiros: {e}")
    else:
        st.warning("Preencha todos os campos antes de gerar.")
