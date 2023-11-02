from bot import parser

def main():
    while True:
        user_input = input(">>>")
        func, data = parser(user_input)
        result = func(*data)
        print(result)
        if result == "Good bye!":
            break
        

if __name__ == '__main__':
    main()