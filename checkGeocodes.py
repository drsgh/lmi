import _gmAutocomplete
import _gmGeocode
import _containsPoint

#Runs full address -> geocode -> zone check process, putting results into "foundAddresses"

_gmAutocomplete
print("ADDRESS COMPLETION DONE")

_gmGeocode
print("ADDRESS GEOCODING DONE")

_containsPoint
print("ZONE CHECK DONE")