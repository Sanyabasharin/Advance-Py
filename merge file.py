import pandas as pd
#данные по звонкам
data1=pd.read_csv('https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv', na_values="NA", skiprows=1, 
#decimal=",",
delimiter=";",
names=["ID","AdmArea","Year","global_id","Month","Calls","null"]
#, index_col="Year"
  )
data1=data1.set_index(["AdmArea","Year", "Month"])
data1=data1.loc["Центральный административный округ"]
print(data1.head())

#данные по безработице
data2=pd.read_csv('https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv', na_values="NA",
skiprows=1, 
delimiter=";",
names=["global_id","ID","Year","UnemployedMen","UnemployedWomen","UnemployedYoung","UnemployedDisabled","UnemployedTotal","Month","null"]
#, index_col="Year"
 )
data2=data2.set_index(["Year", "Month"])
print(data2.head())

data=pd.merge(data1, data2, left_index=True, right_index=True)
data=data.reset_index()
data=data.set_index("Calls")
data=data.sort_index()

print(data["UnemployedMen"][0:1])
#.head())
#print(data ["Calls"].mean().round(0))
