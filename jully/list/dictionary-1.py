user_info = {'id': 'software', 'pw': 'python'}
id = input("Input ID:")
pw = input("Input PW:")

if user_info['id'] != id:
    print("ID  Mismatch!")
elif user_info['pw'] != pw:
    print("PW Mismatch!")
else:
    print("Success in Login")
