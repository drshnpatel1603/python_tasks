# print("hello world")

# -----------------  total NUM or Avg ---------------------
output = {}
mydict = {
    'nilesh-geography': 89,
    'alpesh-history': 77,
    'shital-math': 93,
    'dimpal-hindi': 68,
    'nilesh-english': 74,
    'alpesh-sci': 85,
    'shital-history': 91,
    'dimpal-geography': 87,
    'nilesh-sci': 83,
    'alpesh-math': 92,
    'dimpal-english': 78,
    'shital-hindi': 81,
    'nilesh-history': 90,
    'alpesh-geography': 79,
    'dimpal-math': 84,
    'shital-sci': 88,
    'nilesh-hindi': 71,
    'alpesh-english': 80,
    'dimpal-sci': 89,
    'shital-geography': 82,
    'nilesh-math': 93,
    'alpesh-hindi': 75,
    'dimpal-history': 90,
    'shital-english': 87
}
count = 0
avg = {}
for key ,val in mydict.items():
    new_key = key.split("-")
    new_val = output.get(f"{new_key[0]}")
    if new_val:
        out = new_val + val
        output.update({f'{new_key[0]}' : out})
        avg.update({f'{new_key[0]}' : avg[f'{new_key[0]}']+1})
    else:
        output.update({f'{new_key[0]}' : val})
        avg.update({f'{new_key[0]}' : 1})

print(f"Total Marks : {output})")

# -------------  AVG MARKS -----------------
for key, val in avg.items():
    avg.update({f"{key}" : output[f'{key}']/val})
print(f"AVG meks : {avg}")


# -------------  Highest Score -------------
temp_name = ""
temp_mark = 0
for name,mark in output.items():
    if temp_mark < mark:
        temp_name = name
        temp_mark = mark

print(f"highest score : {temp_name} : {temp_mark}")


# -------------- Subject vise highest marks -----------------
stu_subject = {}
for name, mark in mydict.items():
    new_name = name.split("-")[1]
    if stu_subject.get(f'{new_name}'):
        if stu_subject.get(f'{new_name}') < mark:
            stu_subject[f'{new_name}'] = mark
    else:
        stu_subject[f'{new_name}'] = mark

print(f"Subject wise Highest marks : {stu_subject}")

#  -------------------- highest to lower marks -----------------
print({k : v for k,v in sorted(output.items(), key=lambda key: key[1], reverse=True)})
# print(temp)


