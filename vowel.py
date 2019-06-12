r=['a','e','i','o','u']
t=['a','b','c','d','e','f','g','h','i','j','k','l','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','w','z']
o=input()
if o in t:
  if o in r:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")     
