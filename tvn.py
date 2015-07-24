import feedparser

import sys

reload(sys)

sys.setdefaultencoding('UTF8')

feedparser._HTMLSanitizer.acceptable_elements.remove('img')

rss = feedparser.parse('http://www.tvn24.pl/najnowsze.xml')

newsfeed1 = rss.entries[0]['title'] + '. ' + rss.entries[0]['description'] + '. ' + rss.entries[1]['title'] + '. ' + rss.entries[1]['description'] + '. ' + rss.entries[2]['title'] + '. ' + rss.entries[2]['description'] + '. ' + rss.entries[3]['title'] + '. ' + rss.entries[3]['description'] + '. '

newsfeed = newsfeed1.replace('"', '')

print newsfeed

