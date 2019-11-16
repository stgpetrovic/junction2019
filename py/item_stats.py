import product_metadata
import csv
import co2
import os

print('Reading')
co2s = {}
data = {}
ids = []
header = []
attr_to_column = {}
with open('item_stats_smaller.csv') as infile:
    reader = csv.reader(infile, delimiter=',')
    header = next(reader, None)
    for row in reader:
        data[row[0]] = row
        ids.append(row[0])
next_column = len(header)
extra_columns = 0

def AddColumn(col):
    global header
    global attr_to_column
    global next_column
    global extra_columns
    header += [col]
    attr_to_column[col] = next_column
    next_column += 1
    extra_columns += 1

def Store(ean, attr, value):
    data[ean][attr_to_column[attr]] = value
    
AddColumn('co2')
AddColumn('co2_rank')
AddColumn('pic_url')
product_attrs = sorted(product_metadata.PRETTY_MAP.values())
for attr in sorted(product_attrs):
    AddColumn(attr)

print('Fetching')
present = set()
m = product_metadata.ProductMetadata()
for i in range(0, len(ids), 100):
    batch = ids[i:i + 100]
    for info in m.Infos(batch):
        present.add(info.ean)
        data[info.ean] += ['' for _ in range(extra_columns)]
        co2s[info.ean] = co2.emissions_g(info)
        Store(info.ean, 'co2', co2s[info.ean])
        if info.picurl:
            Store(info.ean, 'pic_url', info.picurl)
        for attr in product_attrs:
            if hasattr(info, attr):
                Store(info.ean, attr, str(getattr(info, attr)))

co2_list = sorted(list(co2s.items()), key=lambda item: item[1])
for i, item in enumerate(co2_list):
    ean = item[0]
    Store(ean, 'co2_rank', i / len(present))

print('Writing')
with open('item_stats_smaller_filtered.csv', 'w') as outfile:    
    writer = csv.writer(outfile, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)
    for ean in sorted(data.keys()):
        row = data[ean]
        if row[0] not in present: continue
        writer.writerow(row)

