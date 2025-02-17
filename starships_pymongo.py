import json, requests, os
import pymongo
import pickle
import pprint

from bson import ObjectId

# ###
# '''
# Step 1: Connect MongoDB to Python.
# Step 2: Fetch the starships from the Star Wars API
# Step 3: Use a dictionary to slice the data with the fields we need.
# The fields are [name, model, manufacturer, length, max_atmosphering_speed, crew, passengers, pilot]
# Step 4: Replace "pilot" field with the right ObjectId's using pymongo to fetch the character documents.
# Step 5: Make a function to add starships (with updated "pilot" fields) from dictionary one by one to
# a document in MongoDB.
# '''
#
# url = "https://swapi.dev/api/starships/?page="
# response = []
# for i in range(1, 5):
#     response.append(requests.get(url + f"{i}"))
# # print(response)
# list_of_starships = []
# for item in response:
#     list_of_starships.append(json.loads(item.text)["results"])
#
# full_starships = list_of_starships[0] + list_of_starships[1] + list_of_starships[2] + list_of_starships[3]
# # print(full_starships)
# # print(len(full_starships))
# print(full_starships[4]["pilots"])
# url_10 = full_starships[10]["pilots"][0]
# # print("Length of list: ", len(url_10))
# # print("URL: ", url_10[0])
# # print("Length of list: ", len(url_10[0]))
# response_10 = requests.get(url_10)
# name_of_pilot = json.loads(response_10.text)["name"]
# print("Name of Pilot: ", name_of_pilot)
# print(type(name_of_pilot))
#
# '''
# 1. A dictionary as input
# 2. Access "pilots" field
# 3. Use the API to request info from the URL in "pilots"
# 4. Some "pilots" are empty
# 5. From that URL, get the name of the pilot using ["name"]
# as a slicer
# 6. Fetch the document with that name from your MongoDB collection
# of Star Wars characters
# 7. From that document, get the ID
# 7b. Created a dictionary with pilot names and assigned IDs ready to replace URLs
# 8. Replace the URL in "pilots" with
# the ID e.g. ObjectId("sw89sg8ys89gs")
# 9. Final dictionary should be the same except for every URL in "pilots"
# is replaced with the ObjectId from the MongoDB db.
# 10. Loop over the dictionaries in list "full_starships"
# and create new list of dictionaries.
# '''
#
#
# def get_name(dictionary):
#     client = pymongo.MongoClient()  # This automatically calls the default address of our connection
#     db = client["starwars"]
#
#     # We must call the following values from the dictionary:
#     # [name, model, manufacturer, length, max_atmosphering_speed, crew, passengers, pilot]
#
#     new_dict = {}
#     for value in ["name", "model", "manufacturer", "length", "max_atmosphering_speed", "crew", "passengers", "pilots"]:
#         new_dict[value] = dictionary[value]
#     #print(new_dict)
#     pilot_urls = new_dict["pilots"]
#     if pilot_urls == []:
#         return new_dict
#     else:
#         pilot_names = {}
#         for i, pilot_url in enumerate(pilot_urls):
#             response = requests.get(pilot_url)
#             # Get name
#             pilot_name = json.loads(response.text)["name"]
#             # Get ID
#             pilot_id = db.characters.find_one({"name": pilot_name}, {"_id": 1})
#             replacement_id = ObjectId(pilot_id['_id'])
#             new_dict["pilots"][i] = replacement_id
#             #pilot_names["Pilot Name"].append(json.loads(response.text)["name"])
#
#     return new_dict
#
# #print(get_name(full_starships[4]))
# transformed_dicts = []
# for i in range(36):
#     print(i)
#     transformed_dicts.append(get_name(full_starships[i]))
#
# ##########
# # Saving transformed starship documents to a pickle file
#
# with open('transformed_list.pkl', 'wb') as f:
#     pickle.dump(transformed_dicts, f)

### UNCOMMENT ABOVE AND COMMENT BELOW TO INITIATE

with open('transformed_list.pkl', 'rb') as f:
    transformed_dicts = pickle.load(f)

#print(full_starships[4])
print(transformed_dicts[6])

client = pymongo.MongoClient()  # This automatically calls the default address of our connection
db = client["starwars"]

collection = db['starships']

for transformed_dict in transformed_dicts:
    collection.insert_one(transformed_dict)
# #
# # def mongo_id(dictionary)
#
# millennium_pilots = get_name(full_starships[4])
# print(millennium_pilots["Pilot Name"])
# for name in millennium_pilots["Pilot Name"]:
#     pilot_id = db.characters.find_one({"name": name}, {"_id": 1})
#     print(f"ObjectId({pilot_id['_id']})")
