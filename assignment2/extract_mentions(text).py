def extract_mentions(text):
    mentions = []

    for word in text.split():
        if word.startswith("@"):
            username = word[1:]
            if username and all(char.isalnum() or char == "_" for char in username):
                mentions.append(word)

    return mentions


message = "Hello @sam and @riya"
print(extract_mentions(message))  # ['@sam', '@riya']