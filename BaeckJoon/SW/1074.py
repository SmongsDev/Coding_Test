import sys; input = sys.stdin.readline
n,r,c = map(int,input().split())

def recur(size, x, y, offset):
    div_size = size//2
    if size == 1:
        return offset
    
    if x <= r < x + div_size and y <= c < y + div_size:
        return recur(div_size, x, y, offset)
    
    elif x <= r < x + div_size and y + div_size <= c < y + size:
        return recur(div_size, x, y + div_size, offset + (div_size) * (div_size))
    
    elif x + div_size <= r < x + size and y <= c < y + div_size:
        return recur(div_size, x + div_size, y, offset + (div_size) * (div_size) * 2)
    
    elif x + div_size <= r < x + size and y + div_size <= c < y + size:
        return recur(div_size, x + div_size, y + div_size, offset + (div_size) * (div_size) * 3)

print(recur(2**n,0,0,0))