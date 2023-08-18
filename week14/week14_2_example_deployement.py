import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
import json

model = None
with open('rf_classifier.pickle', "rb") as input_file:
    model = pickle.load(input_file)

pca = None
with open('pca.pickle', "rb") as input_file:
    pca = pickle.load(input_file)

minmaxes = None
with open('minmaxes.json', 'r') as openfile:
    # Reading from json file
    minmaxes = json.load(openfile)



def predictArray( data: np.array ) -> int:

    gender = {'Male': 1, 'Female': 0}
    ctype = {'Loyal Customer': 1, 'disloyal Customer': 0}
    ttype = {'Personal Travel': 1, 'Business travel': 0}
    classtype = {'Eco': 0, 'Eco Plus': 0, 'Business': 1}

    data[0] = gender[ data[0] ]
    data[1] = ctype[ data[1] ]
    data[2] = ttype[ data[2] ]
    data[3] = classtype[ data[3] ]

    cols = list(minmaxes.keys())

    data = [float(q) for q in list(data)]
    for i in range(len(data)):
        data[i] = (data[i] - minmaxes[cols[i]]['min']) / (minmaxes[cols[i]]['max'] - minmaxes[cols[i]]['min'])

    pca_result = pca.transform( [data] )[0][0]
    data = list(data)
    data.append( pca_result )

    return model.predict( [data] )[0]


def predict( Gender,Customer_Type,Type_of_Travel,Class,Seat_comfort,
        Food_and_drink,Inflight_wifi_service,Inflight_entertainment,
        Online_support,Ease_of_Online_booking,On_board_service,
        Leg_room_service,Baggage_handling,Cleanliness,
        Online_boarding,Entertainment_Score,Service_Rating,
        Total_Online_Support_Score ) -> int:

    return predictArray( np.array([Gender,Customer_Type,Type_of_Travel,Class,Seat_comfort,
        Food_and_drink,Inflight_wifi_service,Inflight_entertainment,
        Online_support,Ease_of_Online_booking,On_board_service,
        Leg_room_service,Baggage_handling,Cleanliness,
        Online_boarding,Entertainment_Score,Service_Rating,
        Total_Online_Support_Score]) )


r = predict( 'Male', 'Loyal Customer', 'Personal Travel', 'Eco', 4, 3, 3, 4, 2, 1, 4, 4, 4, 4, 4, 4, 4,4 )

print("FINAL RESULT", r)
