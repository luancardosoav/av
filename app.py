import streamlit as st
import openai
import tempfile

st.set_page_config(page_title="VOID Assistant", layout="wide")
st.title("🎬 VOID Assistant – Ferramenta Interna")

# Menu lateral
menu = st.sidebar.radio("Escolha uma funcionalidade:", [
    "🧾 Orçamentos",
    "📘 Playbook",
    "📋 Roteiros",
    "📈 Análise de Conteúdo",
    "🧠 Ideias de Conteúdo por Segmento",
    "🗓️ Planejador de Grade de Conteúdo",
    "🎧 Transcreve AI"
])

# OpenAI API key
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Orçamentos
if menu == "🧾 Orçamentos":
    st.header("Gerador de Orçamentos Automáticos")
    st.write("Cole abaixo o texto ou transcrição do áudio enviado pelo cliente.")
    client_input = st.text_area("📥 Texto enviado pelo cliente:")
    tipo_servico = st.text_input("📦 Tipo de serviço")
    prazo = st.text_input("⏳ Prazo desejado")
    nivel = st.selectbox("💰 Nível de produção", ["Básico", "Intermediário", "Premium"])
    if st.button("Gerar orçamento"):
        st.success("🔧 Em breve: Geração automática via GPT com base nos orçamentos armazenados.")

# Playbook
elif menu == "📘 Playbook":
    st.header("Respostas para Dúvidas e Objeções")
    question_input = st.text_area("💬 Dúvida ou objeção do cliente:")
    categoria = st.selectbox("📂 Categoria da objeção", ["Preço", "Prazo", "Resultado", "Entrega", "Outro"])
    tom_resposta = st.selectbox("🗣️ Tom da resposta", ["Confiante", "Empático", "Objetivo", "Informativo"])
    if st.button("Gerar resposta"):
        st.success("🔧 Em breve: Resposta baseada no playbook personalizado.")

# Roteiros
elif menu == "📋 Roteiros":
    st.header("📋 Roteirista Inteligente VOID")
    st.write("Responda às perguntas abaixo para gerar 3 versões diferentes de um roteiro.")

    tema = st.text_input("🎯 Qual o tema do vídeo?")
    objetivo = st.selectbox("🎯 Qual o objetivo do vídeo?", ["Gerar autoridade", "Converter em vendas", "Engajamento", "Outro"])
    tom = st.selectbox("🗣️ Qual o tom da comunicação?", ["Inspirador", "Confiante", "Leve", "Direto", "Outro"])
    publico = st.text_input("👥 Quem é o público-alvo?")
    formato = st.selectbox("🎬 Formato do vídeo", ["Reels", "Story", "YouTube Shorts", "Institucional", "Outro"])
    tempo = st.selectbox("⏱️ Duração estimada", ["Até 30s", "1 minuto", "2-3 minutos", "Outro"])

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

    if st.button("🎬 Gerar Roteiros"):
        if openai_api_key and tema and publico:
            with st.spinner("Criando roteiros com VideoCraft..."):
                resultado = gerar_roteiros()
                st.markdown("### 🧠 Roteiros Gerados")
                st.markdown(resultado)
        else:
            st.error("Preencha todos os campos e insira sua OpenAI API Key.")

# Análise de Conteúdo
elif menu == "📈 Análise de Conteúdo":
    st.header("Análise de Conteúdo Produzido")
    conteudo = st.text_area("📝 Cole aqui o texto do conteúdo:")
    if st.button("Analisar conteúdo"):
        st.success("🔧 Em breve: Análise completa com feedback sobre CTA, gancho, storytelling e objetivo.")

# Ideias por Segmento
elif menu == "🧠 Ideias de Conteúdo por Segmento":
    st.header("Ideias de Conteúdo por Segmento")
    nicho = st.selectbox("🏷️ Nicho do cliente", ["Barbearia", "Estúdio de tatuagem", "Clínica estética", "Loja de roupas", "Petshop", "Outro"])
    objetivo = st.selectbox("🎯 Objetivo do conteúdo", ["Atrair novos clientes", "Vender mais", "Gerar autoridade", "Engajar"])
    if st.button("Gerar ideias"):
        st.success("🔧 Em breve: Sugestões de roteiros e CTAs personalizados por segmento.")

# Grade de Conteúdo
elif menu == "🗓️ Planejador de Grade de Conteúdo":
    st.header("Planejador de Grade de Conteúdo")
    postagens_semana = st.selectbox("📅 Frequência semanal de postagens", ["1", "2", "3", "4", "5+"])
    foco = st.selectbox("🎯 Foco principal", ["Autoridade", "Engajamento", "Conversão", "Relacionamento"])
    nivel_cliente = st.selectbox("🏁 Nível do cliente nas redes", ["Iniciante", "Intermediário", "Avançado"])
    if st.button("Gerar grade"):
        st.success("🔧 Em breve: Grade semanal com ideias e formatos distribuídos.")

# Transcreve AI
elif menu == "🎧 Transcreve AI":
    st.header("🎧 Transcreve AI – Transcrição de Áudio e Vídeo")
    st.write("Envie um arquivo de áudio/vídeo ou cole um link para gerar a transcrição automática.")

    arquivo = st.file_uploader("📤 Envie um arquivo de áudio ou vídeo (.mp3, .mp4, .wav, .m4a)", type=["mp3", "mp4", "wav", "m4a"])
    link = st.text_input("🔗 Ou cole o link direto do arquivo (em breve YouTube)")

    if st.button("🎙️ Transcrever"):
        if openai_api_key:
            if arquivo:
                with st.spinner("Transcrevendo o arquivo..."):
                    try:
                        with tempfile.NamedTemporaryFile(delete=False) as temp:
                            temp.write(arquivo.read())
                            temp_path = temp.name
                        audio_file = open(temp_path, "rb")
                        transcript = openai.Audio.transcribe("whisper-1", audio_file)
                        st.subheader("📝 Transcrição:")
                        st.write(transcript["text"])
                    except Exception as e:
                        st.error(f"Erro ao transcrever: {e}")
            elif link:
                st.warning("⚠️ Transcrição por link ainda não está disponível nesta versão. Envie um arquivo por enquanto.")
            else:
                st.warning("⚠️ Por favor, envie um arquivo ou insira um link.")
        else:
            st.error("🔐 API Key da OpenAI não fornecida.")
