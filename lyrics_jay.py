import requests


music_list_url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp"
music_lyrics_url = "https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg"

headers = {
    "Origin": "https://y.qq.com",
    "Referer": "https://y.qq.com/n/yqq/song/",
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/71.0.3578.98 Safari/537.36'
    }

for page_num in range(1, 6):
    music_list_param = {
        "ct": "24",
        "qqmusic_ver": "1298",
        "new_json": "1",
        "remoteplace": "txt.yqq.song",
        "searchid": "70783466275292510",
        "t": "0",
        "aggr": "1",
        "cr": "1",
        "catZhida": "1",
        "lossless": "0",
        "flag_qc": "0",
        "p": str(page_num),
        "n": "10",
        "w": "周杰伦",
        "g_tk": "5381",
        "loginUin": "0",
        "hostUin": "0",
        "format": "json",
        "inCharset": "utf8",
        "outCharset": "utf-8",
        "notice": "0",
        "platform": "yqq.json",
        "needNewCode": "0"
    }

    music_list_res = requests.get(music_list_url, headers=headers, params=music_list_param)
    music_list_json = music_list_res.json()
    music_list = music_list_json["data"]["song"]["list"]
    for music_info in music_list:
        music_lyrics_param = {
            "nobase64": "1",
            "musicid": str(music_info["id"]),
            "-": "jsonp1",
            "g_tk": "5381",
            "loginUin": "0",
            "hostUin": "0",
            "format": "json",
            "inCharset": "utf8",
            "outCharset": "utf-8",
            "notice": "0",
            "platform": "yqq.json",
            "needNewCode": "0"
        }
        # print(music_info["name"] + ":" + str(music_info["id"]))
        music_lyrics_res = requests.get(music_lyrics_url, headers=headers, params=music_lyrics_param)
        music_lyrics_json = music_lyrics_res.json()
        # print("lyric" in music_lyrics_json)
        if "lyric" in music_lyrics_json:
            print(music_lyrics_json["lyric"])
