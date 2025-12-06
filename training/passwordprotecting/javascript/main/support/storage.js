import User from "./user.js"
import UserToken from "./token.js";
import generateGUID from "./guid.js";

const USERS = [];

const USER_TOKENS = [];

const DATA = [];

const expirationMsec = 10000;

class Storage {

  constructor() {
    // read users files to load array
    // 
  }

  // #region USER ACCESS

  /**
   * 
   * @param {string} username 
   * @param {string} password - GUID
   * @param {string} publicName 
   */
  insertUser(username, password, publicName) {
    let user = new User(username, password, publicName);
    USERS.push(user);
    console.log(`    .Storage.insertUser - Inserting: ${user.getId()} ${username} ${user._publicName}`)
    return user.getId();
  }

  /**
   * 
   * @param {string} username 
   * @returns {boolean}
   */
  doesUserExist(username) {
    return (USERS.find(user => user.getUsername() == username) != null);
  }

  /**
   * 
   * @param {string} username 
   * @returns {User}
   */
  getUser_RESTRICTED(username) {
    let index = USERS.findIndex(user => user.getUsername() == username);
    if (index > -1) {
      return USERS[index]
    }
    console.log(`    .Storage.getUserHash - Failed to find user: ${username}`)
    return null;
  }

  /**
   * Set the user to a logged in state by storing the token and user Id
   * @param {int} userId 
   * @returns {string} auth token 
   */
  loginUser(userId) {
    const token = generateGUID()[0]
    console.log(`    Generated token: ${token}`)
    USER_TOKENS.push(new UserToken(userId, token))
    return token;
  }



  
  /**
   * isTokenValid
   * @param {string} token - auth GUID 
   * @returns {int} user Id
   */
  isTokenValid(token) {
    currentCutoff = Date.now()
    const found = USER_TOKENS.find(ut => ut.getToken(expirationMsec) == token)
    console.log(`    .Storage.isTokenValid::  cutoff: ${currentCutoff}  token created: ${found?._createdDateTime}`);
    if (found) {
      if (found._createdDateTime + expirationMsec > currentCutoff) {
        return found?.getUserId();
      } else {
        found._isValid = false;
      }
    }
    return null;
  }

  /**
   * getTokenFromUserId
   * @param {int} userId 
   * @returns 
   */
  getTokenFromUserId(userId) {
    const found = USER_TOKENS.find(ut => ut.getUserId() == userId)
    return found?.getToken();
  }

  /**
   * logout
   * @param {int} userId 
   */
  logout(userId) {
    const found = USER_TOKENS.find(ut => ut.getUserId() == userId)
    if (found) {
      found.invalidateToken();
    }
  }

  /**
   * logoutUsername
   * @param {string} token GUID
   */
  logoutToken(token) {
    const found = USER_TOKENS.find(ut => ut.getToken() == token)
    if (found) {
      found.invalidateToken();
    }
  }

  /**
   * logoutUsername
   * @param {string} username 
   */
  logoutUsername(username) {
    const user = getUser_RESTRICTED(username);
    if (user) {
      const found = USER_TOKENS.find(ut => ut.getUserId() == user.getId())
      if (found) {
        found.invalidateToken();
      }
    }
  }

  /**
   * isDuplicate
   * @param {string} username 
   */
  isDuplicate(username) {
    let counter = 0;
    const nameCounter = (usr) => {
      if (usr._username == username) {
        counter++;
      }
    }
    USERS.forEach(nameCounter);
    console.log(`    .Storage.isDuplicate:: count of username ${username} is ${counter}`)
    if (counter == 0) console.log("    .Storage.isDuplicate:: username does not exist")
    return (counter > 1);
  }

  // #endregion USER ACCESS

  // #region STORAGE

  insertData(data, token, userId) {

  }

  getDataPermissions(dataId) {

  }

  readData(dataId) {

  }

  updateData(dataId, newData) {

  }

  deleteData(dataId) {

  }

  // #endregion STORAGE

  shutdown() {
    console.log(`    .Storage.shutdown - Shutting down storage`)

    // write to files

    const len = USERS.length;
    for (let i = 0; i < len; i++) {
      USERS[i].describe();
    }

  }
}

export default Storage;
