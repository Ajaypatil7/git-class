from pyjavaproperties import Properties
# input_stream=open("C:\\Users\\Admin\\PycharmProjects\\seleniumPro\\config.properties", 'r')
# prop=Properties()
#
# prop.load(input_stream)                    #STEPS:-
# print(prop.getProperty("USERNAME"))           #1> Open the file
# print(prop.getProperty("PASSWORD"))           #2> Create an object of Property class.
# print(prop.getProperty("URL"))                #3> Pass the file object to the property object
# input_stream.close()                          #4> Now by using the getProperty method we can access the Keys from the
#                                               #    config file.


#Writing the data into the file.
output_stream=open("C:\\Users\\Admin\\PycharmProjects\\seleniumPro\\config.properties", 'a')
prop=Properties()

prop.setProperty("fname1", "Aryan")
prop.setProperty("lname1", "patil")
prop.setProperty("email1", "aryanpatil@gmail.com")
prop.store(output_stream)
output_stream.close()