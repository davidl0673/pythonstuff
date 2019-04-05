rot13_dict = {}

for i in range(26):
    rot13_dict[chr(i + 97)] = chr(((i + 13) % 26) + 97)


for i in range(26):
    rot13_dict[chr(i + 65)] = chr(((i + 13) % 26) + 65)


def rot13(message):
    encrypted_message = []
    for charecter in message:
        try:
            encrypted_message.append(rot13_dict[charecter])
        except KeyError:
            encrypted_message.append(charecter)                                 # used exceptions to accept spaces


secret = rot13 ("I like pie")
print(secret)
print(rot13(secret))