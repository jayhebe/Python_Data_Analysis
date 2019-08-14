import sys
import json

sys.path.append(r"C:\Study\Programming\Python\Python_Data_Analysis")

from d10.mymodule.stats_word import stats_text


with open("tang300.json", encoding="utf-8") as f_poems:
    poems_json = json.load(f_poems)

all_poems = ""
for poems_info in poems_json:
    all_poems += poems_info["contents"]

try:
    en_result, cn_result = stats_text("", all_poems)
    print("EN words result: ", en_result)
    print("CN words result: ", [(word, count) for word, count in cn_result if len(word) >= 2][:20])
except ValueError as e:
    print("Exception catched.")
    print(e)
