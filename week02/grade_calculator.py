#İlk başta notları toplayacağım ve kişi sayısını tutmak içi variable yap sıfırdan başlat
toplam_not=0
student_num=0
#sürekli isim için sonsuz döngü
while True:
  #kullanıcan isim al eğer "e" veya "E" yazarsa çık
  ad = input("Enter your name or press e to exit: ")
  if ad.lower()== "e":
    break#koddan çıkıp alttaki if'e götür
  notes=float(input("Enter your note:"))#belki ondalık girerler diye float yaptım
  if notes<0 or notes>100:
    #eğer 0 dan kucuk veya 100 den buyuk olursa diye continue ile başa dondur
    print("invalid note")
    continue
  #hatalı nottan çıkan notları burada süzerek yerine koy ve f stringle kullanıcıya göster ve harf notunu ver
  if notes >= 90:
    print(f"{ad} : {notes}  A")
  elif notes >= 80 :
    print(f"{ad} : {notes} B")
  elif notes >=70 :
   print(f"{ad} : {notes}  C")
  elif notes >=60:
   print(f"{ad} : {notes}  D")
  elif notes >=0:
   print(f"{ad} : {notes}  F")
#harf notundan sonra notları toplam nota ekle ve kişi sayısını bir arttır
  toplam_not=toplam_not+notes
  student_num=student_num+1
#0/0 hatasından kurtulmak için bir if statement koydum
if student_num>0:
#toplam puanı toplam kişi sayısına bölerek aver buldum ve ekrana yazdırdım
  aver=toplam_not/student_num
  print(f"Total students:{student_num}")
  print(f"Average note:{aver}")
else:
  print("No students entered.")
