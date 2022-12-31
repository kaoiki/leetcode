s = "MCMXcIV"
s = s.upper()
score = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
# for item in s:
#     print(score[item])

result = 0
for seed in range(len(s)-1):
    if score[s[seed]] < score[s[seed+1]]:
        result -= score[s[seed]]
    else:
        result += score[s[seed]]

result += score[s[len(s)-1]]
print("result = " + str(result))