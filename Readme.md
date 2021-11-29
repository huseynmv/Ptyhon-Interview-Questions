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


## 18. What is Monkey patching ?

* Hansısa classı və ya metodu sonradan dəyişmək prosesinə pythonda monkey patching deyilir. Bəzən böyük proyektlərdə işləyən zaman third-party bir kitabxananın bizin üçün əlverişli olmadığını görə bilirik. Bu zaman monkey patching istifadə edilə bilər.

## 19. What are negative indexes and why are they used?

* Pythonda listin indexi neqativ və pozitiv ola bilər. İndex pozitiv olduğu zaman 0 birinci index, 1 ikinci index olur və indexlər bu ardıcıllıqla davam edir. İndex neqativ olduqda isə -1 sondan birinci index, -2 sondan ikinci index olur və bu ardıcıllıqla davam edir. Neqativ index adətən listə yeni əlavə olunmuş obyekti silmək üçün və ya ən son əlavə olunmuş obyekti görmək üçün istifadə edilir.

## 20. Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1] ?

* Yuxarıdakı sualda qeyd etdiyimiz kimi -1 indexi listin daxilində sonuncu elementi təmsil edir. Bu halda bizim listimizdə sonuncu element 25 olduğu üçün, cavab 25 olacaqdır.

## 21. What is TkInter?

* Tkinter pythonun GUI (Graphical user interface) üçün istifadə olunun kitabxanasıdır. Ən çox desktop applicationlar yaratmaq üçün istifadə olunur.


## 22. What is slicing?

* Pythonda slice() funsiyasi list, tuple və dictionaryləri müəyyən hissəyə bölmək ("kəsmək") üçün istifadə olunur. Bu funksiya da range funksiyası kimi 3 arqument götürür. Start, stop və step.

```py

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])   // 'd', 'e'
```

## 23. Name the File-related modules in Python?

* Pythonda fayllar və fayl sistemi ilə işləmək mümkündür. Bundan istifadə edərək siz faylı silə, yenisini yaradabilə, faylı dəyişə bilə və ya silə bilərsiniz. 3 əsas modul istifadə edilir. os, os.path və shutil. os və os.path faylları "tutmaq üçün" istifadə edilir. shutil isə faylı kopyalamaq, silmək kimi işlər üçün istifadə olunur.


## 24. How to open a file c:\scores.txt for writing?

```py

file = open("c:\\scores.txt", "w")

```

## 25. What Are The Types of Objects Support in Python Language?

* Pythonda obyektin iki növü mövcuddur. Bunlar immutable(dəyişilə bilməyən) və mutable(dəyişə bilən) obyektlərdir. Bu iki tipin ən əsas fərqi, mutable obyektlərin konteninin dəyişkən, immutable obyektlərin kontentinin dəyişkən olmamasıdır.

    * İmmutable obyektlər : Built-in data tipləri olan int, float, boolean, string, tuple immutable obyektlərdir.
        
        ```py
        tuple1 = (0, 1, 2, 3) 
        tuple1[0] = 4
        print(tuple1)
        ```
    Tuple immutable olduğu üçün onun daxilindəki elementləri dəyişmək olmur. Error :
    
    File "c:\Users\Huseyn\Desktop\app.py", line 2, in <module>
    tuple1[0] = 4
    TypeError: 'tuple' object does not support item assignment

    ```py
        text = "Salam dunya"
        text[0] = 'A'
        print(text)
    ```
    String də immutable olduğu üçün aşağıdakı error ilə qarşılaşacağıq :

    TypeError: 'str' object does not support item assignment

* Mutable obyektlər : Bunlara list, dict, set aiddir.

    ```py
        adlar = ['Huseyn', 'Yusif', 'Ayten']
        adlar[0] = 'Rustam'
        print(adlar)
    ```
    List mutable olduğu üçün daxilindəki elementləri sonradan dəyişmək mümkündür. Yuxarıdakı kodun nəticəsi belə olacaqdır :
    ```py
        ['Rustam', 'Yusif', 'Ayten']
    ```

* P.s : Tuple immutable olduğu üçün daxilində mutable obyektlər daşıya bilər.

    ```py
    tuple1 = ([1,2,3], 'salam')
    ```

## 26. How do you create your own package in Python?

* İlk öncə package üçün direktoriya yaradırıq və ona packegimizin adını veririk.

* Daha sonra classları və lazım olacaq funksiyaları yazırıq

* Sonda isə __init__.py faylı yaradırıq.

Aşağıdakı nümunədə Cars package yaradacağıq.

Cars folderini yaratdıqdan sonra onun daxilindəki modulları yazmalıyıq. 

```py

    class Bmw:
        def __init__(self):
            self.models = ['x5', 'x3', 'm5', 'x6']

    class Mercedes:
        def __init__(self):
            self.models = ['c220', 's560', 'e320']
```

Bütün prosesləri etdikdən sonra növbə __init__ faylını yaratmağa gəlir. init faylını yaradarkən bu faylın Cars ilə eyni direktoriyada olmasına diqqət etməliyik. init faylının içini boş buraxa bilərik.

İndi isə yaratdığımız packagei ostifsdə edək. Bunun üçün eyni directoriyada app.py faylı yaradaq. app.py faylında yaratdığımız packagei istifadə etmək üçün daha öncə yaratdığımız classları import etməliyik.

```py
    from Cars import Bmw
    from cars import Mercedes

    new_car = Bmw()

```

## 27. Is Python object oriented? what is object oriented programming?

* Bəli, python obyekt yönümlü proqramlaşdırma dilidir. Obyekt yönümlü proqramlaşdırma (OOP) obyekt və classlardan istifadə edilən proqramlaşdırma paradiqmasıdır. OOP-nin 4 əsas prinsipi var. Bunlar inheritance, polymorphisms, encapsulation və abstractiondur. Məşhur OOP dilləri python, java, golang, c++ hesab edilir.

## 28. What is the output of the following?

```py

x = ['ab', 'cd']
print(len(map(list, x)))
```

Yuxarıdakı kod map funksiyasının uzunluğu olmadığına görə error verəcəkdir.

## 29. Explain help() and dir() functions in Python.

* help() funksiyasını hər hansı bir obyekt, metod və ya atribut üçün istifadə etdikdə həmin obyektin Python dokumentasiyasını bizə təqdim edir.

```py

help(len)

Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

```

* dir() funksiyası isə obyektin və ya classım atributlarını bizə göstərir.

```py
class Person:
  def __dir__(self):
    return ['age', 'name', 'salary']

p1 = Person()

print(dir(p1))

['age', 'name', 'salary']
```


## 30. What is the output of the following?

```py
x = ['ab', 'cd']
print(len(list(map(list, x))))
```
Yuxarıdakı kodu işlətdikdə list'də 2 element olduğu üçün len() metodunun köməyi ilə, list'in uzunluğunu, yəni 2 alacayıq.

## 31. Write a sorting algorithm for a numerical dataset in Python.

* Hanısa bir dataseti sıralamaq üçün pythonda sort() funksiyası istifadə edilir. 

```py
my_list = [1,2,3,7,5,10]

my_list.sort()

print(my_list)
```

Bu kodun nəticəsi [1,2,3,5,7,10] olacaqdır. sort() funksiyası kiçikdən böyüyə və ya əlifda sırası ilə (ascending order) sıralayır. Böyükdən kiçiyə və ya əlifba sırasının tərsinə sıralamaq üçün isə sort() funksiyasının daxilinə reverse=True parametri ötürməliyik.

```py

my_list = [1,2,3,7,5,10]

my_list.sort(reverse=True)

print(my_list)
```

Bu zaman nəticə [10,7,5,3,2,1] olacaqdır.


## 32. Explain join() and split() in Python.

* Bəzən kodumuzda müəyyən stringləri ayırmaq lazım gələcəkdir. String immutable tip olduğu üçün, bu zaman köməyimizə split() funksiyası gəlir. split() funksiyasının əsas məqsədi stringi bizim müəyyən edəcəyimiz dəyərə görə bölməkdir(substringlərə ayırmaq).

```py

a = 'salam dunya'

print(a.split('d'))
```

Yuxarıdakı kodda salam dunya sözünü d hərfinə ilə ayırırıq. Nəticə isə aşağıdakı kimi olacaqdır.

```py

['salam ', 'unya']
```

* join() metodu isə bizim təyin etdiyimiz simvol ilə iterable elementi birləşdirib bir string halına gətirir.

```py


list1 = ['1', '2', '3', '4']
 
print(', '.join(list1))

```

## 33. What is the pass statement in Python?

* Bəzən funksiya və ya metod yazarkən bu funksiyanın nə edəcəyinə ilk başda qərar verməyə bilərik. Lakin, funksiyanın yaddan çıxmaması üçün də onu qeyd etmək istəyirik. Əgər funksiyanın sadəcə adını yazıb dayansaq bu zaman errorla qarşılaşacağıq. Bu erroru önləmək üçün pass keywordündən və ya 3 nöqtədən ( ... ) istifadə edə bilərik.

```py

def A():
    pass
```
Və ya 

```py

def A():
    ...

```


## 34. How do you take input in Python?

* Pythonda userdən input almaq üçün built-in funksiya olan input()-dan istifadə edilir. input() userdən məlumatı alır, bu məlumatı hansısa bir dəyişənə bərabər edə bilirik. Yazılışı aşağıdakı kimidir. 

```py

ad = input('Adınızı daxil edin')
```

input götürdüyü məlumatı string formasında saxlayın. Bir məsələyə diqqət etməliyik. Misal üçün əgər istifadəçidən yaşını almaq istəyiriksə, bu zaman yaş bizə '21' kimi görünəcəkdir.(string formasında). Bu isə kodumuzun davamında bizə problem yarada bilər. Errordan qaçmaq üçün ən başda aldığımız inputu integerə çevirməliyik.

```py

yash = int(input('Yashinizi daxil edin'))

```

## 35. Mention five benefits of using Python?

1. Python high level proqramlaşdırma dili olduğu üçün(insan dilinə yaxın) oxuma, yazma və öyrənməsi yeni başlayanlar üçün digər dillərə görə daha asan hesab edilir.

2. Multi purpose dil olması. Pythonu müxtəlif məqsədlər üçün istifadə etmək olar. Desktop application, web development, data analitikası, süni intellekt və s.

3. Kitabxanalarının çox olması. Hesablamalar üçün Numpy, data analitika üçün Pandas və s.

4. Obyekt yönümlü olması. Pythonda demək olar ki, hər şey classlardan ibarətdir və bu bizi uzun kod yazmaqdan xilas edir.

5. Dinamik tipli dil olması. Hər dəfə data tipini yazmaq məcburiyyətində deyilik.


## 36. If you are ever stuck in an infinite loop, how will you break out of it?

* Sonsuz dövrdən çıxmaq üçün klaviaturada ctrl və c düymələrini birlikdə sıxırıq. 

```py

while True:
  
  print('salam')
```

Sonsuz dövr olduğunu görüb ctrl + c sıxırıq. 
```py
salam
salam
salam
salam
.
.
.
.
.
.

Traceback (most recent call last):
  File "c:\UsersHuseyn\Desktop\app.py", line 2, in <module>
    print('salam')
KeyboardInterrupt
```


## 37. When would you use a break statement in a for loop?

* Hər hansı bir loopa girdikdə, istədiyimizi aldıqdan sonra döngünün dayanmasını istəyiriksə break-dən istifadə edirik.

## 38.  How would you declare a comment in Python?

* Pythonda comment # simvolu ilə yazılır.

```py

# BU bir commentdir

```

## 39. Which methods/functions do we use to determine the type of instance and inheritance?

* Bunun üçün biz 3 funsiya/metotdan istifadə edə bilərik. Bunlar type(), isinstance() və issubclass()-dır.

type() - parametr kimi daxil etdiyimiz obyektin tipini bizə qaytarır.

```py

type(3)

<class 'int'>

```

isinstance() - 2 parametr götürür. Bunlar value(dəyər) və tipdir(type). Daxil etdiyimiz valuenin tipi bizim daxil etdiyimiz tipdirsə, funksiya bizə True cavabını verir. Əgər belə deyilsə False qaytarır.

```py

isinstance(3,int)

True

isinstance((1),tuple)

False

```

issubclas() - arqument olaraq iki class qıbul edir. Bizinci class ikincidən miras alırsa(inheritance) funksiya bizə True cavabını verir, əks halda cavab False olur.

```py

class A: 
    pass

class B(A):
    pass

issubclass(B,A)

True

issubclass(A,B)

False

```


## 40. How would you convert a string into an int in Python?

* Pythonda string data tipini integer data tipinə çevirmək üçün int funksiyasını istifadə edirik.

```py

int('111')

111

```

'111' - in tipinə baxsaq cavab string olacaqdır.
```py

type('111')

<class 'str'>

```


Çevirmə etdikdən sonra bu datanın classına baxsaq cavab aşağıdakı kimi olacaqdır.

```py

type(int('111'))

<class 'int'>

```


## 41. What are assignment operators in Python?

* Bu operatorları nümunələrlə daha yaxşı başa düşmək olar.

'+' operatoru 

```py
a = 5

b = a + 1

print(b)

6


```

'-' oeratoru

```py

c = 10

c -= 1

print(c)

9

```

'*' operatoru

```py

d = 10

d*2

print(d)

20

```

'/' operatoru

```py

b = 20 

b / 2

print(b)

10

```

'%' opertoru qalığlı bölmə zamanı alınan qalığı göstərir

```py

a = 7%2

print(a)

1

```

'**' qüvvətə yüksəltmək üçün istifadə edilir.

```py

a = 10**2

print(a)

100

```

## 42. What are membership, operators?

* Pythonda membership operatorları in və not in dir. Bu operatorlar hər hansı bir textdə bizim istəyimiz bir şeyin olub olmadığını yoxlamaq üçündür. Nümumə kod :

```py

if 's' in 'something':
    print(True)

True

if 'x' is not 'something':
    print(False)

False

```

## 43. Is Python case-sensitive?

* Bəli python case sensitive bir dildir. Misal üçün bir dəyişənin adını kiçik hətflə təyin etmişiksə, daha sonra həmin dəyişəni olduğu kimi çağırmalıyıq. Əgər fərqi cür çağırsaq aşağıdakı kimi error ilə qarşılaşacağıq.

```py

ad = 'Huseyn'

print(AD)

NameError: name 'AD' is not defined

```

## 44. What is the concatenation?

* Concetanation hərfi tərcümədə birləşmə deməkdir. Pythonda concatenation stringləri, listləri birləşdirmək üçün istifadə olunur. Nümunə :

```py

'10' + '10'

'1010'

```

Unutmayaq ki, fərqli data tiplərini bir bir ilə birləşdirə bilmərik. Belə olan halda error ilə qarşılaşacağıq.

```py

3 + '3'

TypeError: unsupported operand type(s) for +: 'int' and 'str'

```

## 45. Use a for loop and illustrate how you would define and print the characters in a string out, one per line.

* Bunu etmək üçün ilk öncə stringi loopa salmaq lazımdır. Aşağıdakı nümunədəki kimi edə bilərik.

```py

text = 'Salam dunya'

for i in text :
    print(i)

S
a
l
a
m

d
u
n
y
a

```

Yuxarı koddakı i textimizdəki hər bir xarakteri təmsil edir.



## 46. 

* Inheritance hərfi tərcümədə miras mənasını verir. Pythonda inheritance bir classın bütün xüsusiyyətlərini başqa bir classa miras verilməsi, ötürülməsi deməkdir. İnheritance istifadə etdiyimiz zaman adətən, yeni yaranan classa derived class, miras alınan classa isə base class deyilir. İnheritanceın ən üstün cəhətlərindən biri bizi əlavə kodlar yazmaqdan xilas etməsidir. Belə ki, eyni xüsusiyyətlərə malik çoxlu class yaratmaq əvəzinə, bir class yaradıb digər classları isə ondan inherit edə bilərik. İnheritance istifadə etdiyimiz zaman yeni yaranan classa yeni metodlar da əlavə edə bilərik. 

* İnheritanceın müxtəlif növləri mövcuddur. 

1. Single inheritance - classın yalnın 1 classdan miras almasıdır.

2. Multiple Inheritance - classın iki və daha atrıq classdan miras almasıdır.

3. Multilevel Inheritance - Bu zaman B classı A classından inheritance alır, C classı isə B classından.

4. Hierarchical İnheritance - Bir base classdan müxtəlif sayda classın miras almasıdır.



## 47. Explain split(), sub(), subn() methods of re module in Python.


split() - bu method regex pattern'ə uygun olaraq verilmiş şərtə görə stringi bölür

sub() - bu methodda 2 parametr verilir, biri textdə dəyişmək istədiyiniz hissədir. Digəri isə dəyişmək istədiyiniz hissəyə nə qoymaq istəyirsiz.

subn() - bu method da eyni sub methodu kimi işləyir, eyni zamanda nə qədər dəyişiklik edibsə onun sayın da göstərir.


## 48. What is tuple unpacking?

```py

a = ('Huseyn', 'Mammadov', 21)

```

Yuxarıdakı nümunədə a dəyişəninə tupledakı məlumatları mənimsədirik. Bu prosess packing adlanır.

```

ad, soyad, yas = a

```

Bu kodda isə ad, soyad, yas dəyişənlərinə müvafiq olaraq tupledakı məlumatları mənimsədirik. Bu proses isə unoacking adlanır.

```py

print(ad)

print(soyad)

print(yas)

```

Nəticələr aşağıdakı kimi olacaqdır.

```py

Huseyn

Mammadov

21

```


## 49. Which of the following is an invalid statement?

a) abc = 1,000,000
b) a b c = 1000 2000 3000
c) a,b,c = 1000, 2000, 3000
d) a_b_c = 1,000,000 

* a variantında abc tuple təyin edilib. abc = (1, 000, 000) kim düşünə bilərik. Burda səhvlik yoxdur.

* c variantında hər üç dəyişənə müxtəlif dəyərlər təyin edilib. a = 1000 b = 2000 c = 3000 kimi düşünə bilərik. Burda da səhvlik yoxdur.

* d variantında eyni ilə a variantındaki proses baş verir.

* b variantında isə dəyişənlər arasında boşluq olduğu üçün errorla qarşılaşacağıq.

Cavab b


