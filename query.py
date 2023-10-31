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
    elif choice == "sn":
        n = input("   Enter a search term: ").lower()
        for i in movies._movies:
            if n in i['name'].lower():
                print(i['name'])
    elif choice == "sc":
        n = input("   Enter a search term: ").lower()
        namelist = []

        for i in movies._movies:
            castlist = i['cast']
            m = 0
            flag = 0
            while m < len(castlist):
                if n in castlist[m].lower():
                    if flag == 0:
                        print(i['name'])
                        flag = 1
                    namelist.append(castlist[m])
                m = m+1
            if flag == 1:
                print(namelist)
                
    else:
        print("Invalid input. Try again.")
