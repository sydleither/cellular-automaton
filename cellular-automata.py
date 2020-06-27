# Sydney Leither 2020 #
from PIL import Image
from math import ceil
import sys


def check(l,c,r,new_states):
    #[8,7,6,5,4,3,2,1]
    l1, c1, r1 = l, c, r
    patterns = []
    for i, val in enumerate(new_states):
        if val == 1:
            binary = format(i,'03b')
            if binary[0] == '1':
                l1 = not l1
            if binary[1] == '1':
                c1 = not c1
            if binary[2] == '1':
                r1 = not r1
            patterns.append(l1 and c1 and r1)
            l1, c1, r1 = l, c, r
    if True in patterns:
        return True
    return False


def create(img, pixels, case):
    for j in range(1,img.size[0]-1):
        for i in range(1,img.size[1]-1):
            if check(pixels[i-1,j-1] == (0,0,0), pixels[i,j-1] == (0,0,0), \
                     pixels[i+1,j-1] == (0,0,0), case):
                pixels[i,j] = (0,0,0)


def main():
    print('Enter your rule set (in format 0 0 0 1 1 1 1 0):')
    rule_set = input()
    try:
        rule_set = list(map(int, rule_set.split()))
    except:
        print('Invalid input')
        sys.exit(0)
    if len(rule_set) != 8 and not 0 in rule_set and not 1 in rule_set:
        print('Invalid input')
        sys.exit(0)
        
    img = Image.new('RGB',(100,100),(255,255,255))
    pixels = img.load()

    pixels[ceil(img.size[0]/2),0] = (0,0,0)
    create(img, pixels, rule_set)
            
    img.show()
    
    
if __name__ == '__main__':
    main()