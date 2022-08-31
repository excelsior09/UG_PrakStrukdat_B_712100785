print('Ini merupakan kalkulator sederhana!')

while True:
       angka = input("")
       n = angka.split( )
       angka1 = n[0]
       if angka == "Q":
              break
       angka2 = n[2]

       if n[1] == "+":
              print(int(angka1)+int(angka2))
       elif n[1] == "-":
              print(int(angka1)-int(angka2))
       elif n[1] == "*":
              print(int(angka1)*int(angka2))
       else:
              print(int(angka1)/int(angka2))
       