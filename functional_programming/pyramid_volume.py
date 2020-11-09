'''
Create a function that takes the length, width, height (in meters)
and output unit and returns the volume of a pyramid
to three decimal places in the correct unit.
'''

def pyramid_volume(l, w, h, unit):
    dct = {
        'centimeters' : 100,
        'millimeters' : 1000,
        'kilometers' : 0.001,
        'meters' : 1,
    }
    result = (l * w * (dct[unit] ** 3) * (h / 3))
    # result = result[:result.find('.')+4] if len(result) - result.find('.') > 3 \
                                         # else result + '00'
    return '{:.3f} cubic {}'.format(result, unit)

print(pyramid_volume(4, 6, 20, "centimeters"))
 # ➞ "160000000.000 cubic centimeters"

print(pyramid_volume(1843, 1823, 923, "kilometers"))
 # ➞ "1.033 cubic kilometers"

print(pyramid_volume(18, 412, 93, "millimeters"))
 # ➞ "229896000000000.000 cubic millimeters"
