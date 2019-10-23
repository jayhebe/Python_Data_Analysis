import requests
import openpyxl


zhihu_wb = openpyxl.Workbook()
zhihu_sheet = zhihu_wb.active
zhihu_sheet.title = "Blog - Zhang Jiawei"

zhihu_sheet["A1"] = "标题"
zhihu_sheet["B1"] = "链接"
zhihu_sheet["C1"] = "摘要"

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
zhihu_base_url = "https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles"
zhihu_page_offset = 0

while True:
    zhihu_param = {
        "include": "data[*].comment_count, suggest_edit, is_normal, \
        thumbnail_extra_info, thumbnail, can_comment, comment_permission, \
        admin_closed_comment, content, voteup_count, created, updated, \
        upvoted_followees, voting, review_info, is_labeled, label_info; \
        data[*].author.badge[?(type=best_answerer)].topics",
        "offset": str(zhihu_page_offset),
        "limit": "20",
        "sort_by": "voteups"
    }
    zhihu_res = requests.get(zhihu_base_url, headers=header, params=zhihu_param)
    zhihu_data = zhihu_res.json()["data"]
    if len(zhihu_data) != 0:
        for data in zhihu_data:
            row = list()

            title = data["title"]
            link = data["url"]
            description = data["excerpt"]

            row.append(title)
            row.append(link)
            row.append(description)

            zhihu_sheet.append(row)
    else:
        break

    zhihu_page_offset += 20

zhihu_wb.save("zhihuzhangjiawei.xlsx")
