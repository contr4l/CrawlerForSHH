from wordcloud import WordCloud
import time
import Crawl_test
import Analyze

#f = open(Crawl_test.filename + '_Word.txt','r').read()

wordcloud = WordCloud(font_path = r'C:\Users\ctrl\Desktop\CrawlForSHH\FZDHJT.TTF',background_color="white",width=2000, height=2000, margin=2).generate_from_frequencies(Analyze.new_tags)


import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file(Crawl_test.filename+'.png')