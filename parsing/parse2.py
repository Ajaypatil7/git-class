import pickle

fobj= open("C:\\Users\\Admin\\Desktop\\file2.pkl", "rb")

data=pickle.load(fobj)
print(data)