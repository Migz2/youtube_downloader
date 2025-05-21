import streamlit as st
import time
from pytube import YouTube
import os

def get_youtube_object():
    url = st.text_input("YT Link")
    if url:
        try:
            yt = YouTube(url)
            # Testa se consegue acessar as informações do vídeo
            yt.check_availability()
            return yt
        except Exception as e:
            st.error(f"Erro ao processar o vídeo: {str(e)}")
            return None
    return None

def download_video(stream):
    if stream:
        try:
            # Cria a pasta 'video' se não existir
            if not os.path.exists('video'):
                os.makedirs('video')
            
            # Faz o download
            file_path = stream.download(output_path='video')
            return True, file_path
        except Exception as e:
            st.error(f"Erro ao baixar o vídeo: {str(e)}")
            return False, None
    return False, None

def main():
    st.title("Youtube Downloader")
    
    # Mostrar GIF inicial
    gifs_path = os.path.join("src")
    gif_name = "yt.gif"
    gif_full_path = os.path.join(gifs_path, gif_name)
    if os.path.exists(gif_full_path):
        st.image(gif_full_path, use_container_width=True)
    
    # Obter objeto YouTube
    yt = get_youtube_object()
    
    if yt:
        try:
            # Mostrar informações do vídeo
            st.write(f"Título: {yt.title}")
            st.write(f"Duração: {yt.length} segundos")
            
            if st.button("Download"):
                # Mostrar GIF de download
                gif_name2 = "dl.gif"
                gif_full_path = os.path.join(gifs_path, gif_name2)
                if os.path.exists(gif_full_path):
                    st.image(gif_full_path, use_container_width=True)
                
                # Obter stream e fazer download
                stream = yt.streams.get_highest_resolution()
                success, file_path = download_video(stream)
                
                if success:
                    st.success(f"Download completo! Arquivo salvo em: {file_path}")
        except Exception as e:
            st.error(f"Erro ao processar o vídeo: {str(e)}")

if __name__ == "__main__":
    main()