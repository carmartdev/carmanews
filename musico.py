from requests_html import HTMLSession


url="https://musico.ir/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%D8%A2%D9%87%D9%86%DA%AF/%d8%a7%d8%ad%d8%b3%d8%a7%d9%86-%d8%ae%d9%88%d8%a7%d8%ac%d9%87-%d8%a7%d9%85%db%8c%d8%b1%db%8c/"

session = HTMLSession()

r = session.get(url)

articles = r.html.find('article')

music_index = 0

for item in articles:
    musics = item.find('audio')
    for music in musics:
        music_titles = item.find('.m1h')
        for music_title in music_titles:
            music_titles = music_title.find('a')
            for music_title in music_titles:
                print("Title:",music_title.text)
        artists = item.find('.mokp')
        for artist in artists:
            artistnames = artist.find('span')
            for artistname in artistnames:
                print("Artist:",artistname.text)
        link = music.attrs["src"]
        music_r = session.get(link)
        title = music_title.text
        title = title.replace('دانلود', '')
        title = title.replace('آهنگ', '')
        open(f'musics/{str(artistname)}/{str(title)}.mp3', "wb").write(music_r.content)
        music_index += 1
        # webbrowser.open(link)
        print(link)