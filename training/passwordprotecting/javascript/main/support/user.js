let idRef = 0;

/**
 * User Class for storing critical user information.
 */
class User {

  _id;
  _username;
  _password;
  _publicName;
  _createdDateTime;
  _modifiedDateTime = 0;
  _lastLoginDateTime = 0;

  /**
   * constructor
   * @param {*} username 
   * @param {*} password 
   * @param {*} publicName 
   */
  constructor(username, password, publicName) {
    this._id = ++idRef;
    this._username = username;
    this._password = password;
    this._publicName = publicName ?? username;
    this._createdDateTime = Date.now();
  }

  getUsername() {
    return this._username;
  }

  getUserIdAndHash() {
    return { id: this._id, pwd: this._password };
  }

  getId() {
    return this._id;
  }

  describe() {
    console.log(`  >>>   User: ${this._id} ${this._username} ${this._publicName} ${this._password} ${this._createdDateTime}`)
  }

}

export default User;