import streamlit as st
import unicodedata
import re

st.set_page_config(page_title="Padronizador ISO 9001", page_icon="🗂️")

st.title("🗂️ Padronizador de Nomes de Arquivos - Padrão ISO 9001")
st.subheader("Remoção de acentos, espaços, caracteres especiais e conversão para MAIÚSCULO")

st.markdown("Digite ou cole abaixo os nomes das pastas/arquivos, um por linha, e clique em **Padronizar**.")

entrada = st.text_area("Nomes originais (um por linha)", height=300)

def padronizar_nome(texto):
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    texto = texto.replace(' ', '-')
    texto = re.sub(r'[^A-Za-z0-9_-]', '', texto)
    texto = texto.upper()
    return texto

if st.button("🚀 Padronizar"):
    linhas = entrada.splitlines()
    linhas_padronizadas = [padronizar_nome(linha) for linha in linhas if linha.strip() != '']
    
    st.subheader("✅ Resultado Padronizado:")
    resultado = "\n".join(linhas_padronizadas)
    st.code(resultado)
    
    st.download_button(
        label="📥 Baixar como .txt",
        data=resultado,
        file_name="nomes_padronizados.txt",
        mime="text/plain"
    )
