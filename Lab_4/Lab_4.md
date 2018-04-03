
# Лабораторная работа №4

*Водяный Михаил, РИ-440005*

## Задание
Разработать программу шифрования и дешифрования основанную на асимметричном алгоритме RSA. Разработанную программу для стандартных типов данных (unsigned __int64) расширить для целых чисел произвольной длины.

## 1. Описание алгоритма

1.      Выбираются два простых числа p и q.
2.      Вычисляется произведение p и q, которое называется модулем. N = p*q.
3.      Вычисляется значение функции Эйлера от числа n.
4.      Выбирается целое число e, взаимно простое со значением функции.
5.      Выбирается число d, удовлетворяющее условию e*d mod f(p,q)=1

Получаем {e,n} – открытый ключ шифрования, {d, n} – закрытый.

## 2. Определение функций

## 2.1. Математические функции


```python
def euclid(f, e):
    i = 0
    while(True):
        buf = i * f + 1
        if buf % e == 0:
            return int(buf / e)
        else:
            i += 1
```


```python
def euler(p, q):
    return (p-1)*(q-1)
```


```python
def fast_pow(value, power):
    if power == 0:
        return 1
    
    p = fast_pow(value, power // 2)
    p *= p
    if power % 2:
        p *= value
    return p
```

## 2.2. Функция шифрования


```python
def encode_RSA(word,e,N):
    ret = list()
    for v in word:
        n = ord(v)
        ret.append(int(fast_pow(n,e) % N))
    return ret
```

## 2.3. Функция дешифрования


```python
def decode_RSA(word,d,N):
    ret = list()
    for v in word:
        sim = fast_pow(v,d) % N
        ret.append(chr(sim))
    return ''.join(ret)
```

## 3. Определение констант и вычисление значений


```python
p = 3167
q = 2663
# p = 3557
# q = 2579
```

### 3.1. Вычисление модуля исходных чисел


```python
n = p * q  
print('n =', n)
```

    n = 8433721
    

### 3.2. Вычисление функции Эйлера


```python
f = euler(p, q)
print('f =', f)
```

    f = 8427892
    

## Вычисление закрытой экспоненты


```python
e = 13 # открытая экспонента
d = euclid(f, e) 
print(d)
```

    3241497
    

# 4. Тестирование

## 4.1. Шифрование


```python
text = u'May The Father of Understanding Guide Us'

encoded_text = encode_RSA(text, e, n)
print(l)
```

    [7700892, 3203811, 7016922]
    

## 4.2. Дешифрование


```python
decoded_text = decode_RSA(encoded_text, d, n)
print(decoded_text)
```

    May The Father of Understanding Guide Us
    

## 4.3. Проверка результатов на соответствие


```python
if text == decoded_text:
    print('Шифрование и дешифрование прошло успешно')
else:
    print('Ошибка')
```

    Шифрование и дешифрование прошло успешно
    
