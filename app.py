import streamlit as st

st.set_page_config(page_title="VOID Assistant", layout="wide")

st.title("🎬 VOID Assistant – Ferramenta Interna")

menu = st.sidebar.radio("Escolha uma funcionalidade:", [
    "🧾 Orçamentos",
    "📘 Playbook",
    "📋 Roteiros",
    "📈 Análise de Conteúdo",
    "🧠 Ideias de Conteúdo por Segmento",
    "🗓️ Planejador de Grade de Conteúdo"
])

# Aba: Orçamentos
if menu == "🧾 Orçamentos":
    st.header("Gerador de Orçamentos Automáticos")
    st.write("Cole abaixo o texto ou transcrição do áudio enviado pelo cliente. O sistema vai gerar um orçamento baseado em exemplos anteriores.")
    client_input = st.text_area("📥 Texto enviado pelo cliente:")
    tipo_servico = st.text_input("📦 Tipo de serviço (ex: institucional, reels, cobertura de evento)")
    prazo = st.text_input("⏳ Prazo desejado (ex: 7 dias, urgente, etc.)")
    nivel = st.selectbox("💰 Nível de produção", ["Básico", "Intermediário", "Premium"])
    if st.button("Gerar orçamento"):
        st.success("🔧 Em breve: Geração automática via GPT com base nos orçamentos armazenados.")

# Aba: Playbook
elif menu == "📘 Playbook":
    st.header("Respostas para Dúvidas e Objeções")
    st.write("Insira a dúvida, objeção ou pergunta do cliente. A ferramenta vai responder como se fosse você.")
    question_input = st.text_area("💬 Dúvida ou objeção do cliente:")
    categoria = st.selectbox("📂 Categoria da objeção", ["Preço", "Prazo", "Resultado", "Entrega", "Outro"])
    tom_resposta = st.selectbox("🗣️ Tom da resposta", ["Confiante", "Empático", "Objetivo", "Informativo"])
    if st.button("Gerar resposta"):
        st.success("🔧 Em breve: Resposta baseada no playbook personalizado.")

# Aba: Roteiros
elif menu == "📋 Roteiros":
    # Aba: Roteirista Inteligente
st.header("📋 Roteirista Inteligente VOID")
st.write("Responda às perguntas abaixo para gerar **3 versões diferentes** de um roteiro com base no estilo VOID.")

# Formulário do briefing
tema = st.text_input("🎯 Qual o tema do vídeo?")
objetivo = st.selectbox("🎯 Qual o objetivo do vídeo?", ["Gerar autoridade", "Converter em vendas", "Engajamento", "Outro"])
tom = st.selectbox("🗣️ Qual o tom da comunicação?", ["Inspirador", "Confiante", "Leve", "Direto", "Outro"])
publico = st.text_input("👥 Quem é o público-alvo?")
formato = st.selectbox("🎬 Formato do vídeo", ["Reels", "Story", "YouTube Shorts", "Institucional", "Outro"])
tempo = st.selectbox("⏱️ Duração estimada", ["Até 30s", "1 minuto", "2-3 minutos", "Outro"])

# Chave da API da OpenAI
openai_api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else st.text_inputsk-proj-DBfgfPaY8_eMlF91d22-17vnEH1-CBYhBc5XKFSyZYdmj-s9HyXt955PnRGbGHfBwllClCkRStT3BlbkFJpMdHPlL5mMpyORiYEZW1voLLQN4ycWw8hOAranF56x6nKl6jU-t7xaMonzd5aSjBMVRDZGOg0A", type="password")

# Função para gerar os roteiros via GPT
def gerar_roteiros():
    prompt_base = f"""
Tu é um roteirista experiente chamado VideoCraft, especialista em vídeos curtos com alta conversão para empresas e marcas pessoais. 
Teu estilo mistura storytelling, linguagem acessível e autoridade, com foco nos seguintes blocos: 
🎯 Gancho / 💥 Dor / 🧠 Autoridade / 🧩 Micro-story / 🛒 CTA.

Gere 3 versões diferentes de roteiros para vídeo, com base no seguinte briefing:

Tema: {tema}
Objetivo: {objetivo}
Tom: {tom}
Público-alvo: {publico}
Formato: {formato}
Duração estimada: {tempo}

Cada versão deve ser direta, com frases curtas e impacto emocional. Mantenha a estrutura e destaque os blocos de cada parte com emojis e títulos.
"""

    openai.api_key = openai_api_key
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt_base}],
        temperature=0.9
    )
    return resposta.choices[0].message.content

# Botão para gerar os roteiros
if st.button("🎬 Gerar Roteiros"):
    if openai_api_key and tema and publico:
        with st.spinner("Criando roteiros com VideoCraft..."):
            resultado = gerar_roteiros()
            st.markdown("### 🧠 Roteiros Gerados")
            st.markdown(resultado)
    else:
        st.error("Preencha todos os campos e insira sua OpenAI API Key.")

# Aba: Análise de Conteúdo
elif menu == "📈 Análise de Conteúdo":
    st.header("Análise de Conteúdo Produzido")
    st.write("Cole abaixo um roteiro ou legenda já criada para análise de clareza, persuasão e impacto.")
    conteudo = st.text_area("📝 Cole aqui o texto do conteúdo:")
    if st.button("Analisar conteúdo"):
        st.success("🔧 Em breve: Análise completa com feedback sobre CTA, gancho, storytelling e objetivo.")

# Aba: Ideias de Conteúdo por Segmento
elif menu == "🧠 Ideias de Conteúdo por Segmento":
    st.header("Ideias de Conteúdo por Segmento")
    nicho = st.selectbox("🏷️ Nicho do cliente", ["Barbearia", "Estúdio de tatuagem", "Clínica estética", "Loja de roupas", "Petshop", "Outro"])
    objetivo = st.selectbox("🎯 Objetivo do conteúdo", ["Atrair novos clientes", "Vender mais", "Gerar autoridade", "Engajar"])
    if st.button("Gerar ideias"):
        st.success("🔧 Em breve: Sugestões de roteiros e CTAs personalizados por segmento.")

# Aba: Planejador de Grade de Conteúdo
elif menu == "🗓️ Planejador de Grade de Conteúdo":
    st.header("Planejador de Grade de Conteúdo")
    st.write("Informe os dados abaixo para gerar uma sugestão de grade semanal com temas e formatos ideais.")
    postagens_semana = st.selectbox("📅 Frequência semanal de postagens", ["1", "2", "3", "4", "5+"])
    foco = st.selectbox("🎯 Foco principal", ["Autoridade", "Engajamento", "Conversão", "Relacionamento"])
    nivel_cliente = st.selectbox("🏁 Nível do cliente nas redes", ["Iniciante", "Intermediário", "Avançado"])
    if st.button("Gerar grade"):
        st.success("🔧 Em breve: Grade semanal com ideias e formatos distribuídos.")
