import os
import ffmpeg

files = os.listdir('.')

for i in range(len(files)):
  nameOfFile, fileExtension = os.path.splitext(files[i])
  if fileExtension == '.dsf':
    (
      ffmpeg
      .input(nameOfFile + fileExtension)
      .output(nameOfFile + '.flac')
      .run()
    )
    # os.system("ffmpeg.exe -i" + " " + nameOfFile + fileExtension + " " + nameOfFile + '.flac')
