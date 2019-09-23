Data = [1,4,9,16,25,36,49,64]

Subdata1 = Data[3]
Subdata2 = Data[-3]

Subdata3 = Data[2:4]
Subdata4 = Data[:4]

Data2 = [100,200,300,400,500,600,700,800]

Data3 = Data2 + Data

a = Data[:]
a[4] = 87

x = [Data, Data2]

y = x[1][3]

Data.append(30)

panjang_list = len(Data)


print(panjang_list)