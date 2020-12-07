from moviepy.editor import VideoFileClip    #imports the necessary library for using the necessary functions
import cv2

clip = VideoFileClip("bbb.mp4") #creates a variable with the bunny video
print("Duration:", clip.duration, "seconds")    #shows the durations in SECONDS (9.57 minuts = 597 seconds)

vcap = cv2.VideoCapture('bbb.mp4')  #saves the video file using cv2 for being able to use cv2 functions

width = vcap.get(cv2.CAP_PROP_FRAME_WIDTH ) #gets the width of the video
height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT )   #gets the height of the video
fps =  vcap.get(cv2.CAP_PROP_FPS)   #gets the fps of the video
print("Width:", width, "Height:", height, "fps:", fps)  #shows the width, height and fps of bbb
