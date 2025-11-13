# coding=utf-8
import json, gzip, re
from urllib.request import urlopen, Request

headers = json.load(open('cookie.json'))

def net_get(url):
    req = Request(url, headers=headers, method='GET')

    response = urlopen(req)
    res_data = response.read()

    if response.getheader('Content-Encoding') == 'gzip':
        res_data = gzip.decompress(res_data)

    response.close()
    return res_data.decode('utf-8')


def get_url_bilibili(text):
    if re.match(r'^(?:(http|https)://)?((?:[\w-]+\.)+[a-z0-9]+)((?:/[^?#]*)+)?(\?[^#]+)?(#.+)?$', text):
        match = re.search(r"(BV.*?).{10}", text)
        if match:
            return match.group(0)
        match = re.search(r"av(\d+)", text)
        if match:
            return match.group(0)
    elif re.match(r'^BV[1-9A-HJ-NP-Za-km-z]{10}$', text):
        return f'https://api.bilibili.com/x/web-interface/view?bvid={text}'
    elif re.match(r'^[1-9]\d{5,}$', text):
        return f'https://api.bilibili.com/x/web-interface/view?aid={text}'

if __name__ == '__main__':
    text = input('请输入url/bv/av(只支持普通视频)')

    url = get_url_bilibili(text)

    res = json.loads((net_get(url)))

    if res['code'] == 62012:
        print('仅UP主自己可见')
        exit()
    elif res['code'] != 0:
        print('获取视频信息失败\n'+res['message'])
        exit()

    bvid = res['data']['bvid']
    cid = res['data']['cid']
    title = res['data']['title']

    data = json.loads(net_get(f'https://api.bilibili.com/x/player/v2?cid={cid}&bvid={bvid}'))['data']
    l = data['subtitle']['subtitles']

    for i in l:
        if len(i['subtitle_url']) > 0:
            data = net_get('https:'+i['subtitle_url'])
            with open(f'{title}.bcc', 'w', encoding='utf-8') as f:
                f.write(data)
                f.close()
        else:
            print('未找到字幕文件')
