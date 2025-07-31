from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Python makes coding fun and creative!"
wc = WordCloud(width=400, height=200, background_color='white').generate(text)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
