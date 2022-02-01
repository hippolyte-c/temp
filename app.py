import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av
import threading


st.set_page_config(page_title="Streamlit WebRTC Demo", page_icon="🤖")

class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.model_lock = threading.Lock()

    def recv(self, frame):
        # img = frame.to_ndarray(format="bgr24")
        img = frame.to_image()

        # return av.VideoFrame.from_ndarray(img, format="bgr24")
        return av.VideoFrame.from_image(img)

ctx = webrtc_streamer(
    key="example",
    video_processor_factory=VideoProcessor,
    media_stream_constraints={
        "video": True,
        "audio": False
    }
)
