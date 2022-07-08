from moviepy.editor import *
import random

a = 'jupyter keyshorts'
num = random.randint(1,1000)

mp4 = 'DJ Snake feat Lil Jon Turn Down For What With Lyrics(360p).mp4'
mp3 = f"{a}{num}.mp3"

video_clip = VideoFileClip(mp4)

audio = video_clip.audio
audio.write_audiofile(mp3)

audio.close()
video_clip.close()
