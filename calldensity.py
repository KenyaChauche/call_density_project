# Call Density tool for Camano Island Fire Department
## This tool will process a call records document and
## return that document with some columns added. These
## columns will show which calls overlap with the call
## from that row and how many there were. It will only
## do this for calls that start *after* the call in
## that row. It will also do this with specific units,
## since multiple units can be involved in a call. 

try: 
    import pandas as pd

    header_index = 2

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

        try:
            df = pd.read_excel(path, header = header_index)
        except:
            print("Error with file path, please double check filepath")
            continue
        break


    # process excel spreadsheet
    print("Working on your document...")

    try: 
        df = pd.read_excel(path, header = header_index)

        df = df.iloc[0:len(df) - header_index]


        def overlap_incident_ID(p):
            return set({df['Incident Number'][i] for i in set(df.index) - {p} if (df['Dispatched Date'][p] <= df['Dispatched Date'][i] <= df['Clear Date'][p])
                                                                                    and (df['Incident Number'][p] != df['Incident Number'][i])})

        ## old version (returns call IDS for any overlap, regardless of chronicity
        # def overlap(p):
        #    return set(df['Incident Number'][i] for i in set(df.index) - {p} if (df['Dispatched Date'][i] <= df['Dispatched Date'][p] <= df['Clear Date'][i])
        #                                                                     or (df['Dispatched Date'][p] <= df['Dispatched Date'][i] <= df['Clear Date'][p]))

        print("Processing Incidents...")
        
        df['Overlapping Incident Num'] = df.index.map(overlap_incident_ID)

        df['Number of Incidents'] = df['Overlapping Incident Num'].map(len)

        df['Overlapping Incident Num'] = [None if df['Overlapping Incident Num'][i] == set() else df['Overlapping Incident Num'][i] for i in set(df.index)]
        

        def overlap_unit_name(p):
            return set({df["Apparatus Name"][i] for i in set(df.index) - {p} if (df['Dispatched Date'][p] <= df['Dispatched Date'][i] <= df['Clear Date'][p])
                                                                                and (df['Incident Number'][p] != df['Incident Number'][i])})

        print("Processing Units...")
        
        df['Overlapping Apparatus Name'] = df.index.map(overlap_unit_name)

        df['Number of Apparatuses'] = df['Overlapping Apparatus Name'].map(len)

        df['Overlapping Apparatus Name'] = [None if df['Overlapping Apparatus Name'][i] == set() else df['Overlapping Apparatus Name'][i] for i in set(df.index)]

        
    except Exception as e:
        print(e)


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

    df.to_excel(writer, index = False)

    writer.save()

    print("Done!")
except Exception as e:
    print(e)
