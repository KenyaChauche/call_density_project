# whole team

import pandas as pd
# gather inputs from user
print('We will ask you for three inputs.')
while True:
    # read input
    path = input("Copy/ paste file path: ")
    if path == "":
        print("File path missing value, please double check filepath")
        continue

    # cleaning
    path = path.rstrip()

    path = path.replace('"', '')

    # read in file
    header_index = 2

    try:
        df = pd.read_excel(path, header = header_index)
    except:
        print("Error with file path, please double check filepath")
        continue
    break


# process excel spreadsheet
print("Working on your document...")

header_index = 2

df = pd.read_excel(path, header = header_index)

df = df.iloc[0:len(df) - header_index]

def overlap(p):
    return {df['Incident Number'][i] for i in set(df.index) - {p} if (df['Dispatched Date'][i] <= df['Dispatched Date'][p] <= df['Clear Date'][i])
                                                                     or (df['Dispatched Date'][p] <= df['Dispatched Date'][i] <= df['Clear Date'][p])}

df['overlap'] = df.index.map(overlap)

df['num_overlaps'] = df.overlap.map(len)




while True:
    file_name = input("What would you like the file called? ")
    if file_name == "":
        print("File name empty, please enter a value.")
        continue

    destination = input("Where would you like the file to go? ")
    if destination == "":
        print("File path missing value, please double check destination filepath and re-enter file name and destination filepath")
        continue

    # cleaning

    destination = destination.rstrip()

    destination = destination.replace('"', '')

    if not destination.endswith("\\"):
        destination = destination + "\\"

    file_name = file_name.rstrip()

    if file_name.endswith(".xls"):
        file_name.remove(".xls")

    if ".xlsx" not in file_name:
        file_name = file_name + ".xlsx"

    try:
        df.to_excel(f"{destination + file_name}")
    except Exception as e:
        print(e)
        print("An error has occurred. Please re-enter the folder destination and file name.")
        continue

    break


name = (f'{destination + file_name}')

writer = pd.ExcelWriter(f'{name}', engine = 'xlsxwriter')

df.to_excel(writer)

writer.save()

print("Done!")
