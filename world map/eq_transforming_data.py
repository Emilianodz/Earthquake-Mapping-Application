import json

#Explor the structure of the data.
filename = r'world map\data\4.5_day.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = r'world map\data\readable_equi_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)