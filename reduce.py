__author__ = 'Eladio'
import json

def reduce (key, values, rereduce):
    result = {}

    for i in range(0, len(values)):
        for prop in values[i]:
            if values[i][prop] != None:
                if result[prop] == None:
                    result[property] = 0

                result[property] = float(result[prop])+float(values[i][prop])

    return result

def reduce_json(json_file):
    current_date = ""
    current_count = 0
    obj_result = []

    json_object = json.loads(json_file)

    for line in json_object:
        if line['date'] != current_date:
            current_date = line['date']
            current_count = line['count']
            obj_result.append({'date': current_date, 'total_count':current_count})
        else:
            current_count = current_count + line['count']

    return json.dumps(obj_result)