from pymediainfo import MediaInfo
import os
import shutil

path_AVC = 'C:\\Users\\carol\\Videos\\VIDEOS_AVC'
path_MPEG_4 = 'C:\\Users\\carol\\Videos\\VIDEOS_MPEG-4'
path_digital = 'C:\\Users\\carol\\Videos\\digital'

files = [f for f in os.listdir(path_digital) if f.endswith('.MXF') or f.endswith('.mxf')]
for f in files:
    file_path = path_digital + '\\' + f
    media_info = MediaInfo.parse(file_path)

    for track in media_info.tracks:
        if track.track_type == 'Video':
            miliseconds = (track.to_data()["duration"]) # ms
            print(miliseconds)
            
           if track.format == 'AVC':
               shutil.move(file_path, path_AVC)
           if track.format == 'MPEG-4 Visual':
               shutil.move(file_path, path_MPEG_4)
