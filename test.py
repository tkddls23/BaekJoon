import sys
def convert(s):
    x, y = s.split()
    return int(x) + int(y)/1000000
    
arr = sys.stdin.readlines()[1:]
arr = sorted(arr, key=lambda x: convert(x))
print(''.join(arr))
