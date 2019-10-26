import requests
import json


def get_test_scope():
    print("""
0. GMAT     5. 英专
1. 考研     6. 托福
2. 高考     7. GRE
3. 四级     8. 雅思
4. 六级     9. 任意
    """)
    choice = int(input("请选择出题范围："))

    test_scope = ""
    if choice == 0:
        test_scope = "GMAT"
    elif choice == 1:
        test_scope = "NGEE"
    elif choice == 2:
        test_scope = "NCEE"
    elif choice == 3:
        test_scope = "CET4"
    elif choice == 4:
        test_scope = "CET6"
    elif choice == 5:
        test_scope = "TEM"
    elif choice == 6:
        test_scope = "TOEFL"
    elif choice == 7:
        test_scope = "GRE"
    elif choice == 8:
        test_scope = "IELTS"
    elif choice == 9:
        test_scope = "NONE"

    return test_scope


shanbay_url = "https://www.shanbay.com/api/v1/vocabtest/vocabularies"
shanbay_headers = {
    "referer": "https://www.shanbay.com/vocabtest/",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/77.0.3865.120 Safari/537.36',
    "x-requested-with": "XMLHttpRequest"
}

shanbay_test_scope = get_test_scope()
if len(shanbay_test_scope) != 0:
    shanbay_data = {
        "category": shanbay_test_scope
    }
    shanbay_res = requests.get(shanbay_url, headers=shanbay_headers, params=shanbay_data)
    all_words = [word_info for word_info in shanbay_res.json()["data"]]

    known_words = []
    for num, word in enumerate(all_words):
        answer = input("{}. 请问 {} 这个单词你认识吗？（Y/N）".format(num + 1, word["content"]))
        if answer.lower() == "y":
            known_words.append(word)

    correct_words = []
    for known_word in known_words:
        correct_answer = known_word["pk"]
        print("请问 {} 单词的意思是？".format(known_word["content"]))
        for index, definition_choice in enumerate(known_word["definition_choices"]):
            print("{}. {}".format(index, definition_choice["definition"]))
        print("{}. {}".format(len(definition_choice) + 1, " 不认识"))
        user_answer_index = int(input("请选择正确答案："))
        user_answer = known_word["definition_choices"][user_answer_index]["pk"]

        if user_answer == correct_answer:
            correct_words.append(str(known_word["content"]))

    print("所有测试的单词为：{}".format([word["content"] for word in all_words]))
    print("你答对的单词为：{}".format(correct_words))
    print("正确率为 {:.2f}%".format(len(correct_words) / len(all_words) * 100))
    # print(all_ranks)
    # rank_headers = {
    #     "origin": "https://www.shanbay.com",
    #     "referer": "https://www.shanbay.com/vocabtest/",
    #     "sec-fetch-mode": "cors",
    #     "sec-fetch-site": "same-origin",
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    #     Chrome/77.0.3865.120 Safari/537.36',
    #     "x-requested-with": "XMLHttpRequest"
    # }
    #
    # rank_data = {
    #     "category": shanbay_test_scope,
    #     "phase": "",
    #     "right_ranks": correct_ranks,
    #     "word_ranks": all_ranks
    # }
    #
    # rank_res = requests.post(shanbay_url, headers=rank_headers, data=rank_data)
    # rank_result = rank_res.json()["data"]
    # print(rank_result)
    # print("你的单词量为 {}".format(rank_result["vocab"]))
    # print(rank_result["comment"])
else:
    print("请至少选择一个范围")
