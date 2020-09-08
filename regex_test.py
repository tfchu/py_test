'''
open a file as string, find number > 1001.0000ns

Quantifiers
?: once or more times

Lookahead
q(?=u): positive lookahead. matches a 'q' that is follwed by a 'u'
q(?!u): negative lookahead. matches a 'q' that is NOT followed by a 'u'

Lookbehind
(?<=a)b: positive lookbehind. matches a 'b' that is preceded by an 'a'
(?<!a)b: negative lookbehind. matches a 'b' that is NOT preceded by an 'a'

'''

import re

# find > 1200
def simple_find():
    my_str = 'start, 1201, end'
    # match >= 1200
    #pattern = r'([1-9][2-9][0-9]{2,})'
    # match > 1200 (split to 1201 ~ 1209, 1210 ~ 1299, 1300 ~ 9999, >= 10000)
    pattern = r'(120[1-9]|12[1-9][0-9]|[1-9][3-9][0-9]{2,}|[0-9]{5,})'
    m = re.search(pattern, my_str)
    if m:
        print(m.group(1))
    else:
        print('no match.')

def load_file_and_find():
    with open('C:\\Users\\tony.chu\\Desktop\\Debug\\tmp.csv', 'r') as f:
        for line in f:
            # match = 501 ns
            #pattern = r',([4-9](?!00)[0-9][0-9]?\d+[0-9\.]+)\sns,'
            # match > 1000 ns
            pattern = r',([0-9]{3}\.[0-9]+)\sns,'
            m = re.match(pattern, line)
            if m:
                print(m.group(1))

if __name__ == '__main__':
    simple_find()