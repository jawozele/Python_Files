#A dictionary with all iPhone releases which include year of releases

released = {
  "iPhone": 2007,
  "iPhone 3G": 2008,
  "iPhone 3GS": 2009,
  "iPhone 4": 2010,
  "iPhone 4S": 2011,
  "iPhone 5": 2012,
  "iPhone 5C": 2013,
  "iPhone 5S": 2013,
  "iPhone 6 / 6 Plus": 2014,
  "iPhone 6S / 6S": 2015,
  "iPhone SE": 2016,
  "iPhone 7 / 7": 2016,
  "iPhone 8 / 8": 2017,
  "iPhone X": 2017,
  "iPhone XS / XS": 2018,
  "iPhone XR": 2018

}
released["iPhone 10"] = 2013

print(released)

del released['iPhone']
print(released)

print(len(released))

for item in released:
  if "iPhone 5" in released:
  print("Key Found")
break
else :
  print("No Keys Found")
print(released.get("iPhone 3G", "none"))

print("_" * 10)
print("These are iPhone releases, so far!")
print("_" * 10)
for release in released:
  print(release)

phones = released.keys()
print("phones")

print("This dictionary contains these keys:")