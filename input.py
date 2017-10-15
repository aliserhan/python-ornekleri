name = input("İsmin ne? -> ")#input kullanıcıdan giriş bekler 

print("Hosgeldin",name)#print ekrana yazıyı basıtırır
age=input("Senin yasin? -> ")#girilen inputu age ye atama yaptık
year=input("bulundugun yil? -> ")
brithdate=int(year)-int(age)#age yi ve yearı int e çevirdik 
print(name,brithdate,"yilinda dogdu")
