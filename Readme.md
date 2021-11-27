## Python interview questions


## 1. What is a method?

* Metod hər hansı bir x obyektinin daxilindəki funksiyaya deyilir. Həmin metodu x.funksiya kimi cağıra bilərik.

```py

class A: 
    def meth (self, arg): 
        return arg*2 + self.attribute

```

## 2. What is the statement that can be used in Python if a statement is required syntactically but the program requires no action?

* Kodumuzda syntax errorunun olmamasını istəyiriksə if else blokunda pass keywordündən istifadə edə bilərik.

```py

if a > 0:
    print("Hello")
else:
    pass

```

## 3. Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1] ?

* index olaraq -1 istifadə etdiyimiz zaman listin ən sonuncu obyektini alırıq 

```py 
a = [2, 33, 222, 14, 25]
print(a[-1])

25

```

## 4. Write a Python program to calculate the sum of a list of numbers.

* Listdəki ədədlərin cəmini tapmaq üçün sum() funksiyasından istifadə edə bilərik.

```py
a = [1,2,3,4,5,6,7,8,9,10]

print(sum(a))

55
```

## 5. What is a dictionary in Python?

* Pythonun built-in data tiplərindən biri də dictionarydir. Dictionary data tipində key və value sistemindən istifadə olunur. Key və value arasında one-to-one relationship mövcuddur.

```py

my_dict = {
    'Ad' : 'Huseyn',
    'Soyad' : 'Mammadov'
}

print(my_dict['Ad'])
```

## 6. How do you get a list of all the keys in a dictionary?

* Bunun üçün keys() funksiyasından istiffadə edilir.

```py

my_dict = {
    'Ad' : 'Huseyn',
    'Soyad' : 'Mammadov'
}

print(my_dict.keys())
```

## 7. How would you randomize the contents of a list in-place?

* Bunun üçün shuffle() funksiyasından istiffadə edilir. Öncəliklə bu funksiyanı import etmək lazımdır. İstifadəsi aşağıdakı kimidir.

```py

from random import shuffle

my_list = [1,2,3,5,6,88,54]

shuffle(my_list)

print(my_list)
```

## 8. Explain the //, %, and ** operators in Python.

// Bölünmə zamanı nəticənin integer hissəsini göstərir.

```py

7 // 2

3

Normal bölünmə zamanı cavab 3.5 olmalı idi.
```

** Operatoru ədədin qüvvətini almaq üçündür. a üstü b almaq üçün a**b yazma lazımdır.

```py

2**10

1024
```

% Operatoru qalıqlı bölünmədə qalığı görmək üçün istifadə edilir.

```py

13 % 7 

6
```

## 9. How can you declare multiple assignments in one statement?

Bu əməliyyatı 2 yanaşma ilə edə bilərik :

```py

a,b,c = 1,2,3

Burada a=1, b=2, c=3 qiymmətini alır.

a = b = c = 4

Burada isə hər 3 dəyişən 4 qiymətini alır.

```

## 10. What is a docstring?

* Docstring hər hansı bit funsiyanın və ya metodun daxilində yazılır. Və həmin funksiya/metodun nə etdiyini açıqlayır. Docstringlər 3 ədəd tək/cüt dırnaq arasında yazılır.

```py

def salam():
    """
    Bu funskiya ekrana salam yazısını çıxarır
    """
    print("salam")

salam()

```

Funksiyanın docstringini görmək üçün __doc__ atributu istifadə edilir.

```py

print (salam.__doc__)

```

## 11. With Python, how do you find out which directory you are currently in?

* Bunu tapmaq üçün getcwd() metodundan istifadə edilir. Öncəliklə os modulunu imoprt etməliyik.

```py

import os

os.getcwd()

'C:\Users\lifei\AppData\Local\Programs\Python\Python36-32'

```

Əlavə olaraq, chdir() metodu ilə bu direktoriyanı dəyişə də bilərik.

```py
os.chdir('C:\\Users\\lifei\\Desktop')
os.getcwd()

'C:\Users\lifei\Desktop'

```

## 12. How many arguments can the range() function take?

* range() funksiyası 3 ədəd arqument götürür. Bunlar start, stop və step arqumentləridir. Start hansı ədəddən başlayacağını, stop hansı ədədə qədər davam edəcəyini, step isə artım ədədini bildirir. Step 2 olsa ədədlər iki - iki artacaqdır.

```py

range(5)

Yalnız 1 arqument verdikdə, funksiya bu ədədi stop arqumenti olaraq qəbul edir. Bu halda step 1 olur.

range(0,6)

İki arqument verdikdə birinci rəqəm start arqumenti, ikinci rəqəm isə stop arqumenti olur. Bu halda step yenə 1-ə bərabərdir.

range(0,20,2)

Üç arqument verdikdə isə birinci rəqəm start arqumenti, ikinci rəqəm isə stop arqumenti, üçüncü rəqəm isə step arqumenti olur.

```

## 13. What is the global keyword?

* Global keywordü hansısa dəyişəni kodun istənilən yerində əlçatan etmək üçün istifadə edilir.

Misal üçün :

```py

 a=7
 def func():
    print(a)
    a+=1
    print(a)
```

Belə olan halda a is not defined erroru ilə qarşılaşacağıq. Erroru həll etmək üçün kodu aşağıdakı kimi dəyişməliyik :

```py

 a=7
 def func():
    global a
    print(a)
    a+=1
    print(a)
```

## 14. What functions or methods will you use to delete a file in Python?

* remove() və unlink() metodlarından istifadə edə bilərik.

```py

import os
os.remove('app.py')
```

Unlinkin istifadəsi isə aşağıdakı kimidir.

```py 

import os 
os.unlink("app.py")
```

## 15. How do I convert a number to a string?

* Pythonda ədədi stringə çevirmək üçün built-in funksiya olan str()-dən istifadə edirik. Hexadecimal və octal çevirmə üçün isə hex() və oct() funksiyasından istifadə edilir.

```py

a = 11

string = str(a)
```

## 16. What is Garbage Collection?

* Pythonda yaddaş tənzimləmək üçün proqramda istifadə edilməyən obyektləri avtomatik olaraq silir. Bu proses Garbage Collection adlanır. Garbage collection hər bir obyekt üçün reference count (referans sayı) sayır. Və reference count 0-a bərabır olduğu zaman həmin obyekti silir. Obyektin referans sayı bu obyekt yeni bir dəyişənə ötürüldüyü zaman və ya list, tuple, dictionary-də istifadə olunduğu zaman artır. Obyektin referansları yenidən təyin edildiyi zaman və ya dəyişdirildiyi zaman isə reference count azalır.

```py

a = 100  // <100> obyekti yaranır

b = a // <100>-ün reference count-u artır

c = b // <100>-ün reference count-u artır

d = [a] // <100>-ün reference count-u artır

b = 50 // <100>-ün reference count-u azalır

d[0] = 30 // <100>-ün reference count-u azalır

```


## 17. Explain the use "with" statement in python?

* Pythonda with ifadəsini fayllarla işləyərkən istifadə edirik. with ilə hansısa faylı açıb, faylın içindəki məlumatlarla müəyyən içlər görə bilərik. with ifadəsinin üstün cəhətlərindən biri faylı açdıqdan sonra həmin faylı bağlamağa ehtiyac duymamağımızdır. with özündən sonra gələn kod blokunu icra etdikdən sonra faylı avtomatik olaraq bağlayır.

```py

with open('test.txt', 'r') as test :

``` 

with-in istifadəsi zamanı muxtəlif metodlardan istifadə edə bilərik :

r - Read, faylı oxumaq üçün istifadə olunur. Fayl mövcud olmadığı zaman error verir.

w - Write, faylın üzərinə yazmaq üçün istifadə edilir, fayl mövcud deyilsə yaradır.

