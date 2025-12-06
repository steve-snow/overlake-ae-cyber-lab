class UserToken {
  _token;
  _userId;
  _createdDateTime; // msec
  _isValid = true;

  /**
   * 
   * @param {int} userId 
   * @param {GUID} token 
   */
  constructor(userId, token) {
    this._token = token;
    this._userId = userId;
    this._createdDateTime = Date.now();
  }

  getUserId() {
    return this._userId;
  }

  getToken() {
    // let currentCutoff = Date.now() - expiration;
    return this._token;
  }

  invalidateToken() {
    this._isValid = false;
  }

}

export default UserToken;
