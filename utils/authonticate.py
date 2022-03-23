def create_account(name, password):
  return already_got_account(name, password)


def already_got_account (username, pass1):
  name = username
  password = pass1

  with open ("assets/users.csv","r") as file:
  
    if name in file.read():
      return False, "This username already exists, please try another"
  
    else:
      with open ("assets/users.csv","a") as file:
        print("Creating account")
        new_line = "\n"+ name + "," + password 
        file.write(new_line)
        return True, f"{username} has succesfully registered"

# previous code above here

def login(username, password):
    with open("assets/users.csv", "r") as file:
        login_info = []
        for i in file:
            i = i.strip()
            i = i.split(",")
            login_info.append(i)
        login_info.pop(0)

        if in_list(username, login_info) == -1:
            return False, "this username does not exist please try creating an account first"
        else:
            nameindex = in_list(username, login_info)
            if password == login_info[nameindex][1]:
                return True, "successful login"
            else:
                return False, "password incorrect"


# create a second list
def in_list(c, login_info):
    for i, sublist in enumerate(login_info):
        if c in sublist:
            return i

    return -1

  # prvious code below
#create_account()


# # \n issues as it keeps showing when we print
# def login (username, password):
#   with open("assets/users.csv" , "r") as file:
#     login_info = []
#     for i in file:
#       i = i.strip()
#       i = i.split(",")
#       login_info.append(i)
#     login_info.pop(0)
#       #login.info.slice("\n")
#     print(login_info)

#     successful_login = False
# #username.value
  

#     if in_list(username, login_info) == -1:
#       print("this username does not exist please try creating an account first")
#       return False
#     else:
#       nameindex = in_list(username, login_info)
#       if password == login_info[nameindex][1]:
#         print(f" {username} + {password}")
#         print("successful login")
#         successful_login = True
#         return True
#       else:
#         print("password incorrect")
#         return False