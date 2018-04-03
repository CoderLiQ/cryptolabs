
# coding: utf-8

# # Лабораторная работа №6
# 
# *Водяный Михаил, РИ-440005*

# ## Задание
# Реализуйте один из трёх алгоритмов криптографического хеширования (0 - sha1, 1 - md5, 2 - ГОСТ Р 34.11-94) в зависимости от остатка при делении номера варианта в поле GF(3).
# 
# Вариант 0.

# ## 1. Определение функций

# ### 1.1. Перевод текста в биты

# In[14]:


def text_to_bits(text):
    textBytes = bytearray(text, 'ascii')
    textBits  = [format(byte, '08b') for byte in textBytes]
    return ''.join(textBits)


# ### 1.2. Дополнение битов 

# In[21]:


def bits_addition(bitsString, textLength):
    
    zeros = (448 - (8 * textLength + 1)) % 512
    padBits = '1' + ('0' * zeros + format(textLength * 8, '064b'))
    
    textPadded = bitsString + padBits
    try:
        assert(len(textPadded) % 512 == 0)
    except:
        print('Error')
    return textPadded


# In[16]:


def k_const(t):
    if t <= 19:
        return 0x5a827999
    elif t <= 39:
        return 0x6ed9eba1
    elif t <= 59:
        return 0x8f1bbcdc
    else:
        return 0xca62c1d6


# ### 1.3. Логические функции

# In[17]:


def ROTL(x, n, w):
    return((x << n & (2 ** w - 1)) | (x >> w - n))


# In[18]:


def Ch(x, y, z):
    return((x & y) ^ (~x & z))

def Parity(x, y, z):
    return(x ^ y ^ z)

def Maj(x, y, z):
    return((x & y) ^ (x & z) ^ (y & z))


# ### 1.4. Основная функция

# In[19]:


def sha1(text):

    # Предварительная обработка
    textBits = text_to_bits(text)  # Перевод текста в биты
    textPadded = bits_addition(textBits, len(text))  # Добавление битов до 512
       
    # Инициализация переменных
    H = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0]

    # Количество итераций
    N = int(len(textPadded) / 512)
   
    # Основной цикл
    for i in range(1, N + 1):
        
        W = list()
        
        # Разбиваем сообщение на сообщение меньше размером 512
        start = (i-1) * 512
        finish = start + 512
        M1 = textPadded[start:finish]
        
        # Блок сообщения преобразуется из 16 32-битовых слов в 80 32-битовых слов
        for t in range(80):
            if t <= 15:
                W.extend([ int(M1[ (32 * t) : (32 * (t + 1)) ], 2)  ])
            else:
                W.extend([ ROTL( W[t - 3] ^ W[t - 8] ^ W[t - 14] ^ W[t - 16], n=1, w=32) ])
   
        a, b, c, d, e = H[0], H[1], H[2], H[3], H[4]
        
        # В зависимости от индекса используем разные функции
        for t in range(80):
            if t <= 19:
                f = Ch(b, c, d)
            elif t <= 39:
                f = Parity(b, c, d)
            elif t <= 59:
                f = Maj(b, c, d)
            else:
                f = Parity(b, c, d)

            temp = (ROTL(a, n=5, w=32) + f + e + k_const(t) + W[t]) % (2 ** 32)

            e, d, c, b, a = d, c, ROTL(b, n=30, w=32), a, temp

        # Добавляем хеш-значение к результату
        for index, i in enumerate((a, b, c, d, e)):
            H[index] = (i + H[index]) % (2 ** 32)
    
    # Форматирование
    H = [format(x, '08x') for x in H]

    return("".join(H))


# ## 2. Тестирование

# In[20]:


result = sha1('The quick brown fox jumps over the lazy dog')
print(result)
assert('2fd4e1c67a2d28fced849ee1bb76e7391b93eb12' == result)

