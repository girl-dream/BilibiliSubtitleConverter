main.py
- 自动下载对应视频的字幕(需在cookie.json填写cookie)

json2srt.py
- 在目录自动寻找bcc文件转srt

srt2json.py
- 在目录自动寻找srt文件转bcc
> 多行文字无法正常使用

# 关于bcc格式字幕文件

本质是一个json文件

```json
{
    "font_size": 0.4,
    "font_color": "#FFFFFF",
    "background_alpha": 0.5,
    "background_color": "#9C27B0",
    "stroke": "none",
    "body": [
        {
            "from": 0.068,
            "to": 3.081,
            "location": 2,
            "content": "Lonely萝莉萝莉神降临"
        }
    ]
}
```

