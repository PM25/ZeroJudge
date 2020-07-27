#%%
import sys


def formatlist(factors):
    out = []
    for factor in sorted(set(factors)):
        x = factors.count(factor)
        if x > 1:
            out.append(str(factor) + "^" + str(x))
        elif x == 1:
            out.append(str(factor))

    return " * ".join(out)


# for line in sys.stdin:
for line in [input()]:
    num = int(line)
    pass
# %%
