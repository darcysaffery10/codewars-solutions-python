# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

def solution(s):
    if len(s) % 2 == 1:
        s = s + '_'
    l = []
    for i in range(int(len(s)/2)):
        l.append(s[2*i:2*i+2])
    return l