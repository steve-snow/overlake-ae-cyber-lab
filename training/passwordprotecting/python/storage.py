import guid
from user import User
from token import UserToken
from collections import defaultdict
"""
Storage simulates a generic storage device that could be a database
"""

class Storage:

  USERS:User = []
  USER_TOKENS:UserToken = []
  DATA = []

  expirationMsec = 10000

  def insertUser(username: str = None, password: str = None, publicName: str = None) -> int:
    if username == None or password == None:
      print("Failed to insert user, missing critical information")
      return False
    newUser = User(username, password, publicName)
    Storage.USERS.append(newUser)
    print(f"    .Storage.insertUser - Inserting: {newUser.id()} {username} {newUser._publicName}")
    return newUser.id()
  
  def doesUserExist(username:str = None):
    if username == None:
      return False
    for u in Storage.USERS:
      if u.username() == username:
        return True
    return False
  
  def getUser_RESTRICTED(username = None):
    if username == None:
      return None
    for u in Storage.USERS:
      if u.username() == username:
        return u
    print(f"    .Storage.getUserHash - Failed to find user: {username}")
    return None
  
  def loginUser(userId = -1):
    token = guid.generateGUID()
    print(f"    Generated token: {token}")
    Storage.USER_TOKENS.append(UserToken(userId, token))
    return token
  
  def isDuplicate(username:str = None):
    counter = 0
    for u in Storage.USERS:
      if u.username() == username:
        counter += 1
    return counter > 1
  
  #region TOKEN

  def isTokenValid(token:str = "0000"):
    found = None
    for uToken in Storage.USER_TOKENS:
      if uToken.token() == token:
        found = uToken
    if (found != None):
      print(f"    .Storage.isTokenValid::  expiration: ${Storage.expirationMsec}  token created: ${found._createdDateTime}")
      if (found._createdDateTime > Storage.expirationMsec):
        return found.getUserId()
      else:
        found._isValid = False
    return None

  def getTokenFromUserId(userId:int = -1):
    found = None
    for uToken in Storage.USER_TOKENS:
      if uToken.userId() == userId:
        found = uToken
    return found
  
  #endregion

  #region LOGOUT

  def logout(userId:int = -1):
    found = None
    for uToken in Storage.USER_TOKENS:
      if uToken.userId() == userId:
        found = uToken
    if found != None:
      found.invalidateToken()

  def logoutToken(token:str = None):
    found = None
    for uToken in Storage.USER_TOKENS:
      if uToken.token() == token:
        found = uToken
    if found != None:
      found.invalidateToken()

  def logoutUsername(username:str = None):
    usr = Storage.getUser_RESTRICTED(username)
    found = None
    for uToken in Storage.USER_TOKENS:
      if uToken.userId() == usr.UserId():
        found = uToken
    if found != None:
      found.invalidateToken()

  #endregion LOGOUT

  def shutdown (token: str = None):

    print('    .Storage.shutdown - Shutting down Storage')
    print('    .Storage - USERS content analysis:\n')
    if len(Storage.USERS) < 1:
      print("   - - - No users exist in storage - - -")
    for u in Storage.USERS:
      print(f"   USER:   {u.describe()}")

if __name__ == '__main__':

  print('\n ----- Storage class test code running ------- \n')

  testSto = Storage()
  print(f" - STORAGE - checkint for HAL : exists? {testSto.doesUserExist("HAL")}")

  user1name = "user1"
  user1pwd = "abcdef"
  print(f"\ninserting user: {user1name}")
  print(f"{testSto.insertUser(username= user1name, password= user1pwd, publicName="user_one")}")

  print(f"\nchecking for existing user: {user1name}")

  print(f"\n- STORAGE - USERS contains {user1name} : {testSto.doesUserExist(user1name)}")

  testSto.shutdown()
  