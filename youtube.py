import streamlit as st
from pytube import YouTube
import os

st.set_page_config(page_title="TubeGrab", page_icon="📺", layout="wide")

st.title("TubeGrab 📺")

# create a text input box for the user to paste the YouTube video link
# display the download count to the user
with open('download_count.txt', 'r') as f:
    count = int(f.read() or 0)
    st.write(f"{count} videos downloaded")
counter = 0
video_link = st.text_input("Enter the YouTube video link")

# if the user has entered a link, extract the video details
if video_link:
    try:
        yt = YouTube(video_link)
        thumbnail = yt.thumbnail_url
        title = yt.title
        streams = yt.streams.filter(progressive=True)
        st.image(thumbnail, width=600)
        # adjust image to fit container
        st.markdown("<style>img{max-width: 100%;}</style>", unsafe_allow_html=True)
        st.write(f"<p style='font-size:20px'>{title}</p>", unsafe_allow_html=True)

        # display the available resolutions and buttons to download
        for stream in streams:
            with st.container():
                # create a row layout for each resolution and download button
                res_col, button_col = st.columns([1, 2])
                with res_col:
                    st.write(f"{title} | {stream.resolution} - {stream.mime_type}")

                with button_col:
                    file_extension = stream.mime_type.split("/")[-1]
                    video_bytes = stream.stream_to_buffer()
                    st.success(f"{stream.resolution} download ready!")
                    if st.button(f"Download {stream.resolution}"):
                        st.download_button(data=video_bytes, mime=video/f"{file_extension}", label =f"Click here to download {title}.{file_extension}", key=counter)
                        counter += 1
                        file_size = len(video_bytes)
                        st.write(f"Downloaded file: [{title}.{file_extension}]({title}.{file_extension}) ({round(file_size/1024/1024, 2)} MB)")
                        with open('download_count.txt', 'a+') as f:
                            f.seek(0)
                            count = int(f.read() or 0)
                            f.seek(0)
                            f.truncate()
                            f.write(str(count+1))

    except:
        st.error("Invalid YouTube video link!")
