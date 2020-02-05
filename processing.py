
import pandas as pd
header_index = 2
df = pd.read_excel(path, header = header_index)
df = df.iloc[0:len(df) - header_index]
def overlap(p):
    return {df['Incident Number'][i] for i in set(df.index) - {p} if (df['Dispatched Date'][i] <= df['Dispatched Date'][p] <= df['Clear Date'][i])
                                                                     or (df['Dispatched Date'][p] <= df['Dispatched Date'][i] <= df['Clear Date'][p])}
df['overlap'] = df.index.map(overlap)
df['num_overlaps'] = df.overlap.map(len)
df.to_excel(location + filename)
