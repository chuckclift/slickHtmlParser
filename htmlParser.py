#!/usr/bin/python3
import re

def get_urls(html):
    regex = "<a.*?>"
    anchor_list = re.findall(regex, html)
    html_urls = []
    
    # getting the urls from the html document    
    for a in anchor_list:
        url_beginning = a.find("href=") + 6
 
        if url_beginning is not -1:
            _ = a[url_beginning:-1]
            url_end = _.find("\"")
            url = _[0:url_end]
            html_urls.append(url)

    # filtering out the "#" values
    html_urls = [x for x in html_urls if x.strip() is not "#"]


    # filtering out all values that don't start with "http" or
    # "/" so that only values like these remain
    #        "https://www.whatever.com
    #        "/relative/link/

    for i in html_urls:
        # filtering out all values that don't start with 
        # "http" or "/"
        http_at_start = i.startswith("http")
        slash_at_start = i.startswith("/")

       
        if not http_at_start and not slash_at_start:
            html_urls.remove(i) 

    return html_urls 
        
    
def get_paragraphs(html):    
    pContent = ""

    ##getting everything that is inside of the p tags
    while True:
        tagOpen = html.find("<p")
        tagClose = html.find("</p")

        pContent = pContent + html[tagOpen:tagClose]
        html = html[tagClose + 3:]

        if tagClose == -1:
            break

    ##getting rid of all tags so the text is readable
    while True:
        tagOpen = pContent.find("<")
        tagClose = pContent.find(">")

        if tagOpen == 0:
            pContent = pContent[tagClose + 1:]
            
        elif tagClose < tagOpen:
            pContent = pContent[tagClose + 1:]
            
        else:
            pContent = pContent[:tagOpen - 1] + pContent[tagClose + 1:]
            
        if tagOpen == -1 or tagClose == -1:
            break
        
    return pContent
 

    
if __name__ == "__main__":
    with open("example.html", encoding="utf-8") as f:
        sampleHtml = f.read()
    url_list = get_urls(sampleHtml) 
    for a in url_list:
        print(a)
    
