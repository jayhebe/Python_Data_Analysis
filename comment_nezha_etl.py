import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from imageio import imread


f_comment = open("comments.txt", 'rb')
words = []
for line in f_comment.readlines():
    if (len(line)) == 12:
        continue
    A = jieba.cut(line)
    words.append(" ".join(A))
# 去除停用词
stopwords = [',', '。', '【', '】', '”', '“', '，', '《', '》', '！', '、', '？', '.', '…', '1', '2', '3', '4', '5', '[', ']',
             '（', '）', ' ']
new_words = []
for sent in words:
    word_in = sent.split(' ')
    new_word_in = []
    for word in word_in:
        if word in stopwords:
            continue
        else:
            new_word_in.append(word)
    new_sent = " ".join(new_word_in)
    new_words.append(new_sent)

final_words = []
for sent in new_words:
    sent = sent.split(' ')
    final_words += sent
final_words_flt = []
for word in final_words:
    if word == ' ':
        continue
    else:
        final_words_flt.append(word)

text = " ".join(final_words_flt)
font = r'C:\Windows\Fonts\FZSTK.TTF'
bk = imread("bj.png")
wc = WordCloud(collocations=False, mask=bk, font_path=font, width=1400, height=1400, margin=2).generate(text.lower())
image_colors = ImageColorGenerator(bk)
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
plt.figure()
plt.imshow(bk, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
wc.to_file('word_cloud1.png')
