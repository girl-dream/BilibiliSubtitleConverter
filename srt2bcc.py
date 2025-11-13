# srt to Bilibili Closed Caption

# coding=utf-8
import os, glob


def srt_timestamp_to_seconds(timestamp):
    """将SRT时间戳转换为秒数"""
    hours, minutes, seconds_ms = timestamp.split(':')
    seconds, milliseconds = seconds_ms.split(',')

    total_seconds = (int(hours) * 3600 +
                     int(minutes) * 60 +
                     int(seconds) +
                     int(milliseconds) / 1000)
    return total_seconds


def str_to_bcc(i,file_name):
    with open(i, 'r', encoding='utf-8') as srt:
        with open(os.path.join('.', file_name), 'w', encoding='utf-8') as bcc:
            bcc.write(
                '{"font_size":0.4,"font_color":"#FFFFFF","background_alpha":0.5,"background_color":"#9C27B0","Stroke":"none","body":[')
            for index, value in enumerate(srt.readlines()):
                index = index % 4
                value = value.strip('\n')
                if index == 1:
                    start_time, end_time = value.split(' --> ')
                    start_time = srt_timestamp_to_seconds(start_time)
                    end_time = srt_timestamp_to_seconds(end_time)
                    bcc.write(f'\n{{"from":{start_time},\n"to":{end_time},\n"location": 2,\n')
                elif index == 2:
                    pass
                    bcc.write(f'"content": "{value}"}},')
            bcc.close()
        srt.close()

    with open(os.path.join('.', file_name), 'a', encoding='utf-8') as bcc:
        bcc.seek(0, 2)
        size = bcc.tell()
        bcc.truncate(size - 1)
        bcc.write(']}')
        bcc.close()
        print(f"BCC 文件 {file_name} 已生成")

if __name__ == '__main__':
    for i in glob.glob(os.path.join('.', '*.srt')):
        file_name = f'{os.path.basename(i).split('.')[0]}.bcc'
        str_to_bcc(i,file_name)
