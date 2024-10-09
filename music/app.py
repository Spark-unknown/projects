import streamlit as st
import os
import shutil

# Set the upload folder
UPLOAD_FOLDER = 'music'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def main():
    st.title("Music Streaming App")

    # Upload music files
    st.header("Upload Music")
    uploaded_file = st.file_uploader("Choose a music file...", type=["mp3", "wav", "ogg"])

    if uploaded_file is not None:
        # Save the uploaded file to the music folder
        with open(os.path.join(UPLOAD_FOLDER, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("File uploaded successfully!")

    # List all music files in the upload folder
    st.header("Available Music")
    music_files = os.listdir(UPLOAD_FOLDER)

    if music_files:
        for music in music_files:
            if st.button(f"Play {music}"):
                audio_file = os.path.join(UPLOAD_FOLDER, music)
                st.audio(audio_file)
    else:
        st.write("No music files available.")

if __name__ == "__main__":
    main()
