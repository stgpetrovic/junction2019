import product_metadata
import csv

print('Reading')
data = {}
ids = []
with open('item_stats_smaller.csv') as infile:
    reader = csv.reader(infile, delimiter=',')
    header = next(reader, None)
    for row in reader:
        data[row[0]] = row
        ids.append(row[0])

next_column = len(header)
attr_to_column = {}
product_attrs = sorted(product_metadata.PRETTY_MAP.values())
for attr in sorted(product_attrs):
    attr_to_column[attr] = next_column
    next_column += 1
header += product_attrs

print('Fetching')
present = set()
m = product_metadata.ProductMetadata()
for i in range(0, len(ids), 100):
    batch = ids[i:i + 100]
    for info in m.Infos(batch):
        present.add(info.ean)
        data[info.ean] += ['' for _ in product_attrs]
        for attr in product_attrs:
            if hasattr(info, attr):
                data[info.ean][attr_to_column[attr]] = str(getattr(info, attr))
                
print('Writing')
with open('item_stats_smaller_filtered.csv', 'w') as outfile:    
    writer = csv.writer(outfile, delimiter=',', quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)
    for ean in sorted(data.keys()):
        row = data[ean]
        if row[0] not in present: continue
        writer.writerow(row)

