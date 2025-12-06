import * as bcrypt from "bcrypt"
// import generateGUID from "./support/guid.js";
import Storage from "./support/storage.js";

// https://www.bcrypt.io/languages/javascript
// https://blog.logrocket.com/password-hashing-node-js-bcrypt/

// TODO : generate hash salt
const salt = bcrypt.genSaltSync(4);

class Security {

  _storage;

  constructor() {
    this._storage = new Storage();
  }

  //#region ADD USER and LOGIN

  /**
   * insert new user
   * @param {string?} username 
   * @param {string?} password 
   * @param {string?} publicName 
   * @returns {bool} success
   */
  insertUser(username = null, password = null, publicName = null) {

    // 1. TODO, if no password, return false
    if (!password) {
      console.error("ERROR - password is missing");
      return false;
    }
    if (!username) {
      console.error("ERROR - username is missing");
      return false;
    }

    // BONUS TODO: validate password complexity
    if (password.length < 8) {
      console.error("ERROR - ");
      return false;
    }

    // TODO, check if user exists, if so, return an appropriate message
    if (this._storage.doesUserExist(username)) {
      console.error("ERROR - ");
      return false;
    }

    // 2. TODO hash password
    const hashedPwd = bcrypt.hashSync(password, salt);
    console.log(`  before: ${password}     after: ${hashedPwd}`)

    // 3. TODO pass the hashed password instead of the insecure password
    this._storage.insertUser(username, hashedPwd, publicName);
    return true;
  }

  /**
   * login existing user
   * @param {string?} username 
   * @param {string?} password 
   * @returns {string?} GUID token
   */
  loginUser(username = null, password = null) {

    // 4. TODO, handle null username or null password
    if (!username || !password) {
      console.error("ERROR - Invalid username or password");
      return null;
    }

    // 5. TODO get the hashed password in the restricted User object, using the username
    const restricted_user = this._storage.getUser_RESTRICTED(username);

    // confirm found the user
    if (!restricted_user) {
      console.error("ERROR - Invalid username or password");
      return null;
    }

    // 6. TODO check password with bcrypt against hashed password
    if (bcrypt.compareSync(password, restricted_user._password)) {

      // 7. if it matches, get the user Id and pass it to the loginUser method
      const authToken = this._storage.loginUser(restricted_user._id);
      console.log(`    .Security.loginUser - authentication token: ${authToken}`)
      return authToken;
    }

    // if it doesn't match, return null
    console.error("ERROR - Invalid username or password");
    return null;
  }

  //#endregion

  //#region LOGOUT

  /**
   * 
   * @param {*} username 
   */
  logoutUsername(username) {

  }

  /**
   * 
   * @param {int} userId 
   */
  logoutUserId(userId) {

  }

  /**
   * 
   * @param {string} token GUID
   */
  logoutToken(token) {

  }

  //#endregion

  //#region DATA ACCESS



  //#endregion

  /**
   * shutdown the app and trigger any cleanup tasks
   */
  shutdown() {
    console.log(`    .Security.shutdown - Shutting down security`)

    this._storage.shutdown();
  }

}

export default Security;
