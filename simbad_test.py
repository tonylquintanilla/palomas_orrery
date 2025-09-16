from astroquery.simbad import Simbad
result = Simbad.query_object("Proxima Centauri")
print(result)