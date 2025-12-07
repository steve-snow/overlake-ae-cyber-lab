import generateGUID from "./support/guid.js";
import Security from "./security.js";
import * as cmdLine from "./support/cmdLine.js"

const {
  readCmdLine
} = cmdLine;

const security = new Security();
const storageAccess = security._storage;

function main() {
  console.log("\n------ PASSWORD TEST STARTING ----- JAVASCRIPT -----\n");

  const runLevel = readCmdLine();
  console.log(`::: Run Level : ${runLevel} :::`)

  let issuesCount = 0;
  let passingCount = 0;
  let itemCounter = 0;
  let report = "Password Test Report"; // TODO insert date time

  //#region INSERT NEW USER

  // generate username and password

  const user1 = "alpha@mail.com";

  const user2 = "bravo@mail.com";
  const pwd2 = "123456";

  const user3 = "charlie@mail.com";
  const pwd3 = generateGUID()[0];
  const pwd3b = generateGUID()[0];

  const user4 = "delta@mail.com";
  const pwd4 = generateGUID()[0];

  // const user5 = "echo@mail.com";

  // call security.postNewUser with username only - should be rejected

  console.log(`\n... logging item ${++itemCounter} ................ insert New User with username only - should be rejected\n`)
  if (security.insertUser(user1)) {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - reported adding user without password`;
  } else {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - user without password blocked`;
  }

  console.log(`\n... logging item ${++itemCounter} ................ verify user NOT added \n`)
  if (storageAccess.doesUserExist(user1)) {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - added user without password`;
  } else {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - user without password not added to storage`;
  }

  // call security.postNewUser with username and password - not robust enough - should be rejected

  console.log(`\n... logging item ${++itemCounter} ................ insert New User with username and password - not robust enough - should be rejected\n`)
  if (security.insertUser(user2, pwd2)){
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - password not complex enough`;
  } else {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - successfully rejected poor password - lacks sufficient complexity`;
  }

  console.log(`\n... logging item ${++itemCounter} ................ verify user NOT added \n`)
  if (storageAccess.doesUserExist(user2)) {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - added user without complex password`;
  } else {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - user without password not added to storage`;
  }

  // call security.postNewUser with username and diff password - robust - successful

  console.log(`\n... logging item ${++itemCounter} ................ insert New User with username and good password - robust - successful\n`)
  if (security.insertUser(user3, pwd3)){
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - user added sucessfully`;
  } else {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - new valid user rejected`;
  }

  console.log(`\n... logging item ${++itemCounter} ................ verify user added\n`)
  if (storageAccess.doesUserExist(user3)) {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - user exists in storage`;
  } else {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - user missing from storage`;
  }

  // call security.postNewUser with username and diff password - repeat uersname - should be rejected

  console.log(`\n... logging item ${++itemCounter} ................ insert New User with repeat username and diff password - should be rejected\n`)
  if (security.insertUser(user3, pwd3b)){
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - new user incorrectly added when username already exists`;
  } else {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - user rejected because username already exists`;
  }

  console.log(`\n... logging item ${++itemCounter} ................ verify no duplicate exists for username\n`)
  if (storageAccess.isDuplicate(user3)) {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - duplicated existing user`;
  } else {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - duplicate user correctly not added to storage`;
  }

  // call security.postNewUser with diff username and diff robust password - successful

  console.log(`\n... logging item ${++itemCounter} ................ insert New User with diff username and diff robust password - successful\n`)
  if (security.insertUser(user4, pwd4)){
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - user added sucessfully`;
  } else {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - new valid user rejected`;
  }

  console.log(`\n... logging item ${++itemCounter} ................ verify user added\n`)
  if (storageAccess.doesUserExist(user3)) {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - user exists in storage`;
  } else {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - user missing from storage`;
  }

  // verify passwords encrypted

  console.log(`\n... logging item ${++itemCounter} ................ verify user3  password encrypted\n`)
  if (pwd3 == storageAccess.getUser_RESTRICTED(user3)._password) {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - ${user3} password has not been hashed`;
  } else {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - ${user3} password has been hashed`;
  }

  console.log(`\n... logging item ${++itemCounter} ................ verify user4  password encrypted\n`)
  if (pwd4 == storageAccess.getUser_RESTRICTED(user4)._password) {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - ${user4} password has not been hashed`;
  } else {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - ${user4} password has been hashed`;
  }

  //#endregion

  //#region LOGIN - LEVEL 2

  if (runLevel > 1) {

  // call security.login with no username - reject

  console.log(`\n... logging item ${++itemCounter} ................ login with no username - reject\n`)
  const tokenA = security.loginUser(null, pwd2)
  if (tokenA) {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - logged in user without username`;
  } else {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - null username - successfully rejected`;
  }

  // call security.login with no password - reject

  console.log(`\n... logging item ${++itemCounter} ................ .login with no password - reject\n`)
  const tokenB = security.loginUser(user3, null)
  if (tokenB) {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - logged in user without password`;
  } else {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - null password - successfully rejected`;
  }

  // call security.login with user that should not exist - reject

  console.log(`\n... logging item ${++itemCounter} ................ login with user that should not exist - reject\n`)
  const tokenC = security.loginUser(user2, pwd2)
  if (tokenC) {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - logged in user who does not exist`;
  } else {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - user does not exist - successfully rejected`;
  }

  // call security.login with user exists but with wrong password - reject

  console.log(`\n... logging item ${++itemCounter} ................ login of existing user with wrong password - reject \n`)
  const tokenD = security.loginUser(user3, pwd2)
  if (tokenD) {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - logged in an existing user with invlid password`;
  } else {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - existing user with incorrect password - sucessfully rejected`;
  }

  // call security.login

  console.log(`\n... logging item ${++itemCounter} ................ login of existing user who is not currently logged in - accept \n`)
  const tokenE = security.loginUser(user3, pwd3)
  if (tokenE) {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - valid username and password - successful login`;
  } else {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - logged in user should be logged in normally`;
  }

  // call security.login

  console.log(`\n... logging item ${++itemCounter} ................ login of already logged in user - accept \n`)
  const tokenF = security.loginUser(user3, pwd3)
  if (tokenF) {
    passingCount++;
    report += `\n - Item ${itemCounter} : PASSING - valid username and password - successful login of already logged in user... options vary - other token invalidated?`;
  } else {
    issuesCount++;
    report += `\n - Item ${itemCounter} : FAILED - logged in user should be logged in normally`;
  }

  // call security.login

  }

  //#endregion

  //#region LOGOUT - LEVEL 3

  // call security.logout

  //#endregion

  //#region DATA Access - LEVEL 4

  // call fetch X

  //#endregion

  security.shutdown();
  console.log(`\n------ PASSWORD TEST FINISHED -- PASSING ${passingCount} -- FAILING ${issuesCount} ------\n\n`);
  console.log(report);
}

console.log("Running...");

main();
