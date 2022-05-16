# Strings

text = "X-DSPAM-Confidence:    0.8475"

n = text.find('0.8475')

print(float(text[n:]))

