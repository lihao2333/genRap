## 一个语音合成脚本
基于百度开放的语音合成平台, 通过这个脚本, 你可以很方便的将句子按照任意时间格式插入到一个音乐之中.   
你可以用来合成绕口令, 或者rap等等.  
## 安装环境
linux下只需要ffmpeg, 一般是默认安装的.  
windows下要下载一个ffmpeg
## 使用方法
#### 准备歌词
在`lyric/lylric.py`中编辑你的歌词, 格式为
```
{
    "lyricId":"lyric"
}
```
####  准备乐谱
在`musicbook/musicbook.txt`中编辑你的乐谱, 格式为
```
[time] lyricId_speaker_speed_pitch
```
* time如果为`1`, 则意味着插入到第`1`个4个八拍结束处
* lyricId 和 歌词中的匹配既可
* speaker 有`1`:机器男生, `2`:机器女生,`3`:感情男生,`4`:感情女生 四个选项
* speed 为0~15的小数
* pitch 为0~9的整数, 数字越大, 音调越高

#### 配置文件
在`generate_song.py`文件中按照注释修改最上面几行的配置文件

#### 开始生成
执行`python3 generate_song.py`既可. 输出的音乐在`output文件夹里`



