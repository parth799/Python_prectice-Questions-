parth={
    "p": "my name is parth",
    'a': [1,2,3,4,5,6,7,8,9,0],
    "r": ["p","a","r",'t','h'],
    "t": {'parth': 'player'},
    "h": "my name is parth",
    1:2
}
print(parth['p'])
print(parth['a'])
print(parth['r'])
print(parth["t"]['parth'])
#parth['h']='i am parth'
print(parth["h"])
#print(type(parth.keys()))
#print(list(parth.keys()))
#print(parth.values())
#print(parth.item())
print(parth)
updatedict={
    'raj':"friend",
    "subham":"frinde",
    "h":"i am parth"
}
parth.update(updatedict)
print(parth)
print(parth.get("p"))
