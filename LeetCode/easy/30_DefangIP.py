# https://leetcode.com/problems/defanging-an-ip-address/

# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".


# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:

# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"


# Constraints:

# The given address is a valid IPv4 address.

def defangIPaddr(address):

    add_split = address.split(".")
    new_str = ''

    for i in range(len(add_split)):
        new_str += add_split[i]
        if i != (len(add_split)-1):
            new_str += "[.]"

    return new_str


address = "255.100.50.0"
print(defangIPaddr(address))
