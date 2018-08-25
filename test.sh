ffmpeg -y \
  -i gui.mp3 \
  -itsoffset 0.5 \
  -i 0_3_5.2_5.mp3\
  -itsoffset 1.5 \
  -i 2_3_5.2_5.mp3\
  -filter_complex \
  amix=inputs=3:duration=shortest:dropout_transition=4 \
  -f mp3 \
  -async 1 \
  output.mp4
