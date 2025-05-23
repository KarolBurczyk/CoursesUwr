import time
a = time.time()
res = time.localtime(a)
print(res.tm_hour)
print(res.tm_min)
print(res.tm_sec)

