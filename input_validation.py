# Kenya

if path == None:
    path = input("File path missing value, please copy/paste the file path for the document to process: ")

if destination == None:
    destination = input("Destination path missing value, please
    copy/paste the file path for the destination folder: ")

if file_name == None:
    file_name = input("File name missing value, please input what you would like the processed file to be called: ")

if destination[len(destination)] != "/":
    destination = destination + "/"

if ".xls" not in file_name:
    file_name = file_name + ".xls"

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
