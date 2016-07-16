 # from http://www.yiibai.com/python/python3-webbug-series2.html
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry 入队
queue.append("Graham")          # Graham 入队
queue.popleft()                 # 队首元素出队
#输出: 'Eric'
queue.popleft()                 # 队首元素出队
#输出: 'John'
queue                           # 队列中剩下的元素
#输出: deque(['Michael', 'Terry', 'Graham'])
