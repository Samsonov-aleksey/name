a=7
m=4096

main_str="птиц ысодинаковымоперениемохотнолетаютвместетчк"

Y=[0]*32
Y[0]=502
for i in range(1,32):
    Y[i]=(a*Y[i-1])%m
    print(Y)

    gamma= ""
    for i in range(len(Y)):
    gamma += chr(Y[i]%26+97)
    print(gamma)