import pickle

with open('links.txt', 'rb') as db:
	array = pickle.load(db)

print(array)
