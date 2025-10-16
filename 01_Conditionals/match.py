#Match-case 문 사용 (if, elif 대신 사용)



name = input("What's your name?")

match name :
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
        