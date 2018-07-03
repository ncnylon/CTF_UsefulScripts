import hashlib

clear_text = 'H8?jp$s9?h3w9m?f0'
hashed_text = '25c300???efc09??0de2????a769???a'

pattens = []
accepted_results = []                                                                                                          

# ascii code printable 32 - 127
rang = range(32,127)


print('len(clear_text)={0}'.format(len(clear_text)))
print('len(hashed_text)={0}'.format(len(hashed_text)))

x = 0 
for i in rang:
    for j in rang:
        for k in rang:
            test = ''.join([clear_text[0:2], chr(i), clear_text[3:8], chr(j), clear_text[9:14], chr(k), clear_text[15:]])
            m = hashlib.md5()
            m.update(test.encode('ascii'))
            result = m.hexdigest()
            x = x + 1 
            #print('{0:7d}: {1} -> {2}'.format(x, test, result))
            if result[0:6] == hashed_text[0:6] and result[9:14] == hashed_text[9:14] and \
               result[16:20] == hashed_text[16:20] and result[24:28] == hashed_text[24:28] and \
               result[-1] == hashed_text[-1]:
                print('{0} -> {1}'.format(test,result))
                accepted_results.append([test,result,hashed_text])

print(accepted_results)