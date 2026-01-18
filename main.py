def main():
    print("Ceci est la fonction main")

def main2():
    for i in range(10):
        print(i)
    return i

def main3():
    i = 0
    while (i < 10):
        print(i)
        i+=1
    return i

def main4():
    return main2() + main3()

if __name__ == "__main__":
    main()