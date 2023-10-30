from movies import Movies

movies = Movies('./movies.txt')


x = 1
while x == 1:
    choice = input("\nOptions:\nq - quit\nsn - Search films by name\nsc - Search films by cast members\nlist - Print all films' names\n\nWhat will you do? ")

    if choice == "q":
        x = 0
    elif choice == "list":
        for i in movies._movies:
            print(i['name'])
    else:
        print("Invalid input. Try again.")
