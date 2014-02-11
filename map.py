

def getMetricDict(doc,data):
    #returns a dictionary with the metric names as keys and counts as values for
	#// a report at a given index.
    metrics = {}
    mn = doc['report']['metrics']

    for i in range(0, len(mn)-1):
        key = mn[i]['name']
        val = data['counts'][i]
        metrics[key] = val
    return metrics

def getBaseDimensions(doc):
    #// returns the basic dimensions that all emits share per source document /
	#// Omniture report.
	#// TODO: Review what we should really have in here.
    return {
        #'name'    : doc.documentType,
        'type'    : doc['report']['elements'][0]['id'],
        'segment' : doc['report']['segment_id'],
        'date'    : doc['report']['period']
    }

def mapOmniture(doc, dims, vals):

    leng = len(doc['report']['data'])

    for i in range (0, leng - 1):

        keyword = doc['report']['data'][i]['name']
        dim = getBaseDimensions(doc)
        dim['keyword'] = keyword
        data = doc['report']['data'][i]
        metrics = getMetricDict(doc,data)

        new_doc = {}
        new_doc['dims'] = dim
        new_doc['vals'] = metrics
        mapDocument(new_doc, dims, vals)

def mapDocument (doc, dims, vals):
    keys = []

    for i in range(0, len(dims)):
        keys.append(doc['dims'][dims[i]])

    values = {}

    for j in range(0, len(vals)-1):
        values[vals[j]] = doc['vals'][vals[i]]

    print keys, values

##Map Function
def map (doc):
    dims  = ['segment', 'date', 'keyword']
    vals = ['Visits']

    mapOmniture(doc, dims, vals)

