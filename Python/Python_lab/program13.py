import pandas as pd
dataframe1=pd.DataFrame({"ID":["101","102","103","104","105","106"],"Name":["Ullas","Niahr","Prashid","Abhi","KArtik","Dhanush"]})
print(dataframe1)
dataframe2=pd.DataFrame({"Id":["201","202","203","204","205","206"],"Name":["Amogh","Thilak","Vinay","Sanjana","Chetana","Srikrank"]})
print(dataframe2)
frame=[dataframe1,dataframe2]
concat=pd.concat(frame)
print(concat)