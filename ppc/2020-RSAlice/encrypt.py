from random import randint


with open("alice_in_wonderland_modified.txt", "r") as f:
    text = f.read()


flag = '***********'
rid = randint(0, len(text) - 1)
text = text[:rid] + flag + text[rid:]


new_text = ''
l = 0
r = len(text) - 1
while(l <= r):
    new_text += text[l]
    l += 1
    if l <= r:
        new_text += text[r]
        r -= 1


print(new_text)
