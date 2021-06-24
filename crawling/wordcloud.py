from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO

def cloud(text):
    wordcloud = WordCloud(font_path='', background_color='white').generate(text)
    plt.figure(figsize=(30,30))
    plt.imshow(wordcloud, interpolation='lanczos')
    plt.axis('off')
    img = BytesIO()
    plt.savefig(img, format='png', dpi=800)
    wordcloud.to_file('wordcloud.png')
    return img
