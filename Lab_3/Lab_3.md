
# Лабораторная работа №3

*Водяный Михаил, РИ-440005*

## Задание
Разработать программу генерации симметричных ключей с помощью алгоритма Диффи-Хеллмана для расчётов применять алгоритм ускоренного возведения в степень.

## 1. Определение функций


```python
SHARED_PRIME = 7147351
SHARED_BASE = 1367
```

### 1.1. Функция ускоренного возведения в степень


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

### 1.2. Функции генерации симметричных ключей


```python
def first_step_dh(sharedBase, sharedPrime, myKey):
    return fast_pow(sharedBase, myKey) % sharedPrime

def second_step_dh(sharedPrime, myKey, hisRes):
    return fast_pow(hisRes, myKey) % sharedPrime
```


```python
aliceSecret = 13  # a
bobSecret = 37  # b
```


```python
# Alice Sends Bob A = g^a mod p
a1 = first_step_dh(SHARED_BASE, SHARED_PRIME, aliceSecret)

# Bob Sends Alice B = g^b mod p
b1 = first_step_dh(SHARED_BASE, SHARED_PRIME, bobSecret)

print('Шаг 1:\na1: {a1}, b1: {b1}'.format(a1 = a1, b1 =b1))

```

    Шаг 1:
    a1: 3232447, b1: 6353173
    


```python
# Alice Computes Shared Secret: s = B^a mod p
a2 = second_step_dh(SHARED_PRIME, aliceSecret, b1)

# Bob Computes Shared Secret: s = A^b mod p
b2 = second_step_dh(SHARED_PRIME, bobSecret, a1)

print('Шаг 2:\na2: {a2}, b2: {b2}'.format(a2 = a2, b2 =b2))
```

    Шаг 2:
    a2: 1680696, b2: 1680696
    


```python
if a2 == b2:
    print('Ключ:', a2)
else:
    print('Ошибка')
```

    Ключ: 1680696
    
