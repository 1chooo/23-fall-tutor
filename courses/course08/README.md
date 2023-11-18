# Week08 - 2023-1119

### 本週目標
- [ ] [a038. 數字翻轉](https://zerojudge.tw/ShowProblem?problemid=a038)
  - [ ] `reverse()` 用法介紹
  - [ ] `join()` 用法介紹
- [ ] [j605. 1. 程式考試](https://zerojudge.tw/ShowProblem?problemid=j605)
  - [ ] `count()` 用法介紹
  - [ ] `index()` 用法介紹
- [ ] [c290. APCS 2017-0304-1秘密差](https://zerojudge.tw/ShowProblem?problemid=c290)
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
- 第 2 子題組 30分： X 的位數不超過 9。
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

### [煲仔飯 (Clay Pot Rice)](https://tpmso.org/toi/wp-content/uploads/question/202310/ClayPotRice.pdf) [^1]

### [烤肉 (BBQ)](https://tpmso.org/toi/wp-content/uploads/question/202310/BBQ.pdf) [^1]

### [超市排隊 (Supermarket)](https://tpmso.org/toi/wp-content/uploads/question/202310/Supermarket.pdf) [^1]

### [d587. 參貳壹真好吃](https://zerojudge.tw/ShowProblem?problemid=d587)

### [a022. 迴文](https://zerojudge.tw/ShowProblem?problemid=a022)

### [e968. 2. 班級名單 (Student list)](https://zerojudge.tw/ShowProblem?problemid=e968)

### [c294. APCS-2016-1029-1三角形辨別](https://zerojudge.tw/ShowProblem?problemid=c294)

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
