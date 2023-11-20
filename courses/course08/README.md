# Week08 - 2023-1119

### 本週目標
- [ ] [a038. 數字翻轉](https://zerojudge.tw/ShowProblem?problemid=a038)
  - [ ] `reverse()` 用法介紹
  - [ ] `join()` 用法介紹
- [ ] [j605. 1. 程式考試](https://zerojudge.tw/ShowProblem?problemid=j605)
  - [ ] `count()` 用法介紹
  - [ ] `index()` 用法介紹
- [ ] [c290. APCS 2017-0304-1秘密差](https://zerojudge.tw/ShowProblem?problemid=c290)
- [ ] [a149. 乘乘樂](https://zerojudge.tw/ShowProblem?problemid=a149)
- [ ] [a022. 迴文](https://zerojudge.tw/ShowProblem?problemid=a022)
  - [ ] `reverse()` 用法介紹
  - [ ] `copy()` 用法介紹
- [ ] [煲仔飯 (Clay Pot Rice)](https://tpmso.org/toi/wp-content/uploads/question/202310/ClayPotRice.pdf) [^1]
- [ ] [烤肉 (BBQ)](https://tpmso.org/toi/wp-content/uploads/question/202310/BBQ.pdf) [^1]
- [ ] [超市排隊 (Supermarket)](https://tpmso.org/toi/wp-content/uploads/question/202310/Supermarket.pdf) [^1]


### [a038. 數字翻轉](https://zerojudge.tw/ShowProblem?problemid=a038)

輸入任意數字，並將其數字全部倒轉

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 輸入一行包含一個整數，且不超過 $2^{31}$ | 輸出翻轉過後的數字 |
| # 1 | 12345 | 54321 |
| # 2 | 5050 | 505 |

#### Hint: 
- 前面有 0 的話應消除

#### [Python 解] (學校老師解)

```py
a = list(input())
a.reverse()
ans = ''.join(a)
print(int(ans))
```

#### [小實驗]
```py
# 本測試可發現若 list 結尾有 0，則 reverse 後會消失

a = ['1', '2', '3', '4', '0', '0']
a.reverse()
ans = ''.join(a)
print(int(ans))
# 4321

```py

# 我們也可以發現，若是字串，倒轉後 0 也會消失
b = '123400'
b = b[::-1]
print(int(b))
# 4321
```

### [j605. 1. 程式考試](https://zerojudge.tw/ShowProblem?problemid=j605)

給 n 個提交紀錄，第 i 個提交紀錄有兩個整數 ti 和 si 代表上傳時間和該次上傳的分數，若第 i 次的提交結果為嚴重錯誤，則 si 為 -1。  
計算總分的公式為提交紀錄中的最高分 - 總提交次數 - 總嚴重錯誤次數 * 2，若計算出來的分數為負數則計為 0。  
請輸出總分和第一次獲得最高分的時間點。

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 第一行有一個正整數 K (1 <= K <= 6) 代表提交的次數，接下來有 K 行，第 i 行有兩個整數 ti(1 <= ti <= 100) 和 si(1 <= si <= 100)。保證提交紀錄按照時間點嚴格遞增排序，並且第一個提交紀錄不會是嚴重錯誤。<br>(60 分): K = 3<br>(40 分): 無其他限制 | 輸出兩個整數，代表總分和第一次獲得最高分的時間點。 |
| # 1 | 5<br>3 89<br>5 -1<br>10 90<br>15 0<br>20 90 | 83 10 |
| # 2 | 3<br>3 0<br>5 -1<br>6 -1 | 0 3 |

#### [Python 解]
```py
n = int(input())
t = [0] * n
s = [0] * n

for i in range(n):
    x, y = map(int, input().split())
    t[i] = x
    s[i] = y

# 最高分 - 總提交次數 - 總嚴重錯誤次數 * 2
ans = max(s) - n - s.count(-1) * 2

# 若計算出來的分數為負數則計為 0。
if ans < 0:
    ans = 0

# 輸出總分和第一次獲得最高分的時間點。
print(ans, t[s.index(max(s))])
```

#### `[0] * n` 用法介紹

```py
# 創建一個長度為 5 的列表，並且每個元素都是 0
a = [0] * 5
print(a)
# [0, 0, 0, 0, 0]
```

#### `count()` 用法介紹
```py
# 計算 list 中有幾個 1
a = [1, 2, 3, 1, 1, 1]
print(a.count(1))
# 4
```

#### `index()` 用法介紹
```py
# 找出 list 中第一個 1 的位置
a = [1, 2, 3, 1, 1, 1]
print(a.index(1))
# 0
```

### [c290. APCS 2017-0304-1秘密差](https://zerojudge.tw/ShowProblem?problemid=c290)

#### 問題描述
將一個十進位正整數的奇數位數的和稱為A ，偶數位數的和稱為B，則A與B的絕對差值 |A －B| 稱為這個正整數的秘密差。  
例如： 263541 的奇數位和 A = 6+5+1 =12，偶數位的和 B = 2+3+4 = 9 ，所以 263541 的秘密差是 |12 －9|= 3 。  
給定一個 十進位正整數 X，請找出 X的秘密差。

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 輸入為一行含有一個十進位表示法的正整數X，之後是一個換行字元。 | 請輸出 X的秘密差 Y(以十進位表示法輸出 )，以換行字元結尾 。 |
| # 1 | 263541 | 3 |
| # 2 | 131 | 1 |

#### Hint ：
- （說明） 263541 的 A = 6+5+1= 12 , B = 2+3+4 =9 ，|A－B|=|12－9|= 3。
- （說明） 131 的 A = 1+1= 2, B = 3，|A－B|= |2－3|= 1。

#### 評分說明

輸入包含若干筆測試資料，每一的執行時間限制 (time limit)均為 1 秒，依正確通過測資筆數給分。其中：

- 第 1 子題組 20 分： X 一定恰好四位數 。
- 第 2 子題組 30 分： X 的位數不超過 9。
- 第 3 子題組 50 分： X 的位數不超過 1000 。

#### [Python 解]

利用字串長度判斷奇偶數，再分別加上 `even` 和 `odd`，最後算出 `even` 和 `odd` 的**絕對**差值。

```py
s = [int(x) for x in input()]

odd = even = 0

for i in range(len(s)):
    if i % 2 == 0:
        odd += s[i]
    else:
        even += s[i]

print(abs(odd - even))
```

### [a149. 乘乘樂](https://zerojudge.tw/ShowProblem?problemid=a149)

你拿到一個整數，卻忍不住想把每個位數都乘在一起。例如看到 356 就會想要知道 3 * 5 * 6 的值為何。快寫個程式幫幫為了乘數字而快發瘋的自己吧！

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 一開始有一個數字 T，表示共有幾組測試資料。<br>接下來有 T 個數字 n (0 <= n < 2147483648)。 | 輸出可以拯救自己的結果。 |
| # 1 | 3<br>356<br>123<br>9999 | 90<br>6<br>6561 |

#### [Python 解]
```py
n = int(input())

for i in range(n):
    m = int(input())

    if m == 0:
        ans = 0
    else:
        ans = 1
        while m:            # 當 m 不為 0 時，就會一直執行
            ans *= m % 10   # 得到個位數
            m //= 10        # 去掉個位數
    
    print(ans)
```

#### [Python 另解 1]

```py
n = int(input())

for i in range(n):
    num = [int(x) for x in list(input())]
    ans = 1

    for j in num:
        ans *= j
    
    print(ans)
```

#### [Python 另解 2]

```py
n = int(input())

for i in range(n):
    num = input()
    ans = 1

    for j in range(len(num)):
        digit = int(num[j])
        ans *= digit
    
    print(ans)
```

### [a022. 迴文](https://zerojudge.tw/ShowProblem?problemid=a022)

迴文的定義為正向，反向讀到的字串均相同  
如：abba , abcba ... 等就是迴文  
請判斷一個字串是否是一個迴文？

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 輸入資料共一行包含一個字串(長度 < 1000) | 針對每一行輸入字串輸出 yes or no |
| # 1 | abba | yes |
| # 2 | abcd | no |

#### [Python 解]
```py
a = input()

if a == a[::-1]:
    print('yes')
else:
    print('no')
```

#### [Python 另解]
```py
a = list(input())
b = a.copy()
b.reverse()

if a == b:
    print('yes')
else:
    print('no')
```

#### `reverse()` 用法介紹
```py
# 將 list 倒轉
a = [1, 2, 3, 4, 5]
a.reverse()
print(a)
# [5, 4, 3, 2, 1]
```

#### `copy()` 用法介紹
```py
# 將 list 複製一份
a = [1, 2, 3, 4, 5]
b = a.copy()
print(b)
# [1, 2, 3, 4, 5]
```

### [煲仔飯 (Clay Pot Rice)](https://tpmso.org/toi/wp-content/uploads/question/202310/ClayPotRice.pdf) [^1]

你突然超級想吃煲仔飯，但是煲仔飯動不動就要等個十幾二十分鐘，而你的午休時間十分短暫。你找到離學校最近的那家煲仔飯餐廳，搜到很多評論並推算出了你到餐廳後需要的等待時間，又根據你平時吃飯的速度推算出吃飯時間，當然你還得加上回來的時間。你想知道今天究竟有沒有辦法在午休時間內吃完飯回來工作。

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 第一列輸入五個正整數 T、G、W、E、B，其中 T 表示午休時長（1 ≤ 𝑇 ≤ 90），G 表示去程時長（1 ≤ 𝐺 ≤ 60），W 表示等待時間（1 ≤ 𝑊 ≤ 60），E 表示吃飯時間（1 ≤ 𝐸 ≤ 60），B 表示回程時長（1 ≤ 𝐵 ≤ 60）。 | 如果可以順利吃到飯，輸出所需總時長，否則輸出 -1。 |
| # 1 | 90 5 20 30 5 | 60 |
| # 2 | 60 15 30 10 15 | -1 |

#### [Python 解]

解題邏輯就是要判斷 T 是否足夠，若不足夠則輸出 -1，若足夠則輸出 G + W + E + B。

```py
T, G, W, E, B = map(int, input().split())

if T < G + W + E + B:
    print(-1)
else:
    print(G + W + E + B)
```

--- [本週上課內容分隔線] ---

---

### [烤肉 (BBQ)](https://tpmso.org/toi/wp-content/uploads/question/202310/BBQ.pdf) [^1]

阿榮是個大胃王，而他最喜歡吃的食物就是烤肉店的肉串了。每次大快朵頤後，他總是會忘記自己吃了多少串的豬肉和牛肉，只知道店家跟他收了 Ｎ 元，桌上有 Ｍ 串空竹籤。  
已知一串豬肉串 Ｘ 元，一串牛肉串 Ｙ 元，請你幫忙寫個程式計算他各吃了多少串豬肉串和牛肉串，還是店家算錯錢了。

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 輸入只有一列，共有四個數字 N、M (1 ≤ N, M ≤ 10000)、X 和 Y (1 ≤ X, Y ≤ 10，X ≠ Y)，任兩個數字中間以一個空格分開。 | 輸出兩個數字 A 和 B，表示吃了 A 串豬肉串和 B 串牛肉串，數字中間以一個空格分開。如果店家算錯錢，則輸出「-1 -1」。 |
| # 1 | 14 6 3 2 | 2 4 |
| # 2 | 101 11 1 10 | 1 10 |
| # 3 | 50 10 1 2 | -1 -1 |

#### [Python 解]
```py
N, M, X, Y = map(int, input().split())

# 初始化各類肉串的數量為 0
pork_count = 0
beef_count = 0

# 檢查每一種可能的情況，計算吃了多少串豬肉串和牛肉串
for i in range(N + 1):
    for j in range(M + 1):
        total_cost = i * X + j * Y
        if total_cost == N and (i + j) == M:
            pork_count = i
            beef_count = j
            break

# 判斷是否有解，並輸出結果
if pork_count + beef_count == M and (pork_count * X + beef_count * Y) == N:
    print(pork_count, beef_count)
else:
    print(-1, -1)
```

#### [補充] 延伸問題：雞兔同籠

雞跟兔子一共有 9 隻，雞的腳有 2 隻，兔子的腳有 4 隻，在總共有 30 隻腳的情況下，請問雞跟兔子各有幾隻？如果沒有解，請輸出 `No solution found.`
```py
find = False

for chicken in range(1, 10):
    rabbit = 9 - chicken  # 因為雞兔總數是9，所以兔子數量等於9減去雞的數量
    legs = chicken * 2 + rabbit * 4

    if (legs == 30 and rabbit > 0):
        find = True
        break

if find:
    print("Chicken: ", chicken)
    print("Rabbit: ", rabbit)
else:
    print("No solution found.")
```

### [超市排隊 (Supermarket)](https://tpmso.org/toi/wp-content/uploads/question/202310/Supermarket.pdf) [^1]

大黃工作的超市只有三個結帳櫃檯，每天都會出現大排長龍的場面。隊伍上方的攝影機會告訴你現在排隊的人數，以及他們籃子裡有多少商品要結帳。經過大黃一個禮拜的觀察，他發現了以下規律：
1. 每一個商品需要花 3 秒結帳。
2. 每兩個顧客之間會保持固定的距離，這段距離需走 2 秒。

舉例來說，假設某個櫃台的只有兩個人排隊，分別拿著 3 個和 5 個商品，那消化完該隊伍的時間是 3 x 3 + 2 + 3 x 5 = 26 秒。

請你撰寫一個程式，計算當前消化隊伍時間最短的櫃台編號以及所需時間。

| Sample | Input | Output |
| :------: | :--------: | :------: |
| 說明 | 第一列輸入三個數字 A、B 和 C (1 ≤ A, B, C ≤ 100)，分別表示 1、2 和 3 號櫃台的排隊人數。接下來三列分別有 A、B 和 C 個數字 Ki (1≤ Ki ≤ 500)，分別表示每位客人購買的商品數量。 | 輸出兩個數字 M 和 N，以一個空格分開，分別表示消化隊伍時間最短的櫃台編號以及所需時間。 |
| # 1 | 2 2 2<br>2 5<br>1 1<br>5 2 | 2 8 |
| # 2 | 3 2 2<br>1 1 1<br>5 5<br>4 6 | 1 13 |

#### [Python 解]
```py
times = []
for i in range(3):
    customers = list(map(int, input().split()))
    total_time = sum(customers) * 3 + (len(customers) - 1) * 2
    times.append(total_time)

min_time = min(times)
min_index = times.index(min_time) + 1

print(min_index, min_time)
```

<div align="center">
    <p>
        <a href="https://github.com/1chooo/23-fall-tutor/tree/main/courses/course07" target="_blank"><b>👨🏻‍💻 第七週課程</b></a> |
        <!-- <a href="https://github.com/1chooo/23-fall-tutor/tree/main/courses/course08" target="_blank"><b>👨🏻‍💻 第八週課程</b></a> -->
    </p>
</div>


## License

All of these teaching materials are owned by [Hugo ChunHo Lin](https://github.com/1chooo).   
These materials are intended for tutoring purposes. They are open-source to foster a more vibrant Python learning community. We warmly welcome fellow enthusiasts interested in Python to use them. If you use a substantial portion of the source code, please include a link back to this repository.

[^1]: [TOI推廣線上練習賽歷屆試題](https://tpmso.org/toi/index.php/tasks)
