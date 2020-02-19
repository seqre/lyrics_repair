import sys

if len(sys.argv) != 3:
    exit('Proper usage: python3 lyrics_repair.py in.srt out.srt')

f = open(sys.argv[1], 'r')
encoding = f.encoding
f.close()

in_file = open(sys.argv[1], 'rb')
out_file = open(sys.argv[2], 'wb')

data = in_file.read()

dict_map = {
    b'\xb3': u'\u0142'.encode(encoding),  # ł
    b'\xbf': u'\u017C'.encode(encoding),  # ż
    b'\xb9': u'\u0105'.encode(encoding),  # ą
    b'\xf3': u'\u00F3'.encode(encoding),  # ó
    b'\xe6': u'\u0107'.encode(encoding),  # ć
    b'\xea': u'\u0119'.encode(encoding),  # ę
    b'\x9c': u'\u015b'.encode(encoding),  # ś
    b'\x9f': u'\u017a'.encode(encoding),  # ź
    b'\xf1': u'\u0144'.encode(encoding),  # ń
}

for k, v in dict_map.items():
    data = data.replace(k, v)

out_file.write(data)
