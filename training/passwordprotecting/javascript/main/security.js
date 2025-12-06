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




    // TODO, check if user exists, if so, return an appropriate message



    // BONUS TODO: validate password complexity



    // 2. TODO hash password



    // 3. TODO pass the hashed password instead of the insecure password
    this._storage.insertUser(username, password, publicName);
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
    


    // 5. TODO get the hashed password in the restricted User object, using the username



    // 6. TODO check password with bcrypt against hashed password
  


      // 7. if it matches, get the user Id and pass it to the loginUser method



    // if it doesn't match, return null
    // return null;
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
