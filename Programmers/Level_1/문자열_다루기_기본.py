def solution(s):
    try:
        if(len(s) == 4 or len(s) == 6):
            int(s)
            return True
        else:
            return False
    except:
        return False