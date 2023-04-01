import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

videos = os.listdir("./assets")
videos = [VideoFileClip(f"./assets/{video}") for video in videos if video.endswith(".mp4")]
final_clip = concatenate_videoclips(videos)
final_audio = AudioFileClip("./assets/voice_c53d9ca2-352b-44c2-860c-92a1c3a16690.mp3")
final_clip = final_clip.set_audio(final_audio)

# clip the video to audio length
final_clip = final_clip.subclip(0, final_audio.duration)



final_clip.write_videofile("./output/final.mp4")