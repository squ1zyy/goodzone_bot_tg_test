if __name__ == "__main__":
    with open("TOKEN.txt", "w") as file:
        token = ""
        file.write(token)


else: 
    with open("TOKEN.txt", "r") as file:
        TOKEN = file.readline()