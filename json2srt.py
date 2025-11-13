# bilibili subtitle json to srt

# coding=utf-8
import json, os, datetime, glob


def seconds_to_hms(seconds):
    """将秒数转换为 hour:minute:second.millisecond 格式"""
    td = datetime.timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    milliseconds = int(td.microseconds / 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"


def json_to_bcc(data, file_name, code='utf-8'):
    num = 1

    with open(os.path.join('.', f'{file_name}.srt'), 'w', encoding=code) as srt:
        for i in data:
            srt.write(f'{num}\n{seconds_to_hms(i['from'])} --> {seconds_to_hms(i['to'])}\n{(i["content"])}\n\n')
            num += 1
        print(f"SRT 文件 {file_name}.srt 已生成")
        srt.close()


if __name__ == '__main__':
    for i in glob.glob('*.bcc') + glob.glob('*.json'):
        if i == 'cookie.json':
            continue
        file_name = i.split('.')[0]
        with open(i, 'r', encoding='utf-8') as f:
            temp = json.load(f)['body']
            json_to_bcc(temp, file_name)
