http_code = "419"
match http_code:
    case "200":
        print("Hi")
    case _:
        print("Code not found")