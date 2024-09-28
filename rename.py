import os

directory = "./Monthly_Average_Groundwater_Level"

for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Grundwasserstand-Monatsmittel-"):
        new_filename = filename.replace("Grundwasserstand-Monatsmittel-", "")
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)
        os.rename(old_filepath, new_filepath)
