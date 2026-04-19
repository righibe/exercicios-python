def isAnagrama(string, string2):
    if len(string) != len(string2):
        return False
    counts = {}
    
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
            
    for char in string2:
        if char not in counts:
            return False
        counts[char] -= 1
        
        if counts[char] < 0:
            return False
    return True

def main():
    string = input("Digite uma string: ")
    string2 = input("Digite outra string: ")
    print(isAnagrama(string, string2))

if __name__ == "__main__":
    main()
