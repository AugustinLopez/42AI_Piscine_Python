from sys import argv
from time import sleep
from loading import ft_progress

if len(argv) == 2:
  x = range(int(argv[1]))
elif len(argv) == 3:
  x = range(int(argv[1]), int(argv[2]))
else:
  x = range(int(argv[1]), int(argv[2]), int(argv[3]))
ret = 0
for elem in ft_progress(x):
  ret += elem
  sleep(0.01)
print()
print(ret)