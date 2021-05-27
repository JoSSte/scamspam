import json

# quick and dirty file to clean up duplicates in json file

bins = json.loads(open('../data/danish_bin.json', encoding='utf-8').read())
print(len(bins))
unique = { each['IIN'] : each for each in bins }.values()

print(len(unique))

jsonString = json.dumps(list(unique))
jsonFile = open("../data/danish_bin2.json", "w", encoding='utf-8')
jsonFile.write(jsonString)
jsonFile.close()