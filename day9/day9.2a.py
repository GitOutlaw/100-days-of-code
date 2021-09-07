travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visted, times_visited, cities_visted):
    # new_country = {}
    # new_country["country"] = country_visted
    # new_country["visit"] = times_visited
    # new_country["cites"] = cities_visted
    # travel_log.append(new_country)

    # Another way
    travel_log.append({
        "country": cities_visted,
        "visit": times_visited,
        "cities": cities_visted
    })

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
