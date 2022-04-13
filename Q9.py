dict={"p":[
    {'n':'t','price':23},
    {'n':'T','price':525},
    {'n':'j','price':999},
    {'n':'h','price':299},
    {'n':'TV','price':49999},
    {'n':'5S','price':11}
    ]}
val=dict['p']
max=0
min=val[0]['price']
for i in val:
    for key in i:
        if key=='price':
            if i[key]>max:
                max=i[key]
            if i[key]<min:
                min=i[key]
print(max)
print(min)      
# here we fid maximum and minimum   

           
dict={"p":[
    {'n':'t','price':23},
    {'n':'T','price':525},
    {'n':'j','price':999},
    {'n':'h','price':299},
    {'n':'TV','price':49999},
    {'n':'5S','price':11}
    ]}
def get_my_key(val):
      return val['price']
my_list = dict["p"]
my_list.sort(key=get_my_key)
print(my_list)
# here i did sorting