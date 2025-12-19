def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    text = text.replace("=)", "😄")
    text = text.replace(":3", "😊")
    text = text.replace(":D", "😁")
    text = text.replace(":P", "😛")
    text = text.replace(":O", "😮")
    text = text.replace(":X", "😦")
    text = text.replace(":@", "😠")
    text = text.replace(":S", "😨")
    text = text.replace(":$", "😳")
    text = text.replace(":|", "😐") 
    text = text.replace(":/", "😕") 
    text = text.replace(":-", "😑")
    return text


def main():
    user_input = input("Give me your best face :")
    result = convert(user_input)
    print(result)

main()