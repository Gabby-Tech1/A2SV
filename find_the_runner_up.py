if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    result = set(arr)
    result.remove(max(result))
    print(max(result))