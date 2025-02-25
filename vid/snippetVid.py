from skimage.filters import gaussian_filter
from moviepy.editor import VideoFileClip, ImageClip

def blur(image):
  """ Returns a blurred (radius=2 pixels) version of the image """
  return gaussian_filter(image.astype(float), sigma=2)

def blurVid():
  clip = VideoFileClip("my_video.mp4")
  clip_blurred = clip.fl_image( blur )
  clip_blurred.write_videofile("blurred_video.mp4")

def avgFrame(finVid="video.mp4"):
    clip = VideoFileClip(finVid)
    fps= 1. # take one frame per second
    nframes = clip.duration*fps # total number of frames used
    total_image = sum(clip.iter_frames(fps, dtype=float, logger='bar'))
    average_image = ImageClip(total_image/ nframes)
    average_image.save_frame("average_test.png")
