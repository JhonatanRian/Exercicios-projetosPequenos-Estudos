from concurrent.futures import ProcessPoolExecutor

exe = ProcessPoolExecutor(max_workers=2)

def contar(n):
    for i in range(n):
        print(i)

result = exe.submit(contar, 15)

for i in range(15, 0, -1):
    print(i)

print(result)