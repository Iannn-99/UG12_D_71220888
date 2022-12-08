print("~~~~~ Table Matematika Nich ~~~~~")
print("Pilihan Model Matematika")
a=print("1. Perkalian")
b=print("2. Pembagian")
modelmat=input("Masukkan model matematika yang diinginkan 1/2 : ")
tablemat=input("Menampilkan table matematika dari angka: ")

count=3
for j in range(1,11):
    while count ==3:
        j=count+1
    print(count,"x",j,"=",count*j)