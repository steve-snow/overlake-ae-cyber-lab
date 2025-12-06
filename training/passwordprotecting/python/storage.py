import guid
import user
from token import UserToken
from collections import defaultdict
"""
Storage simulates a generic storage device that could be a database
"""

class Storage:

  USERS:user.User = []
  USER_TOKENS:UserToken = []
  DATA = []

  expirationMsec = 10000

  def insertUser(self, username: str, password: str, publicName: str) -> int:
    newUser = user.User(username, password, publicName)
    Storage.USERS.append(newUser)
    print(f"    .Storage.insertUser - Inserting: {newUser.id()} {username} {newUser._publicName}")
    return newUser.id()
  
  def doesUserExist(self, username:str):

    for u in Storage.USERS:
      if u.username() == username:
        return True
    return False
  
  def getUser_RESTRICTED(self, username):
    for u in Storage.USERS:
      if u.username() == username:
        return u
    print(f"    .Storage.getUserHash - Failed to find user: {username}")
    return None
  
  def loginUser(self, userId):
    token = guid.generateGUID()
    print(f"    Generated token: {token}")
    Storage.USER_TOKENS.append(UserToken(userId, token))
    return token
  
  def isTokenValid(self, token:str):
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

  def getTokenFromUserId(self, userId:int):
    found = None
    for uToken in Storage.USER_TOKENS:
      if uToken.userId() == userId:
        found = uToken
    return found

  def logout(self, userId:int):
    found = None
    for uToken in Storage.USER_TOKENS:
      if uToken.userId() == userId:
        found = uToken
    if found != None:
      found.invalidateToken()

  def logoutToken(self, token:str):
    found = None
    for uToken in Storage.USER_TOKENS:
      if uToken.token() == token:
        found = uToken
    if found != None:
      found.invalidateToken()

  def logoutUsername(self, username:str):
    user = self.getUser_RESTRICTED(username)
    found = None
    for uToken in Storage.USER_TOKENS:
      if uToken.userId() == user.userId():
        found = uToken
    if found != None:
      found.invalidateToken()

  def isDuplicate(self, username:str):
    counter = 0
    for u in Storage.USERS:
      if u.username() == username:
        counter += 1
    return counter
  
  def shutdown (token: str):
    # TODO as required
    print('    .Storage.shutdown - Shutting down security')

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
  