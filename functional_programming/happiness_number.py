'''
You will be given a string of characters containing only the three characters : ( ) :

Create a function returns a number based on the number of sad and smiley faces there are.

The happy faces :) and (: are worth 1.
The sad faces :( and ): are worth -1.
'''


def happiness_number(txt):
    return sum(j * txt.count(i) for i, j in {':)': 1, '(:': 1, ':(': -1 , '):': -1}.items())

print(happiness_number(":):("))
