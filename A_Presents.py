people = int(input())
presents = list(map(int, input().split()))

givers = [0] * people
for i in range(people):
    receiver = presents[i]
    givers[receiver - 1] = i + 1


print(" ".join(map(str, givers)))