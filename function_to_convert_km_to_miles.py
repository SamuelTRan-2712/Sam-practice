def convert(miles):
    km = 1.6 * miles
    return km

r = int(input("Please enter the number to be converted to km: "))
k = convert(r)
print ("The result of the number in km is:" ,k)
