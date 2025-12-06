from storage import Storage
import bcrypt
# import user

"""
Security service layer allows new user creation, login, logout, access validation

https://www.bcrypt.io/languages/python
https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/

"""
class Security:
  salt = bcrypt.gensalt(10)
  _mockDb = Storage

  #region INSERT, LOGIN

  def insertUser(username: str | None, password: str | None = None, publicName: str | None =None) -> bool:
    # print(f" Security.insertUser (  {username} {password} {publicName}  )  ")
    # 1. TODO, if no password, return false
    

    # BONUS TODO: validate password complexity and abort insert with meaningful message if not complex enough


    # TODO, check if user exists, if so, return an appropriate message


    # TODO hash password


    # TODO pass the hashed password instead of the insecure password

    # print(f'    .Security.insertUser - {username} - into database')

    return True
  
  def loginUser(username: str | None = None, password: str | None = None) -> int | None:
    # print(f'    .Security.loginUser - {username}  {password}')

    # TODO, handle null username or null password
    
    
    # TODO get the hashed password and id in the restricted User object, using the username
    # restrictedUser = 


    # TODO if restrited user is null, print error, return null


    # TODO check password with bcrypt against hashed password

      # if it matches, get the user Id and pass it to the loginUser method


      # print(f"    .Security.loginUser - auth token: {authToken}")
      # return authToken

    # if it doesn't match, return null
    return None
  
  #endregion LOGIN
  
  #region LOGOUT

  def logoutUsername (username: str):

    print('    .Security.logoutUsername - xxxx')
  
  def logoutUserId (userId: int):

    print('    .Security.logoutUserId - xxxx')

  
  def logoutToken (token: str):

    print('    .Security.logoutToken - xxxx')

  #endregion
  
  #region DATA ACCESS

  #endregion

  def shutdown (token: str = None):
    print('\n    .Security.shutdown - Shutting down security')
    Storage.shutdown()

if __name__ == '__main__':

  print('Security class test code running')

  testSec = Security(str)
  # print(f" - SECURITY - {testSto.doesUserExist("HAL")}")

  user1name = "user1"
  user1pwd = "abcdef"
  print(f"inserting user: {user1name}")
  testSec.loginUser(user1name,user1pwd,"user_one")

  print(f"checking for existing user: {user1name}")

  print(f" - SECURITY - USERS contains {user1name} : ")
  