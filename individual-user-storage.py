import arcgis
from arcgis.gis import GIS
from getpass import getpass

# Log into Portal/arcgis.com
uName = input("Username: ")
pwd = getpass("Password: ")
_gis = GIS("https://ess.maps.arcgis.com/home/index.html", username=uName, password=pwd)

# Accounts is a list of all user objects that you can query
Accounts = _gis.users.search(query= None, max_users =500)
# For each user in the org, give me a list of the items they own
for user in Accounts:
    storage = 0
    userItems = user.items(max_items=100) # The max_items default is 100
    if userItems: # Checks to see if the user owns items
        for item in userItems:
            # Adds up the total storage of all items the user owns, in bytes
            storage += item.size
    print (user.username + " is using {0} bytes of storage".format(storage))