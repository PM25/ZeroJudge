#%%
import sys

for line in sys.stdin:
    for cc in line:
      a=ord(cc)-7
      print(chr(a), end='')
    print()

      
      





# %%
