from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO

def cloud(text):
    wordcloud = WordCloud(font_path='C:\\Users\\rlagu\\Desktop\\폰트\\고딕체\\NIXGONFONTS B 2.0.ttf', background_color='white').generate(text)
    plt.figure(figsize=(30,30)) #이미지 사이즈 지정
    plt.axis('off') #x y 축 숫자 제거
    img = BytesIO()
    plt.savefig(img, format='png', dpi=600)
    wordcloud.to_file('wordcloud.png')
    return img
