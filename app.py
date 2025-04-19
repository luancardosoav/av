import streamlit as st
from openai import OpenAI
import tempfile

st.set_page_config(page_title="VOID Assistant", layout="wide")
st.title("🎬 VOID Assistant – Ferramenta Interna")

menu = st.sidebar.radio("Escolha uma funcionalidade:", [
    "🧾 Orçamentos",
    "📘 Playbook",
    "📋 Roteiros",
    "📈 Análise de Conteúdo",
    "🧠 Ideias de Conteúdo por Segmento",
    "🗓️ Planejador de Grade de Conteúdo",
    "🎧 Transcreve AI"
])

# OpenAI Key
openai_api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else st.text_input("🔑 Cole sua OpenAI API Key", type="password")

# Utilitário para "Outro"
def handle_outro(selecao, label):
    if selecao == "Outro":
        return st.text_input(f"✍️ Especifica o {label.lower()}")
    return selecao

# ORÇAMENTOS
if menu == "🧾 Orçamentos":
    st.header("Gerador de Orçamentos Automáticos")
    client_input = st.text_area("📥 Texto enviado pelo cliente:")
    tipo_servico = st.text_input("📦 Tipo de serviço")
    prazo = st.text_input("⏳ Prazo desejado")
    nivel_raw = st.selectbox("💰 Nível de produção", ["Básico", "Intermediário", "Premium", "Outro"])
    nivel = handle_outro(nivel_raw, "nível de produção")
    if st.button("Gerar orçamento"):
        st.success("🔧 Em breve: Geração automática via GPT com base nos orçamentos armazenados.")

# PLAYBOOK
elif menu == "📘 Playbook":
    st.header("Respostas para Dúvidas e Objeções")
    question_input = st.text_area("💬 Dúvida ou objeção do cliente:")
    categoria_raw = st.selectbox("📂 Categoria da objeção", ["Preço", "Prazo", "Resultado", "Entrega", "Outro"])
    categoria = handle_outro(categoria_raw, "categoria da objeção")
    tom_raw = st.selectbox("🗣️ Tom da resposta", ["Confiante", "Empático", "Objetivo", "Informativo", "Outro"])
    tom = handle_outro(tom_raw, "tom da resposta")
    if st.button("Gerar resposta"):
        st.success("🔧 Em breve: Resposta baseada no playbook personalizado.")

# ROTEIROS
elif menu == "📋 Roteiros":
    st.header("📋 Roteirista Inteligente VOID")

    tema = st.text_input("🎯 Qual o tema do vídeo?")
    objetivo_raw = st.selectbox("🎯 Qual o objetivo do vídeo?", ["Gerar autoridade", "Converter em vendas", "Engajamento", "Outro"])
    objetivo = handle_outro(objetivo_raw, "objetivo")

    tom_raw = st.selectbox("🗣️ Qual o tom da comunicação?", ["Inspirador", "Confiante", "Leve", "Direto", "Outro"])
    tom = handle_outro(tom_raw, "tom")

    publico = st.text_input("👥 Quem é o público-alvo?")

    formato_raw = st.selectbox("🎬 Formato do vídeo", ["Reels", "Story", "YouTube Shorts", "Institucional", "Outro"])
    formato = handle_outro(formato_raw, "formato do vídeo")

    tempo_raw = st.selectbox("⏱️ Duração estimada", ["Até 30s", "1 minuto", "2-3 minutos", "Outro"])
    tempo = handle_outro(tempo_raw, "duração")

    def gerar_roteiros():
        client = OpenAI(api_key=openai_api_key)
        prompt_base = f"""
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

# ANÁLISE
elif menu == "📈 Análise de Conteúdo":
    st.header("Análise de Conteúdo Produzido")
    conteudo = st.text_area("📝 Cole aqui o texto do conteúdo:")
    if st.button("Analisar conteúdo"):
        st.success("🔧 Em breve: Análise completa com feedback sobre CTA, gancho, storytelling e objetivo.")

# IDEIAS POR SEGMENTO
elif menu == "🧠 Ideias de Conteúdo por Segmento":
    st.header("Ideias de Conteúdo por Segmento")
    nicho_raw = st.selectbox("🏷️ Nicho do cliente", ["Barbearia", "Estúdio de tatuagem", "Clínica estética", "Loja de roupas", "Petshop", "Outro"])
    nicho = handle_outro(nicho_raw, "nicho")

    objetivo_raw = st.selectbox("🎯 Objetivo do conteúdo", ["Atrair novos clientes", "Vender mais", "Gerar autoridade", "Engajar", "Outro"])
    objetivo = handle_outro(objetivo_raw, "objetivo do conteúdo")

    if st.button("Gerar ideias"):
        st.success("🔧 Em breve: Sugestões de roteiros e CTAs personalizados por segmento.")

# GRADE
elif menu == "🗓️ Planejador de Grade de Conteúdo":
    st.header("Planejador de Grade de Conteúdo")
    postagens = st.selectbox("📅 Frequência semanal de postagens", ["1", "2", "3", "4", "5+"])
    foco_raw = st.selectbox("🎯 Foco principal", ["Autoridade", "Engajamento", "Conversão", "Relacionamento", "Outro"])
    foco = handle_outro(foco_raw, "foco")
    nivel_raw = st.selectbox("🏁 Nível do cliente nas redes", ["Iniciante", "Intermediário", "Avançado", "Outro"])
    nivel = handle_outro(nivel_raw, "nível do cliente")
    if st.button("Gerar grade"):
        st.success("🔧 Em breve: Grade semanal com ideias e formatos distribuídos.")

# TRANSCRIÇÃO
elif menu == "🎧 Transcreve AI":
    st.header("🎧 Transcreve AI – Transcrição de Áudio e Vídeo")
    arquivo = st.file_uploader("📤 Envie um arquivo (.mp3, .mp4, .wav, .m4a)", type=["mp3", "mp4", "wav", "m4a"])
    link = st.text_input("🔗 Ou cole o link (YouTube em breve)")

    if st.button("🎙️ Transcrever"):
        if openai_api_key:
            if arquivo:
                with st.spinner("Transcrevendo..."):
                    try:
                        client = OpenAI(api_key=openai_api_key)
                        with tempfile.NamedTemporaryFile(delete=False) as temp:
                            temp.write(arquivo.read())
                            temp_path = temp.name
                        with open(temp_path, "rb") as audio_file:
                            transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
                        st.subheader("📝 Transcrição:")
                        st.write(transcript.text)
                    except Exception as e:
                        st.error(f"Erro ao transcrever: {e}")
            elif link:
                st.warning("⚠️ Transcrição por link ainda não disponível. Use upload de arquivo por enquanto.")
            else:
                st.warning("⚠️ Envie um arquivo ou insira um link.")
        else:
            st.error("🔐 API Key da OpenAI não fornecida.")
