from baseconvert.baseconvert import base


origin = open("01.in", "r")
output = open("01.out", "w")

def split(tupi):
    return [char for char in tupi]

num = tuple(map(int, origin.readline().strip()))
numin = base(num, 10, 2)
zerin = 0
for x in numin:
    if x == 0:
        zerin = zerin + 1
    else:
        zerin = 0
numout = ''
numlen = zerin + 1
numbase = 2
zer = 0
baseout = 2

while zerin < numlen:
    numbase = numbase + 1
    numout = base(numin, 2, numbase,)
    numlen = len(numout)
    for i in numout:
        if i == 0:
            zer = zer + 1
        if len(str(i)) >= 2:
            tupi = [int(z) for z in str(i)]
            for y in tupi:
                if y == 0:
                    zer = zer + 1
                else:
                    zer = 0
        else:
            zer = 0
    if zer > zerin:
        zerin = zer
        baseout = numbase

output.write(str(baseout))

origin.close()
output.close()
