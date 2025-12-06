class UserToken:

  def __init__(self, userId:int, token:str) -> None:
    self._token = token
    self._userId = userId
    self._createdDateTime = 0
    self._isValid = True

  def userId(self):
    return self._userId
  
  def token(self):
    return self._token
  
  def invalidateToken(self):
    self._isValid = False
