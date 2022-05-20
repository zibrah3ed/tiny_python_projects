#! /Users/tyson/.virtualenvs/tiny_python_projects/bin/python
"""
Authors: TEF, KYC
Purpose: Say Hello
"""
from urllib.request import urlopen

def main():

    testsites = ("https://key.kossconstruction.com"
                ,"https://vrl.kossconstruction.com"
                ,"https://mail.bettisasphalt.com"
                ,"https://vpn.bettisasphalt.com"
                ,"https://ba-manage.bettisasphalt.com")


    for testsite in testsites:
        url = testsite
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        
        tagToFind = "<title>"
        title_index = html.find(tagToFind)
        start_index = title_index + len(tagToFind)
        end_index = html.find("</title>")
        title_string = html[start_index:end_index]
        print(title_string)




if __name__ == '__main__':
    main()
