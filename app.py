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
    st.header("Criação de Roteiros com Perguntas Guiadas")
    st.write("Responda às perguntas abaixo para gerar um roteiro com base no estilo VOID.")
    tema = st.text_input("🎯 Qual o tema do vídeo?")
    objetivo = st.selectbox("🎯 Qual o objetivo do vídeo?", ["Gerar autoridade", "Converter em vendas", "Engajamento", "Outro"])
    tom = st.selectbox("🗣️ Qual o tom da comunicação?", ["Inspirador", "Confiante", "Leve", "Direto", "Outro"])
    publico = st.text_input("👥 Quem é o público-alvo?")
    formato = st.selectbox("🎬 Formato do vídeo", ["Reels", "Story", "YouTube Shorts", "Institucional", "Outro"])
    tempo = st.selectbox("⏱️ Duração estimada", ["Até 30s", "1 minuto", "2-3 minutos", "Outro"])
    if st.button("Gerar roteiro"):
        st.success("🔧 Em breve: Roteiro gerado com base nas respostas.")

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
