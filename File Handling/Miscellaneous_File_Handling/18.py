text=input("enter something:")
with open("user_input","w") as f:
    f.write(text)