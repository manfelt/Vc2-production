#Fil for alle provinsenes verdier.
#Klasse som definerer verdiene utifra en gitt liste
class province:
	def __init__(self, TAG, size, terrain, pop):
		self.TAG = TAG
		self.size = size
		self.terrain = terrain
		self.pop = pop

#Eksempel paa variablene programet skal behandle
London = province("LON", 3, 2, 8173941)
Berlin = province("BER", 3, 2, 6004857)
Trondheim = province("TRO", 1, 1, 178021)




debug_p = str("%TAG")

# print Trondheim.TAG, Trondheim.size, Trondheim.terrain, Trondheim.pop


samling = {}