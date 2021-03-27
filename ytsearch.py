from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from time import sleep
import argparse

parser = argparse.ArgumentParser(description="This program searches youtube for desired query and opens desired number of video.\n",prog="ytsearch")
parser.add_argument("query", type=str, help="This is what the program will search on YouTube")
parser.add_argument("-n","--n", type=int, help="(Optional Argument) From the top, this number-th video will be played. First video will be played if not specified.")
args = parser.parse_args()

def SearchYT(query,n):
    if n==None:
        n=1
    c_options = wb.ChromeOptions()
    c_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    c_options.add_extension("D:\\Downloads\\adblock.crx")

    br = wb.Chrome(options=c_options)
    br.get("https://www.youtube.com/results?search_query="+query)

    sleep(3)
    br.find_elements_by_id("video-title")[n-1].click()
    return br

a = SearchYT(args.query,args.n)