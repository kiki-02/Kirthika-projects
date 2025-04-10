import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the model and preprocessing objects
model = pickle.load(open("model.pkl", "rb"))
preprocessor = pickle.load(open("preprocessor.pkl", "rb"))

# Streamlit UI
st.title("Chennai House Price Prediction App")

# Dropdown options
area_options = ['Chrompet', 'Karapakkam', 'KK Nagar', 'Velachery', 'Anna Nagar', 'Adyar', 'T Nagar']
sale_cond_options = ['AdjLand', 'Partial', 'Normal Sale', 'AbNormal', 'Family']
park_facil_options = ['Yes', 'No']
buildtype_options = ['House', 'Others', 'Commercial']
utility_avail_options = ['AllPub', 'NoSewer', 'ELO']
street_options = ['Paved', 'Gravel', 'No Access']
mzzone_options = ['RL', 'RH', 'RM', 'C', 'A', 'I']

# User Inputs
AREA = st.selectbox("Area", area_options)
INT_SQFT = st.number_input("Built-up Area (in sqft)", min_value=100, step=1)
DIST_MAINROAD = st.number_input("Distance from Main Road (in meters)", min_value=0, step=1)
N_BEDROOM = st.number_input("Number of Bedrooms", min_value=0, step=1)
N_BATHROOM = st.number_input("Number of Bathrooms", min_value=0, step=1)
N_ROOM = st.number_input("Total Number of Rooms", min_value=1, step=1)
SALE_COND = st.selectbox("Sale Condition", sale_cond_options)
PARK_FACIL = st.selectbox("Parking Facility", park_facil_options)
BUILDTYPE = st.selectbox("Build Type", buildtype_options)
UTILITY_AVAIL = st.selectbox("Utility Availability", utility_avail_options)
STREET = st.selectbox("Street Type", street_options)
MZZONE = st.selectbox("Zone", mzzone_options)
QS_ROOMS = st.slider("Quality Score - Rooms", 0.0, 10.0, step=0.1)
QS_BATHROOM = st.slider("Quality Score - Bathroom", 0.0, 10.0, step=0.1)
QS_BEDROOM = st.slider("Quality Score - Bedroom", 0.0, 10.0, step=0.1)
QS_OVERALL = st.slider("Overall Quality Score", 0.0, 10.0, step=0.1)
REG_FEE = st.number_input("Registration Fee", min_value=0, step=1000)
COMMIS = st.number_input("Commission", min_value=0, step=1000)

# Prediction
if st.button("Predict House Price"):
    input_data = pd.DataFrame([[
        AREA, INT_SQFT, DIST_MAINROAD, N_BEDROOM, N_BATHROOM, N_ROOM,
        SALE_COND, PARK_FACIL, BUILDTYPE, UTILITY_AVAIL, STREET,
        MZZONE, QS_ROOMS, QS_BATHROOM, QS_BEDROOM, QS_OVERALL,
        REG_FEE, COMMIS
    ]], columns=[
        'AREA', 'INT_SQFT', 'DIST_MAINROAD', 'N_BEDROOM', 'N_BATHROOM', 'N_ROOM',
        'SALE_COND', 'PARK_FACIL', 'BUILDTYPE','UTILITY_AVAIL','STREET',
        'MZZONE', 'QS_ROOMS', 'QS_BATHROOM', 'QS_BEDROOM', 'QS_OVERALL',
        'REG_FEE', 'COMMIS'
    ])

    processed_input = preprocessor.transform(input_data)
    prediction = model.predict(processed_input)
    st.success(f"Predicted House Price: ₹ {int(prediction[0]):,}")
