#!/usr/bin/env python3

import sys
import os
import re

WEBSITE_BASE = "https://iosifache.me"

if len(sys.argv) != 2:
    exit(1)

article_file = sys.argv[1]
if not os.path.isfile(article_file):
    exit(1)

with open(article_file) as article:
    content = article.read()

    content = content[content.find("---\n\n") + 5:]

    link_id = 1
    links = []
    new_text = ""
    cursor = 0
    for match in re.finditer(r"\[(.*?)\]\((.*?)\)", content):
        start = match.start()
        end = match.end()
        text, link = match.groups()

        links.append(link)

        new_text += content[cursor:start] + text + " [" + str(link_id) +  "]"
        link_id += 1
        cursor = end
    
    new_text += content[cursor:]
    
    new_text += "\n\n"
    for link_id, link in enumerate(links):
        if link.startswith("/"):
            link = WEBSITE_BASE + link

        new_text += f"[{link_id + 1}] {link}\n"
    
    print(new_text, end="")