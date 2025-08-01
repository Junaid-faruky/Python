# 6. WordCloud generation
from wordcloud import WordCloud
import matplotlib.pyplot as plt
text = "Python AI ML Data Science Python AI"
wc = WordCloud().generate(text)
plt.imshow(wc)
plt.axis("off")
plt.show()
