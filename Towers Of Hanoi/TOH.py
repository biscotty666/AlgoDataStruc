def pm(start, end):
    print(start, '->', end)
    
def hanoi(n, start, end):
    """
    Print list of steps to move n disks from start rod to end rod
    """
    if n == 1:
        pm(start, end)
    else:
        other = 6 - (start + end)
        hanoi(n-1, start, other)
        pm(start, end)
        hanoi(n-1, other, end)



hanoi(3,1,3)