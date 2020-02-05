import pandas as pd

print('We will ask you for three inputs.')
path = input("Copy/ paste file path: ")
file_name = input("What would you like the file called? ")
destination = input('Where would you like the file to go? ')

test = pd.read_excel(f'{path}')

name = (f'{destination}' + '/' +f'{file_name}')

writer = pd.ExcelWriter(f'{name}' + '.xlsx', engine = 'xlsxwriter')

test.to_excel(writer)

writer.save()
