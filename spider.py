import requests
import re  
import sys
import urlparse

try:
    target_list=[]

    def get_url(target_url):
        try:
            response = requests.get("http://" + target_url)
            return response
        except requests.exceptions.ConnectionError:
            pass

    def filter_content(content):
        result = re.findall('(?:href=")(.*?)"',content)
        return result

    def crawl(response):
        href_list = filter_content(response)
        for link in href_list:
            link = urlparse.urljoin(target_url,link)
            if target_url in link and link not in target:
                target_list.append(link)
                print(link)
                crawl(link)
    
    target_url = raw_input("Enter the target website name:")
    response = get_url(target_url)
                
    crawl(response.content)


except KeyboardInterrupt:
    print("\nExiting..")
    sys.exit()