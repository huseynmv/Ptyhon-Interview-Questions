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