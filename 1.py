n = int(input())

total = {}
ok = {}

for i in range(n):
    elems = input().split()

    name = elems[0]
    task = elems[1]
    result = elems[2]

    if name in total:
        total[name] += 1
    else:
        total[name] = 1

    if result.lower() != 'ok':
        continue

    if name in ok:
        if task in ok[name]:
            ok[name][task] += 1
        else:
            ok[name][task] = 1
    else:
        ok[name] = {task: 1}

# sort total by name
total = dict(sorted(total.items()))

for name in total:
    if name not in ok:
        print(name, total[name], 0)
        continue
       
    print(name, total[name], len(ok[name]))
