import pandas as pd

# Carica i CSV e rimuove le colonne non necessarie
accident = pd.read_csv(r"C:\Users\david\Downloads\UK_Accident.csv").drop(columns=[
    "Carriageway_Hazards", "1st_Road_Class", "1st_Road_Number", "2nd_Road_Class", "2nd_Road_Number",
    "Did_Police_Officer_Attend_Scene_of_Accident", "Special_Conditions_at_Site",
    "Location_Easting_OSGR", "Location_Northing_OSGR", "LSOA_of_Accident_Location", "Year", "InScotland"])

vehicles = pd.read_csv(r"C:\Users\david\Downloads\UK_Accident_Vehicles.csv").drop(columns=[
    "Driver_IMD_Decile",
    "Hit Object in Carriageway",
    "Hit Object off Carriageway",
    "Journey_Purpose_of_Driver",
    "Vehicle Location.Restricted Lane",
    "Vehicle Reference",
    "Was_Vehicle_Left_Hand_Drive"
])

# Mantieni solo gli incidenti che hanno un veicolo associato (filtraggio senza aggiungere colonne)
accident_filtered = accident[accident["Accident_Index"].isin(vehicles["Accident_Index"])]

# Mantieni solo i veicoli che hanno un incidente associato
vehicles_filtered = vehicles[vehicles["Accident_Index"].isin(accident["Accident_Index"])]

# Salva i nuovi file CSV
accident_filtered.to_csv(r"C:\Users\david\Downloads\UK_Accident_ETL.csv", index=False)
vehicles_filtered.to_csv(r"C:\Users\david\Downloads\UK_Accident_Vehicles_ETL.csv", index=False)

print("Filtraggio completato e file salvati.")
