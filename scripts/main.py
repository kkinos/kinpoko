import textwrap
import feedparser


RSS_URL = 'https://kinpokoblog.com/rss.xml'
GENERATE_FILE_NAME = 'README.md'

def main():
    

    # ブログの新着記事以外の部分を書き込む
    docs = textwrap.dedent("""\


    # Hi!
    
    [![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=kinpoko)](https://github.com/anuraghazra/github-readme-stats)
    
    [![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=kinpoko&langs_count=8&layout=compact)](https://github.com/anuraghazra/github-readme-stats)
    
    ## Recent Posts on [my blog](https://kinpokoblog.com)
    """)


    with open(GENERATE_FILE_NAME, 'w') as f:
        f.write(docs)


    # ブログの新着記事を書き込む
    d = feedparser.parse(RSS_URL)
    for entry in d.entries:
        docs = textwrap.dedent("""\
            - [{title}]({url})
            """).format(
                title = entry.title,
                url = entry.link
            )

        with open(GENERATE_FILE_NAME, 'a') as f:
            f.write(docs)




if __name__ == '__main__':
    main()
