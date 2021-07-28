""" Name: Benton Speck
	Date: Feburary 15, 2019
	Desc: Simple web crawler that searches UIndy's
		  home page and follows the links
"""

import requests
import re

def WebCrawler(url, depth):
	if depth <= 0:
		return
	print("")
	ret = []
	page = requests.get(url)
	url_pattern = re.compile(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+')
	links = url_pattern.findall(page.text)

	for link in links:
		if 'http' in link:
			ret.append(link)

	print("All links for {}".format(url))
	for i in ret:
		print(i)
		WebCrawler(i, depth - 1)
	return ret


def main():
	# url = input("What is the base URL?\n")
	url = 'https://uindy.edu/'
	depth = input("How far do you want to travel?\n")

	links = WebCrawler(url, int(depth) )


if __name__ == '__main__':
	main()
