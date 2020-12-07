import os

os.system('ls')
os.system('cd Desktop')
#keep creating the path with these functions to the video file; in my case, the 5 quality outputs were in the Desktops

#using the previous seminar functions for cuting the video and transforming it to the 4 different qualities
#os.system('ffmpeg -ss 00:04:18 -i bbb.mp4 -to 00:00:10 -c copy bbb10sec.mp4')

#os.system('ffmpeg -i bbb10sec.mp4 -filter:v scale=720:-2 -c:a copy bbb10sec720.mp4')
#os.system('ffmpeg -i bbb10sec.mp4 -filter:v scale=480:-2 -c:a copy bbb10sec480.mp4')
#os.system('ffmpeg -i bbb10sec.mp4 -filter:v scale=360:240 -c:a copy bbb10sec360x240.mp4')
#os.system('ffmpeg -i bbb10sec.mp4 -filter:v scale=160:120 -c:a copy bbb10sec160x120.mp4')

#this functions just changes the name of the files
os.rename('bbb10sec1080.mp4', '1080_quality.mp4') #As the file is already 1080, we do not need to create this new file
os.rename('bbb10sec720.mp4', '720_quality.mp4')
os.rename('bbb10sec480.mp4', '480_quality.mp4')
os.rename('bbb10sec360x240.mp4', '360x240_quality.mp4')
os.rename('bbb10sec160x120.mp4', '160x120_quality.mp4')
