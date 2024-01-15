import os
import requests
import bs4
import json

source = requests.get('https://support.microsoft.com/en-us/windows/common-file-name-extensions-in-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01')
soup = bs4.BeautifulSoup(source.text, 'lxml')

table_row = soup.find_all('tr')

my_ext_list = []

for tr_count, row in enumerate(table_row, 1):
    if tr_count == 1:
        continue
    
    for cell_count, each_cell in enumerate(row, 1):
        if cell_count == 2:
            ext = each_cell.text.strip()
#            print(ext)
        if cell_count == 4:
            frmt = each_cell.text.strip()
            
            my_ext_data = {'Index': tr_count, 'Extension': ext,'Format': frmt}
            my_ext_list.append(my_ext_data)
            
my_new_ext_list = my_ext_list[1:]
print(my_new_ext_list)

root_directory = r'C:\Users\pkcar\Downloads'
file_name = 'ext.json'

new_file = open(os.path.join(root_directory, file_name), 'w')
json.dump(my_new_ext_list, new_file, indent = 4)