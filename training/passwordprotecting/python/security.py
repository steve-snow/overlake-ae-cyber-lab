import storage
import bcrypt
import user

"""
Security service layer allows new user creation, login, logout, access validation

https://www.bcrypt.io/languages/python
https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/

"""
class Security:
  salt = bcrypt.gensalt(4)

  def __init__(self,):
    self._mockDb = storage.Storage

  def insertUser(self, username: str | None, password: str | None, publicName: str | None) -> bool:
    # 1. TODO, if no password, return false
    if (password == None):
      print("ERROR - missing password")
      return False
    
    if (username == None):
      print("ERROR - missing username")
      return False

    # TODO, check if user exists, if so, return an appropriate message


    # BONUS TODO: validate password complexity and abort insert with meaningful message if not complex enough


    # TODO hash password
    hashed_password = bcrypt.hashpw(password, self.salt)
    print(hashed_password)


    # TODO pass the hashed password instead of the insecure password
    self._mockDb.insertUser(username, hashed_password, publicName)

    print('    .Security.insertUser - xxxx')
    return True
  
  def loginUser(username: str | None, password: str | None) -> int | None:
    print('    .Security.loginUser - xxxx')

    # TODO, handle null username or null password


    # TODO get the hashed password in the restricted User object, using the username
    restrictedUser = None


    # TODO if restrited user is null, pring error, return null


    # TODO check password with bcrypt against hashed password
    # if it matches, get the user Id and pass it to the loginUser method
    # if it doesn't match, return null


    return None
  
  def logoutUsername (username: str):

    print('    .Security.logoutUsername - xxxx')
  
  def logoutUserId (userId: int):

    print('    .Security.logoutUserId - xxxx')

  
  def logoutToken (token: str):

    print('    .Security.logoutToken - xxxx')

  
  def shutdown (token: str):

    print('    .Security.shutdown - Shutting down security')

if __name__ == '__main__':

  print('Security class test code running')

  testSec = Security()
  # print(f" - SECURITY - {testSto.doesUserExist("HAL")}")

  user1name = "user1"
  user1pwd = "abcdef"
  print(f"inserting user: {user1name}")
  testSec.loginUser(user1name,user1pwd,"user_one")

  print(f"checking for existing user: {user1name}")

  print(f" - SECURITY - USERS contains {user1name} : ")
  