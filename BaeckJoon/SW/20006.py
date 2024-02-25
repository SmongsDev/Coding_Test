import sys; input = sys.stdin.readline
n, m = map(int,input().split())
room = []
for _ in range(n):
    lvl, nick = input().split()
    lvl = int(lvl)
    if not room:
        room.append((lvl,nick))
    else:
        for i in room:
            if i[0]-10 <= lvl <= i[0]+10:
                if len(room) != m:
                    i.append((lvl,nick))
                    break
        else:
            room.append((lvl,nick))
print(room)