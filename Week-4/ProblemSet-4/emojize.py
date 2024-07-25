import emoji

get_input = input("Input: ")
print(f"Output: {emoji.emojize(get_input, language = "alias")}")
