# [Similar-RGB-Color]
# (Every capital letter represents some hexadecimal digit from 0 to f) The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand. 
# For example, "#15c" is shorthand for the color "#1155cc".
# Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.
# Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF, and has a shorthand 
# (that is, it can be represented as some "#XYZ"

# Input: color = "#09f166"
# Output: "#11ee66"

# Explanation:  
# The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
# This is the highest among any shorthand color.

# Note:
# color is a string of length 7.
# color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
# Any answer which has the same (highest) similarity as the best answer will be accepted.
# All inputs and outputs should use lowercase letters, and the output is 7 characters.


def similarRGB(color):
    """
    :type color: str
    :rtype: str
    """
    def getClosest(s):
        m = ['00','11','22','33','44','55','66','77','88','99','aa','bb','cc','dd','ee','ff']
        return min(m, key = lambda x: abs(int(x, 16)- int(s,16)))
    
    res = ''
    color = color[1:]
    for i in range(3):
        s = color[2*i:2*i+2]
        res += getClosest(s)
    return '#' +res

color = "#09f166"
# Output: "#11ee66"
print(similarRGB(color))