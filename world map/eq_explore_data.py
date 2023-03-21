import json

#Explor the structure of the data.
filename = r'world map\data\4.5_day.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
        mag = eq_dict['properties']['mag']
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])

"""
readable_file = 'C:/Users/emidz/OneDrive/Desktop/Aprendizaje de python/proyectos/data/plotting/ploting_main/data/readable_equi_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

"""