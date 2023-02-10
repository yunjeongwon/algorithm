import sys
input = sys.stdin.readline

content = input().rstrip()
arr = content.split()
n = int(input())
given = list(map(int, input().split()))
for i in range(len(content)):
    if i - 1 >= 0 and (content[i - 1] == content[i] == " "):
        continue
    if content[i] == " ":
        n -= 1
        continue
    if i - 1 >= 0 and (content[i - 1] == content[i]):
        continue
    if content[i].isupper():
        given[ord(content[i]) - ord("A")] -= 1
    else:
        given[ord(content[i]) - ord("a")] -= 1

if n < 0:
    print(-1)
    exit()

for i in given:
    if i < 0:
        print(-1)
        exit()

ans = ""
for i in arr:
    given[ord(i[0].lower()) - ord("a")] -= 1
    ans += i[0].upper()

for i in given:
    if i < 0:
        print(-1)
        exit()
print(ans)
