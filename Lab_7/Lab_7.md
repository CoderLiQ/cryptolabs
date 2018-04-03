
# Лабораторная работа №7

*Водяный Михаил, РИ-440005*

## Задание
Разработайте приложение которое разбивает файл из первой лабораторной работы на блоки длинной 1000 байт, затем в первом блоке M требуется рассчитать хеш основываясь на реализацию созданную в предыдущей работе.
Подберите такое значение Nonce, что бы hash(M + Nonce) начинался с 0 (старший бит). Учитывайте, что length(M + Nonce + hash(M + Nonce))=1024. Оцените время работы вашего приложения.


## 1. Определение функций


```python
def make_chunks(data,length): #функция для разделения исходных данных на блоки
    return [data[i:i+length] for i in range(0, len(data), length)]
```


```python
# Функция перевода хеш-значения в бинарный вид (для последующего нахождения хеша, старший бит 
# которого равен 0)

def get_bin_hash(hsh): 
    int_hsh=list(map(lambda x: int(x,16),hsh)) 
    bin_hsh="".join((map(lambda x: '{0:04b}'.format(x),int_hsh)))

    return bin_hsh
```


```python
import Lab_6

with open("a06.txt", "r") as file:
    message = file.read()

#Выделение блока в 1000 байтов

first_chunk=make_chunks(message,1000*8)[0] #получение первого блока

hsh= Lab_6.sha1(first_chunk) #Применение алгоритма sha1 из 6 ЛР

```


```python
import random

def get_nonce(message): #функция, перебором находящая значение nonce 
#(4 байта, т.к. Так как существует условие length(M + Nonce + 
#hash(M + Nonce))=1024 и длина сообщения и хеша равна, 
#соответственно, 1000 байт и 20 байт (160 бит)) такое, 
#чтобы старший бит хеша был равен 0

    while True:
        nonce = random.randint(0,9223372036854775807)
        new_hsh = Lab_6.sha1(message+str(nonce))
        new_bin_hsh = get_bin_hash(new_hsh)

        if new_bin_hsh[0] == '0':
            print('hash: ', new_bin_hsh)

            return nonce
    

```

## 2. Тестирование


```python
hsh
```




    '73b62e4389babcbdd3f44f7e88e3598ae4e662f4'




```python
get_nonce(hsh)
```

    hash:  0000110100011011000010100011100101110001110110001001110100101000110101101100010010001110100010100101100011111011001101011111111010001100000111101101100111101000
    




    7691666816729358163



## 3. Оценка времени работы лагоритма


```python
import timeit
print(timeit.timeit())
```

    0.008973414938623137
    
