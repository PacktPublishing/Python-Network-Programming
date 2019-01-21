countryname=input("Enter country name:")
countryname=countryname.lower()
lastcharacter=countryname.strip()[-1]
if 'a' in lastcharacter:
    print ("Vowel found")
elif 'e' in lastcharacter:
    print ("Vowel found")
elif 'i' in lastcharacter:
    print ("Vowel found")
elif 'o' in lastcharacter:
    print ("Vowel found")
elif 'u' in lastcharacter:
    print ("Vowel found")
else:
    print ("No vowel found")
