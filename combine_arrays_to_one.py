import json
combined_array = []
# ottaa vastaan JSON-tiedoston, jossa on useita arrayta ja tekee niistä yhden ison arrayn
with open ("suodatettu.json", "r") as f:
    imported_json = json.load(f)
    for i in range(len(imported_json)):
        for j in range(len(imported_json[i])):
            combined_array.append(imported_json[i][j])
    
with open("suodatettu_yhdistetty.json", "w") as f:

    json.dump(combined_array, f)

