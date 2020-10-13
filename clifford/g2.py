import clifford as cf

layout, blades = cf.Cl(2) # creates a 2-dimensional clifford algebra

e1 = blades['e1']
e2 = blades['e2']
e12 = blades['e12']

(e1^e2) - e12

abs((e1^e2) - e12)

2^e1^e2 - 7^e12

(2^e1^e2) - (7^e12)

