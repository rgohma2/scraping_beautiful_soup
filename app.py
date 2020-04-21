# ***IMPORTS***
import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('http://english.www.gov.cn/policies/latestreleases/')


# first param is variable to scrape from second will be 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser') 

# soup is an object with built in methods 
# such as....

# variable = soup.select('enter-id-here')
	# similar to jquery can take class name, id name, or html element
	# RETURNS ITEMS BACK IN LIST EVEN IF THERE IS ONLY ONE ITEM RETURNED

# variable = soup.find(id='enter-id-here')
# variable = soup.find(class_='enter-class-here') <---- NOTICE UNDERSCORE AFTER CLASS
# variable = soup.find(attrs={data-name: "string"})


# TEST CASES
container = soup.find(class_='list-container')
li_list = container.contents[3].contents
# print(li_list)

# removes all the line breaks from the list
def skip_a_line(list):
	return list[1::2]


li_list = skip_a_line(li_list)
print(li_list)
	

print('hello world')



