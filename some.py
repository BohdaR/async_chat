import re

if __name__ == '__main__':

    s = 'bvi_47 ' \
        'BohdaR ' \
        'How are you?'
    s.replace()

    r = re.search(r'(^\d+)', s)
    r = re.split(r'(\d+)', s)
    ns = re.sub(r'(^\d+)', '', s)
    print(r.count(''))
print(r)
print(ns)
