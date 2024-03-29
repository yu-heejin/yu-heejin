import feedparser, time

URL = "https://medium.com/@hee98.09.14/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=vo3ov1111)](https://solved.ac/vo3ov1111/)

## Project
### Devridge (2023.12.28 ~)
> Community for Developers
>
**Repository**
* [Backend](https://github.com/devridge-team-project/devridge-server)
### GGOOMi (2023.08.21 ~ 2023.09.02)
> Draw my diary with DALLE ☺️
>
**Repository**
* [Backend](https://github.com/prompter-day-2023)
### Ladder (2022.08.27 ~ 2022.10.01)
> Website Project changing recognized person in picture
>
**Repository**
* [DevOps](https://github.com/2022-SeongNam-Team-C/Ladder-docker)
* [Backend](https://github.com/2022-SeongNam-Team-C/Ladder-Backend)
### Police In My Pocket (2022.04.15 ~ 2022.11.30)
> App Project for my safety in Emergency
>
**Repository**
* [Frontend](https://github.com/hanium-project/Police-in-my-pocket-frontend)
* [Backend](https://github.com/hanium-project/Police-in-my-pocket-backend)

## Recent Post 
"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
