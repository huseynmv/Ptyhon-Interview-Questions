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
