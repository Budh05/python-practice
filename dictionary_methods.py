a={"name":"harsh",
   "from":"india",
   "marks":[99,98,97]}
#! i) 
print("items")
print(a.items())

#! ii)
print("keys")
print(a.keys())

#! iii) 
print("update")
a.update({"neha":"india"})
print(a)

#! iv)
print("pop and assign val to new key country")
a["country"]=a.pop("from")
print(a)