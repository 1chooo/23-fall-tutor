# 使用 Python List 賦值時要小心


以下是個 python 的小實驗我們先定義一個 `a` list 並且存放 `1, 2, 3`，接著我們把定義一個 `b` list 存放 `a` 的內容，並且透過 `b = a` 的方式，由以下程式碼實現

```py
a = [1, 2, 3]
b = a

print("a:", a)  # a: [1, 2, 3]
print("b:", b)  # b: [1, 2, 3]
```

接著我們只修改 `a` list 的第一個元素，將第一個元素改為 `5` 照一般理解來說，應該只有 `a` list 會被修改才對，可是我們將 `b` list print 出來會發現 `b` list 也一起被修改了。

```py
a[0] = 5

print("a:", a)  # a: [5, 2, 3]
print("b:", b)  # b: [5, 2, 3]
```

到這邊大家一定覺得很奇怪，我明明只修改了 `a` list 的內容，並且先把 `a` list 的內容都存到 `b` list 了，就是不希望 `a` 改動了 `b` 也跟著改動，但是 `a, b` 兩個 list 的內容卻都一起更改了
