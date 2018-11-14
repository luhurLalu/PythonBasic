from collections import deque
# stacking/tumpukan (first in last out)
data = [1, 2, 3, 4, 5]
print(data)
data.append(6)
print('data masuk :',6)
print(data)
data.append(7)
print('data masuk :',7)
print(data)

stack = data.pop()
print('data terakhir dihapus :',stack)
print(data)

print('='*100)
# queue/antrian (first in first out)
data1 = deque([1, 2, 3, 4, 5])
print ('data awal :',data1)

data1.appendleft(0)
print('data ditambahkan',0)
print(data1)

data1.append(6)
print('data ditambahkan',6)
print(data1)

queue = data1.popleft()
print('data pertama dihapus :',queue)
print(data1)
