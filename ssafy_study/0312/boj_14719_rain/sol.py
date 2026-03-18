import sys
sys.stdin = open('./input.txt')

H, W = map(int, input().split())
height = list(map(int, input().split()))

total = 0
for h in range(1, H+1):
    rain = 0
    start = 0  # End
    for x in height:
        # 블럭
        if x >= h:
            start = 1
            if rain:
                total += rain
                rain = 0
        # 비
        else:
            if start:
                rain += 1
<<<<<<< Updated upstream
print(total)
=======
print(total)
>>>>>>> Stashed changes
