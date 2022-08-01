import pickle

fobj= open("C:\\Users\\Admin\\Desktop\\file2.pkl", "wb")

data=[10,'python', 20.3]

pickle.dump(data, fobj)

print('Data is writen successfully')