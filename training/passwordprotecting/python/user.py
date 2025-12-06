class User:
  _idRef = 0

  def __init__(self, username:str, pwdHash:str, publicName:str):
    self._idRef += 1
    self._id = self._idRef
    self._username = username
    self._publicName = publicName
    self._pwdHash = pwdHash
    self._createdDateTime = 0
    self._modifiedDateTime = self._createdDateTime
    self._lastLoginDateTime = 0

  def username(self):
    return self._username

  def getUserIdAndHash(self):
    return { self._id, self._pwdHash }

  def id(self):
    return self._id

  def setPublicName(self, publicName:str):
    self._publicName = publicName
    self._createdDateTime += 1

  def updateLastLogin(self, loginDateTIme):
    self._lastLoginDateTime = loginDateTIme

  def describe(self):
    print(f" User: ${self._id} ${self._username} ${self._publicName} ${self._pwdHash} ${self._createdDateTime}")
