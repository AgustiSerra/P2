from videoprops import get_video_properties #imports the necessary library for using the necessary functions

props = get_video_properties('bbb.mp4') #saves the video file using get_video_properties for being able to use its functions

#printing the codec of audio of the video, its resolution, its aspect ratio and  its frame rate
print(f'''
Codec: {props['codec_name']}
Resolution: {props['width']}×{props['height']}
Aspect ratio: {props['display_aspect_ratio']}
Frame rate: {props['avg_frame_rate']}
''')
