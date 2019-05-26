text = "X-DSPAM-Confidence:    0.8475";
number = text.find('.')
endnum = text[number:]
result = float(endnum)
print(result)
