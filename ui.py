import streamlit as st
from Youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="Youtube video Analyzer",
    layout="centered"
)
st.title("🎥AI Youtube Video Analyzer")



@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent=get_agent()

# input box
video_url=st.text_input("Enter Youtube Video Link") # link pase as sting
button=st.button("Analyze Video") # True/false

if video_url and button:
    with st.spinner("Analyzing video....."):
        response = agent.run(
            f"Analyze the video: {video_url}"
        )
    st.markdown("Analysis Report of video")
    st.markdown(response.content) # it wark for (text+markdown)