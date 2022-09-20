# Nomor 1 
 
def sum_squares(a,b,c):
    return a**2 + b**2 + c**2
a,b,c = [1,2,3]
Hasil = sum_squares(a,b,c)
 
print(Hasil)

#Nomor 2
def triangular(a):
    temp = 0
    for i in range(a):
        temp += a
        a -= 1
    return temp
print("Hasil triangular 5 = " + str(triangular(5)))

#Nomor 3
def pangkat (x,y):
    if y > 1 :
        return x*pangkat(x,y-1)
    return x
Hasil dari = x
print(pangkat(3,2))


#Nomor 4
def reverse(f) :
    str = ""
    for i in f :
        str = i + str
    return str
f = "rotator"
test = reverse(f)

print ("string awal : ",end = "")
print(f)

print(reverse(f))
if reverse(test) :
    print("True")
else :
    print("False")