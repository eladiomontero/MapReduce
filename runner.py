__author__ = 'Eladio'
import map
import reduce
import json
import glob

#############################################
def load_files(url):
    files= glob.glob(url)
    json_out = []
    keys = []
    values = []

    for file in files:

        json_file= open(file,'r')
        json_object = json.load(json_file)
        keys, values = map.map(json_object)

    return keys, values

json_mapped = load_files("./data/*.json")

json_reduced = reduce.reduce_json(json_mapped)

print json_reduced

