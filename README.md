# 🍲 eat(); 🛌🏼sleep(); 👩🏼‍💻code(); 🔁repeat();

> place where aspiring developers **_grow_**  
>  and inspiring people **share**

## Popular interview questions level easy

-   Ceasar Cypher Encryptor

![Ceasar Cypher Encryptor](https://gkaccess.com/wp-content/uploads/2020/01/Caesar_Cipher_GateKeeper_security_compliance_proximity_authentication_2fa_mfa-768x803.jpg)

### Video explanation
[![](https://markdown-videos-api.jorgenkh.no/youtube/JEsUlx0Ps9k)](https://www.youtube.com/watch?v=JEsUlx0Ps9k)

```python
def caesar_cipher_encryptor(string, key):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters = []
    newStr = ''
    keyMod = key % 26
    for letter in string:
        newCharKey = alphabet.index(letter) + keyMod
        newChar = alphabet[newCharKey] if newCharKey <= 25
        else alphabet[0 + newCharKey % 26]
        letters.append(newChar)
        return newStr.join(letters)
```

---

-   Binary Search

![Binary Search Image](https://www.freecodecamp.org/news/content/images/size/w1000/2023/07/image-65.png)

### Video explanation
[![](https://markdown-videos-api.jorgenkh.no/youtube/7nbatZEehyo)](https://www.youtube.com/watch?v=7nbatZEehyo)

```python
def rec_binary_search(array, target, start, end):
    if start > end:
        return -1
    middle = start + end //2
    if target == array[middle]:
        return middle   //
    elif target < array[middle]:
        return rec_binary_search(array, target, start, middle -1)
    else:
        return rec_binary_search(array, target, middle + 1, end)
```

```python
def recursive_binary_search(array, target):
    return rec_binary_search(array, target, 0, len(array) - 1)
```

---

-   Two Number Sum

![Two Numbers Sum Image](https://miro.medium.com/v2/resize:fit:720/format:webp/0*kzet3Y1ff07dH1g7.png)


### Video explanation
[![](https://markdown-videos-api.jorgenkh.no/youtube/n2OMYeZhCgI)](https://www.youtube.com/watch?v=n2OMYeZhCgI)

```python
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        curSum = array[left] + array[right]
        if curSum == targetSum:
            return [array[left], array[right]]
        elif curSum > targetSum:
            right -= 1
        elif curSum < targetSum:
            left += 1
    return []
```

---

## Places to start your coding journey for free:

1. [FreeCodeCamp](https://www.freecodecamp.org/)
2. [Codecademy](https://www.codecademy.com/)
3. [Odin Project](https://www.theodinproject.com/)
4. [Harvard CS50](https://pll.harvard.edu/course/cs50-introduction-computer-science)

---

## Places to practice your algorithms and data structures:

-   [Leetcode](https://leetcode.com/)
-   [Codewars](https://www.codewars.com/)
-   [Hackerrank](https://www.hackerrank.com/)
-   [Coderpad](https://coderpad.io/)

---

## Contact

Follow for more:

[Email Me](mailto:k.stopczynska@gmail.com) [LinkedIn](https://www.linkedin.com/in/klaudia-stopczynska/) [Github](https://github.com/k-stopczynska)

## Hey there, I am Kseniia! 
### My hobby:
* :volleyball: Volleyball
* :walking_woman: Hiking
* :mount_fuji: Anime
* :potted_plant: House Plant

---

#### Favorite quote:
> “Anyone who stops learning is old, whether at twenty or eighty. Anyone who keeps learning stays young.”
> 
![alt text](https://www.mindset2millions.com/wp-content/uploads/2020/12/Anyone-who-stops-learning-is-old-whether-at-twenty-or-eighty.-Anyone-who-keeps-learning-stays-young-Henry-Ford.png "Henry Ford quote")
