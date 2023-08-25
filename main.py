from requests_html import HTMLSession
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from translate import Translator
import webbrowser

root = ttk.Window(themename="darkly")

session = HTMLSession()

# google_url = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR1owYkhnU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen'

# google_r = session.get(google_url)

# google_articles = google_r.html.find('article')

keyhan_url = 'https://kayhan.ir/'

keyhan_r = session.get(keyhan_url)

keyhan_titles = keyhan_r.html.find('h2')

def open_new(newurl):
    for url in newurl:
        webbrowser.open(url)

print("KEYHAN")
for item in keyhan_titles:
        new = item.find('a', first=True)
        title = new.text
        link = new.absolute_links
        print(title, link)
        label = ttk.Label(text=title)
        label.pack()
        button = ttk.Button(text="Go to the new", command = open_new(link))
        button.pack()
# print("GOOGLE")
# for item in google_articles:
#     try:
#         new = item.find('h4', first=True)
#         translator = Translator(to_lang="fa")
#         title = translator.translate(new.text)
#         link = new.absolute_links
#         print(title, link)
#         label = ttk.Label(text=title)
#         label.pack()
#         # button = ttk.Button(text="Go to the new", command = open_new(link))
#         # button.pack()
#     except:
#         pass

root.mainloop()
