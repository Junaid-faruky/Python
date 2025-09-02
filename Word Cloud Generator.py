from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = open("book.txt").read()
wc = WordCloud(width=800, height=400, background_color="white").generate(text)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
