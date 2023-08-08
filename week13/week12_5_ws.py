
#: Import web service packages
import re
from fastapi import FastAPI
import uvicorn
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import json

# open a file, where you stored the pickled data
file = open('week12_5_model.pickle', 'rb')
model = pickle.load(file)
file.close()

file = open('week12_5_scaler.pickle', 'rb')
scaler = pickle.load(file)
file.close()

#: Load the state zip
statezip = None
with open('week12_5_statezip.json') as json_file:
    statezip = json.load(json_file)

#: Calculate the maxes and mins
columns_order = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
       'waterfront', 'view', 'condition', 'sqft_above', 'sqft_basement',
       'yr_built', 'yr_renovated', 'statezip_value']

maxes = { columns_order[i]:scaler.data_max_[i] for i in range(len(scaler.data_max_)) }
mins =  { columns_order[i]:scaler.data_min_[i] for i in range(len(scaler.data_min_)) }


#: Create the web service application
app = FastAPI()

#: Create a main function to be called from outside
@app.get("/estimate")
async def estimate(bedrooms, bathrooms, sqft_living, sqft_lot, floors,
       waterfront, view, condition, sqft_above, sqft_basement,
       yr_built, yr_renovated, statezip_value):

    #: Create a list of incoming values
    row = [bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, sqft_above, sqft_basement, yr_built, yr_renovated]
    cols = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated']

    #: For each values
    for i in range(len(row)):
        v = row[i]

        #: If none, EXIT
        if v == None:
            return {"type":"error", "result": "the given value is None"}
        
        #: If not numeric, EXIT
        if not re.match(r"^[0-9\,\.\-]+$", v):
            return {"type":"error", "result": "the given value is numeric"}
        
        #: Check min, max
        #if float(v) < mins[cols[i]]: 
        #    return {"type":"error", "result": f"the given value is LOWER than limit {i}, {cols[i]}"}
        #if float(v) > maxes[cols[i]]: 
        #    return {"type":"error", "result": f"the given value is HIGHER than limit {i}, {cols[i]}"}

    #: Check state value is in DICT
    if statezip_value not in statezip:
        return {"type":"error", "result": "the given value is not in state DICT"}

    #: Append to list
    row.append( statezip_value )

    #: Transform into value
    row[-1] = statezip[ statezip_value ] # WA 98001

    #: Parse into floats
    row = [float(r) for r in row]

    #: Transform, min max scale
    rowT = scaler.transform([ row ])

    #: Predict
    result = model.predict( rowT )[ 0 ]

    #: Return
    return {"type":"ok", "result": result}







uvicorn.run(
    app,
    host="0.0.0.0",
    port=5003,
    log_level="debug",
)

