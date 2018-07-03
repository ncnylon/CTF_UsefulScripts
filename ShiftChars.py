import string
# Place your ASCII characters here
input_str = 'This is a dog, that\'s a cat.'

# only convert the following patterns
lower_chars = string.ascii_lowercase
upper_chars = string.ascii_uppercase

for i in range(26):
    result = ''
    for j in range(len(input_str)):
        if input_str[j] in upper_chars:
            offset = (upper_chars.index(input_str[j]) + i) % 26 
            c = upper_chars[offset]
        elif input_str[j] in lower_chars:
            offset = (lower_chars.index(input_str[j]) + i) % 26 
            c = lower_chars[offset]
        else:
            c = input_str[j]
        result = result + c

    print('{0:2d} : {1}'.format(i,result))