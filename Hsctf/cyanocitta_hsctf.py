# Sage Script
# sols = f(x,y)=c[0]*x^2 + c[1]*y^2 + c[2]*x*y + c[3]*x + c[4]*y + c[5]
input_list = [(26, 66, 70314326037540683861066), (175, 242, 1467209789992686137450970), (216, 202, 1514632596049937965560228), (13, 227, 485439858137512552888191), (1, 114, 112952835698501736253972), (190, 122, 874047085530701865939630), (135, 12, 230058131262420942645110), (229, 220, 1743661951353629717753164), (193, 81, 704858158272534244116883)]
xs = []
ys = []
sols = []
for i in input_list:
    xs.append(i[0])
    ys.append(i[1])
    sols.append(i[2])

tempA = []
tempB = []
for i in range(len(xs)):
    tempA.append([pow(xs[i],2),pow(ys[i],2),xs[i]*ys[i],xs[i],ys[i],1])
    tempB.append([sols[i]])
A = matrix(tempA)
B = matrix(tempB)
C = A.solve_right(B)
a = 886191939093
b = 589140258545
fab = C[0]*pow(a,2) + C[1]*pow(b,2) + C[2]*a*b + C[3]* a + C[4] *b+ C[5]
ct = 19440293474977244702108989804811578372332250
fab = int(fab[0])
flag = ct^^fab
flag = hex(flag)[2:]
print(bytes.fromhex(flag))
