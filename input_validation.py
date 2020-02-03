# Kenya

# input validation
if path == None:
    path = input("File path missing value, please copy/paste the file path for the document to process: ")

if destination == None:
    destination = input("Destination path missing value, please
    copy/paste the file path for the destination folder: ")

if file_name == None:
    file_name = input("File name missing value, please input what you would like the processed file to be called: ")

# path and filename formatting

while destination[len(destination)] == " ":
    del destination[len(destination)]

while path[len(path)] == " ":
    del path[len(path)]

while file_name[len(file_name)] == " ":
    del file_name[len(file_name)]

if destination[len(destination)] != "/":
    destination = destination + "/"

# must specifically be .xlsx at end to work with ExcelWriter
if ".xls" in file_name:
    file_name.remove(".xls")

if ".xlsx" not in file_name:
    file_name = file_name + ".xlsx"



# file read in and read out validation

try:
    df = pd.read_excel(f"{path}", header = header_index)
except:
    path = input("Error with file path, please double check path and copy/paste file path for document to process: ")

try:
    df.to_excel(f"{destination + file_name}")
except:
    print("An error has occurred. Please re-enter the folder destination and file name.")
    file_name = input("File name: ")
    destination = input("Path to folder: ")
