import sys 
import itertools 
sys.setrecursionlimit(1000000000)

def patterncount(Text, Pattern):
    count = 0
    for idx in range(len(Text)-len(Pattern)+1):
        if Text[idx:idx+len(Pattern)] == Pattern:
            count += 1
    return count

def frequentwords(text, k):
    frequentpattern = set()
    count = []
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        count.append(patterncount(text, pattern))
    maxcount = max(count)
    for i in range(len(text)-k+1):
        if count[i] == maxcount:
            frequentpattern.add(text[i:i+k])

    output = ' '.join(frequentpattern)
    print len(frequentpattern)
    return output
    
def reversecomplement(text):
    reverDic = {'A':'T', 'a':'T',
                'T':'A', 't':'A',
                'G':'C', 'g':'C',
                'C':'G', 'c':'G'}
    rever = ''
    for char in text:
        rever = reverDic.get(char, '') + rever
    return rever
    
def allpattern(pattern, text):
    rptn = reversecomplement(pattern)
    ptn = reversecomplement(rptn)
    plen = len(ptn)
    pos = []
    for idx in range(len(text)-plen+1):
        box = text[idx:idx+plen]
        if box ==  ptn or box == rptn:
            pos.append(str(idx))
    return ' '.join(pos)

def patternclumps(text, k, l, t):
    dic = {}
    ptn = []
    for idx in range(len(text)-k+1):
        pattern = text[idx:idx+k]
        dic[pattern] = dic.get(pattern, [])+[idx]
        if len(dic[pattern]) >= 2 and len(dic[pattern]) <= t:
            for pos in dic[pattern][:][:-1]:
                if (idx-pos) > (l - k):
                    dic[pattern].remove(pos)
    for pattern, pos in dic.items():
        if len(pos) >= t:
            ptn.append(pattern)
    return ' '.join(ptn)
                    
def skew(text):
    output = [0]
    dic = {'C': -1, 'G':1, 'A':0, 'T':0}
    for char in text:
        output.append(output[-1] + dic[char]) 
    return ' '.join(map(str, output))

def maxskew(text):
    output = [0]
    dic = {'C': -1, 'G':1, 'A':0, 'T':0}
    for char in text:
        output.append(output[-1] + dic[char])
    m = max(output)
    pos = []
    for idx in range(len(output)):
        if m == output[idx]:
            pos.append(idx)
    return ' '.join(map(str, pos))

def hammingdistance(text1, text2):
    if len(text1) == 1 and len(text2) == 1:
        return int(text1 <> text2)
    else:
        return int(text1[-1] <> text2[-1]) + hammingdistance(text1[:-1], text2[:-1]) 

def approximatematching(pattern, text, d):
    pos = []
    l = len(pattern)
    for idx in range(len(text)-l+1):
        if hammingdistance(pattern, text[idx:idx+l]) <= d:
            pos.append(idx)
    return ' '.join(map(str, pos))

def approximatepatterncount(text, pattern, d):
    l = len(pattern)
    n = 0
    for idx in range(len(text)-l+1):
        if hammingdistance(pattern, text[idx:idx+l]) <= d:
            n += 1
    return n

def mostfrequentkmer(text, k, d):
    patterns = itertools.product('ATGC', repeat = k)
    dic = {}
    for item in patterns:
        pattern = ''.join(item)
        dic[pattern] = approximatepatterncount(text, pattern, d)
    m = max(dic.values())
    output = []
    for pattern, num in dic.items():
        if num == m:
            output.append(pattern)
    return ' '.join(output)

# path = 'C:/Users/Yang/Downloads/frequent_words_mismatch_data_1.txt'
# fh = open(path)
# contect = fh.readlines()
# text = contect[0].strip()
# print contect[1].strip().split()
# k, d = contect[1].strip().split()


print approximatepatterncount('CGTGACAGTGTATGGGCATCTTT', 'TGT', 1)


