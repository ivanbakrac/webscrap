import re
import time

import requests
from bs4 import BeautifulSoup


def web_scrap(url):
    text_scrap = (
        []
    )  # create empty list to be updated with text and append Purpose and Name
    success = False  # set success by default as false, if True, Requests is Success
    f = open("text_scrap.txt", "w")
    for response in range(50):
        try:
            response = requests.get(url)
            success = True
            soup = BeautifulSoup(response.content, "html.parser")  # parse html
            soup_text = soup.get_text()  # get text
            extract_name = re.findall(
                r"Name.+", soup_text
            )  # find words that begin with "Name"
            extract_purpose = re.findall(
                r"Purpose.+", soup_text
            )  # find words that begin with "Purpose"
            extract_all = extract_name + extract_purpose  # sum up the strings
            text_scrap.append(extract_all)  # append name and purpose in the list
        except:
            if response < 2:  # try 2 times else break the loop, request with no success
                print("the attempt to get the response failed")
                time.sleep(2)
                continue
            else:
                break
    if not success:
        return None
    f.write(
        str(text_scrap)
    )  # write the list to text file, each list item has name + purpose = list of lists
    f.close()


url1 = "http://18.207.92.139:8000/random_company"
if __name__ == "__main__":
    web_scrap(url1)
