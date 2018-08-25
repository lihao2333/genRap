#!/bin/python3
## 配置
PERIOD = 11.9   #伴奏4个8拍的时间
DELAY=5     #添加延时,有的音乐最前面有不规则长度的音乐片段
MUSICBOOK_PATH="./musicbook/musicbook.txt"  #选择音乐脚本
ACCOMPANY_PATH="./accompany/v3.2.mp3"   #选择伴奏
OUTPUT_SONG_NAME="./output/output.mp3"   #输出音乐文件名
OUTPUT_LYRIC_NAME="./output/output_musicbook.txt"   #输出歌词文件名

import re,os

## 开始体
### 歌词
from lyric.lyrics import lyrics as lyrics
### 解析乐谱
partten = "^\[(.*)\]\s+(.*?)_(\d+)_(\d+.\d+)_(\d+)$"
compile_rule = re.compile(partten,re.M)
musicbook = re.findall(compile_rule, open(MUSICBOOK_PATH).read())
### 准备合成音乐的命令
cmd_0 = "ffmpeg -y -i %s "%(ACCOMPANY_PATH)
cmd_1 = ""
cmd_2 = "-filter_complex \
    amix=inputs={cnt}:duration=first:dropout_transition=4\
    -f mp3 \
    -async 1 \
    {output} \
    ".format(cnt=len(musicbook)+1, output=OUTPUT_SONG_NAME)
### 最终输出歌词文件的路径
outputLyricFile = open(OUTPUT_LYRIC_NAME,"w")

### 循环体
def generateVoice(lyricId, speaker, speed, pitch): 
    voice_output_path = "voice/{}_{}_{}_{}.mp3".format(lyricId, speaker, speed, pitch)
    if os.path.basename(voice_output_path)  in os.listdir('./voice'):
        print(voice_output_path,"exists")
    else:
        print(voice_output_path,"no exists generating")
        cmd = "./generate.sh {} {} {} {} {}  ".format(lyrics[lyricId], speaker, speed, pitch, voice_output_path)
        os.system(cmd)
def appendCMD(time, lyricId, speaker, speed, pitch):
    global cmd_1
    cmd_1 +=  "-itsoffset {0} ".format(float(time)*PERIOD + DELAY)
    cmd_1 +=  "-i voice/{}_{}_{}_{}.mp3 ".format(lyricId, speaker, speed, pitch)
def writeLyric(time, lyricId):
    global outputLyricFile
    outputLyricFile.write("[%02d:%02.2f] %s\n"%((float(time)*PERIOD+DELAY)/60,(float(time)*PERIOD+DELAY)%60, lyrics[lyricId]))

for _musicbook in musicbook: #time, lyricId, speaker, speed, pitch
    generateVoice(*_musicbook[1:])
    appendCMD(*_musicbook[0:])
    writeLyric(*_musicbook[0:2])

### 结束体
cmd_end = cmd_0 + cmd_1 + cmd_2
print(cmd_end)
os.system(cmd_end)
