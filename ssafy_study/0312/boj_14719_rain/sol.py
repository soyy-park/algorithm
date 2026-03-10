import sys
sys.stdin = open('input.txt')

H, W = map(int, input().split())
height = list(map(int, input().split()))

rain = 0
for h in range(H):
    for x in height:
        if x >= h:
            if flag != 'b':     # block
                rain += tmp
                tmp = 0
                flag = 'b'
        else:
            if flag == 'e':     # empty
                tmp += 1