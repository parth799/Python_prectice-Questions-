from xml.dom.pulldom import START_ELEMENT


parth={
    "pankha":"fan",
    "tel":"oil",
    "phone":"samrt phone"
}
print("options is:",parth.keys())
a=input("find you words name:")
#print("you word is:",parth[a])
print("you word is:",parth.get(a))
