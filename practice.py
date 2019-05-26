# #practice file
# user_name = input("Enter your username ")
# print( "User Name is " + user_name)
# # print("User Name is Umair " )

# list work

employ_list = ['umair','ammar','affan','atta','ramsha',5,3.6]
# print("Employ name is " +str(employ_list[6]))
print(employ_list[6])

employ_det = ['Umair',22,'karachi']
print("Employ name is " +employ_det[0] +" Employ age is " +str(employ_det[1])+ " Employ city is "+ employ_det[2])
employ_det.append('Pakistan')
print(employ_det)
# employ_det[10]='Lahore'
print(employ_det)
employ_det.insert(1,'Shehzad')
print(employ_det)
employ_det.pop()
print(employ_det)
del employ_det[2]
print(employ_det)
employ_det.remove('Shehzad')
print(employ_det)
city = employ_det.pop(0)
print(city)