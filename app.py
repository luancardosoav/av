import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="VOID Assistant – VideoCraft", layout="centered")
st.title("VOID Assistant – Roteirista Profissional")

st.markdown("Crie roteiros específicos, humanos e com impacto real. Preencha o briefing abaixo:")

# API Key segura
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Função auxiliar para lidar com "Outro"
def handle_outro(opcao, label):
    if opcao == "Outro":
        return st.text_input(f"✍️ Especifique o {label.lower()}")
    return opcao

# Formulário de briefing
with st.form("briefing_form"):
    tema = st.text_input("Tema central do vídeo")

    objetivo_raw = st.selectbox("Objetivo principal do vídeo", [
        "Gerar autoridade", "Atrair novos clientes", "Educar o público",
        "Engajar seguidores", "Posicionar a marca", "Converter leads em clientes", "Outro"
    ])
    objetivo = handle_outro(objetivo_raw, "objetivo")

    tom_raw = st.selectbox("Tom da comunicação", [
        "Confiante", "Inspirador", "Educativo", "Direto", "Provocador", "Divertido", "Emocional", "Outro"
    ])
    tom = handle_outro(tom_raw, "tom")

    publico = st.text_input("Descreva brevemente o público-alvo")

    formato_raw = st.selectbox("Formato do vídeo", [
        "Reels (Instagram)", "Shorts (YouTube)", "Stories", "Vídeo institucional", "Anúncio (ads)", "VSL (vídeo de vendas)", "Outro"
    ])
    formato = handle_outro(formato_raw, "formato")

    duracao_raw = st.selectbox("Duração estimada", [
        "Até 15 segundos", "Até 30 segundos", "1 minuto", "2-3 minutos", "Outro"
    ])
    duracao = handle_outro(duracao_raw, "duração")

    submit = st.form_submit_button("Gerar Roteiros")

# Geração de roteiros (sem emojis, mais específicos)
def gerar_roteiros(tema, objetivo, tom, publico, formato, duracao):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openai_api_key
    )

    prompt = f"""
Você é um roteirista profissional chamado VideoCraft, especializado em criação de roteiros curtos e específicos que conectam com o público certo.

Crie 3 versões diferentes de um roteiro para vídeo com base no briefing abaixo. Cada roteiro deve ser direto, parecer escrito por um humano com experiência real na área e conter:
- Um gancho claro logo de início
- Uma dor ou desafio real enfrentado por quem está assistindo
- Uma solução que gere autoridade e passe confiança
- Um exemplo ou situação real que represente o cenário
- Uma chamada para ação convincente e natural

Importante:
- Escreva os roteiros inteiramente em português do Brasil
- Não utilize emojis
- Não utilize marcadores ou divisões visuais artificiais
- A linguagem deve ser estratégica, fluida e natural, como se fosse falada no vídeo
- Adapte a abordagem de cada versão ao tom e público informados

Briefing:
Tema: {tema}
Objetivo do vídeo: {objetivo}
Tom desejado: {tom}
Público-alvo: {publico}
Formato: {formato}
Duração estimada: {duracao}
"""

    resposta = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )

    return resposta.choices[0].message.content

# Caixa de feedback para alterações
def refinar_roteiro(texto_original, instrucoes):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openai_api_key
    )

    prompt_refinamento = f"""
Você acabou de gerar os seguintes roteiros:

{texto_original}

Agora, com base nas instruções do usuário abaixo, reescreva os roteiros de forma aprimorada, mantendo a estrutura e a naturalidade, mas aplicando os ajustes solicitados.

Instruções do usuário:
{instrucoes}

Importante:
- Continue escrevendo em português do Brasil
- Não use emojis
- Mantenha a linguagem natural e realista
"""

    resposta = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt_refinamento}],
        temperature=0.9
    )

    return resposta.choices[0].message.content

# Execução
if submit:
    if all([tema, objetivo, tom, publico, formato, duracao]):
        with st.spinner("Gerando roteiros com mais impacto..."):
            try:
                resultado_inicial = gerar_roteiros(tema, objetivo, tom, publico, formato, duracao)
                st.markdown("### Roteiros Gerados")
                st.markdown(resultado_inicial)

                st.markdown("---")
                st.subheader("Quer pedir ajustes?")
                feedback = st.text_area("Descreva aqui o que gostaria de mudar, melhorar ou refinar nos roteiros:")
                if st.button("Aplicar alterações"):
                    with st.spinner("Refinando com base no teu feedback..."):
                        refinado = refinar_roteiro(resultado_inicial, feedback)
                        st.markdown("### Roteiros Ajustados")
                        st.markdown(refinado)
            except Exception as e:
                st.error(f"Erro ao gerar os roteiros: {e}")
    else:
        st.warning("Preencha todos os campos para gerar os roteiros.")
