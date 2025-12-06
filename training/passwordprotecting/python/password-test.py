import cmdLine
import guid
from storage import Storage
from security import Security

def main():
  print("\n------ PASSWORD TEST STARTING ----- PYTHON -----\n")
  passingCount = 0
  issuesCount = 0
  itemCounter = 0
  report = "Password Test Report"

  guardian = ()

  runLevel = cmdLine.readCmdLine()
  print(f"::: Run Level : runLevel :::")

  #region INSERT NEW USER

  user1 = "alpha@mail.com"
  print(f"  1   {user1}  {None}")

  user2 = "bravo@mail.com"
  pwd2 = "123456"
  print(f"  2   {user2}  {pwd2}")

  user3 = "charlie@mail.com"
  pwd3 = guid.generateGUID()
  print(f"  3   {user3}  {pwd3}")
  pwd3b = guid.generateGUID()
  print(f"  3b  {user3}  {pwd3b}")

  user4 = "delta@mail.com"
  pwd4 = guid.generateGUID()
  print(f"  4   {user4}  {pwd4}")

  # user5 = "echo@mail.com";

  # call postNewUser with username only - should be rejected

  itemCounter += 1
  print(f"\n... logging item {itemCounter} ................ insert New User with username only - should be rejected\n")
  if Security.insertUser(user1, None, None):
    issuesCount += 1
    report += f"\n - Item {itemCounter} : FAILED - reported adding user without password"
  else:
    passingCount += 1
    report += f"\n - Item {itemCounter} : PASSING - user without password blocked"
  
  itemCounter += 1
  print(f"\n... logging item {itemCounter} ................ verify user NOT added \n")
  if Storage.doesUserExist(user1):
    issuesCount += 1
    report += f"\n - Item {itemCounter} : FAILED - added user without password"
  else:
    passingCount += 1
    report += f"\n - Item {itemCounter} : PASSING - user without password not added to storage"

  # call postNewUser with username and password - not robust enough - should be rejected

  itemCounter += 1
  print(f"\n... logging item {itemCounter} ................ insert New User with username and password - not robust enough - should be rejected\n")
  if Security.insertUser(user2, pwd2):
    issuesCount += 1
    report += f"\n - Item {itemCounter} : FAILED - password not complex enough"
  else:
    passingCount += 1
    report += f"\n - Item {itemCounter} : PASSING - successfully rejected poor password - lacks sufficient complexity"

  itemCounter += 1
  print(f"\n... logging item {itemCounter} ................ verify user NOT added \n")
  if Storage.doesUserExist(user2):
    issuesCount += 1
    report += f"\n - Item {itemCounter} : FAILED - added user without password"
  else:
    passingCount += 1
    report += f"\n - Item {itemCounter} : PASSING - user without password not added to storage"

  # call postNewUser with username and diff password - robust - successful

  itemCounter += 1
  print(f"\n... logging item {itemCounter} ................ insert New User with username and good password - robust - successful\n")
  if Security.insertUser(user3, pwd3):
    passingCount += 1
    report += f"\n - Item {itemCounter} : PASSING - user added sucessfully"
  else:
    issuesCount += 1
    report += f"\n - Item {itemCounter} : FAILED - new valid user rejected"

  itemCounter += 1
  print(f"\n... logging item {itemCounter} ................ verify user added\n")
  if Storage.doesUserExist(user3):
    passingCount += 1
    report += f"\n - Item {itemCounter} : PASSING - user exists in storage"
  else:
    issuesCount += 1
    report += f"\n - Item {itemCounter} : FAILED - user missing from storage"

  # call postNewUser with username and diff password - repeat uersname - should be rejected

  itemCounter += 1
  print(f"\n... logging item {itemCounter} ................ insert New User with repeat username and diff password - should be rejected\n")
  if Security.insertUser(user3, pwd3b):
    issuesCount += 1
    report += f"\n - Item {itemCounter} : FAILED - new user incorrectly added when username already exists"
  else:
    passingCount += 1
    report += f"\n - Item {itemCounter} : PASSING - user rejected because username already exists"

  itemCounter += 1
  print(f"\n... logging item {itemCounter} ................ verify no duplicate exists for username\n")
  if Storage.doesUserExist(user3):
    issuesCount += 1
    report += f"\n - Item {itemCounter} : FAILED - inserted new user but that user already exists"
  else:
    passingCount += 1
    report += f"\n - Item {itemCounter} : PASSING - duplicate user correctly not added to storage"

  # call postNewUser with diff username and diff robust password - successful

  itemCounter += 1
  print(f"\n... logging item {itemCounter} ................ insert New User with diff username and diff robust password - successful\n")
  if Security.insertUser(user4, pwd4):
    passingCount += 1
    report += f"\n - Item {itemCounter} : PASSING - user added sucessfully"
  else:
    issuesCount += 1
    report += f"\n - Item {itemCounter} : FAILED - new valid user rejected"

  itemCounter += 1
  print(f"\n... logging item {itemCounter} ................ verify user added\n")
  if Storage.doesUserExist(user3):
    passingCount += 1
    report += f"\n - Item {itemCounter} : PASSING - user exists in storage"
  else:
    issuesCount += 1
    report += f"\n - Item {itemCounter} : FAILED - user missing from storage"

  #endregion

  #region LOGIN - LEVEL 2

  if (runLevel > 1):

  # call login with no username - reject

    itemCounter += 1
    print(f"\n... logging item {itemCounter} ................ login with no username - reject\n")
    tokenA = Security.loginUser(None, pwd2)
    if (tokenA):
      issuesCount += 1
      report += f"\n - Item {itemCounter} : FAILED - logged in user without username"
    else:
      passingCount += 1
      report += f"\n - Item {itemCounter} : PASSING - None username - successfully rejected"


    # call login with no password - reject

    itemCounter += 1
    print(f"\n... logging item {itemCounter} ................ .login with no password - reject\n")
    tokenB = Security.loginUser(user3, None)
    if (tokenB):
      issuesCount += 1
      report += f"\n - Item {itemCounter} : FAILED - logged in user without password"
    else:
      passingCount += 1
      report += f"\n - Item {itemCounter} : PASSING - None password - successfully rejected"


    # call login with user that should not exist - reject

    itemCounter += 1
    print(f"\n... logging item {itemCounter} ................ login with user that should not exist - reject\n")
    tokenC = Security.loginUser(user2, pwd2)
    if (tokenC):
      issuesCount += 1
      report += f"\n - Item {itemCounter} : FAILED - logged in user who does not exist"
    else:
      passingCount += 1
      report += f"\n - Item {itemCounter} : PASSING - user does not exist - successfully rejected"


    # call login with user exists but with wrong password - reject

    itemCounter += 1
    print(f"\n... logging item {itemCounter} ................ login of existing user with wrong password - reject \n")
    tokenD = Security.loginUser(user3, pwd2)
    if (tokenD):
      issuesCount += 1
      report += f"\n - Item {itemCounter} : FAILED - logged in an existing user with invlid password"
    else:
      passingCount += 1
      report += f"\n - Item {itemCounter} : PASSING - existing user with incorrect password - sucessfully rejected"


    # call login

    itemCounter += 1
    print(f"\n... logging item {itemCounter} ................ login of existing user who is not currently logged in - accept \n")
    tokenE = Security.loginUser(user3, pwd3)
    if (tokenE):
      passingCount += 1
      report += f"\n - Item {itemCounter} : PASSING - valid username and password - successful login"
    else:
      issuesCount += 1
      report += f"\n - Item {itemCounter} : FAILED - logged in user should be logged in normally"


    # call login

    itemCounter += 1
    print(f"\n... logging item {itemCounter} ................ login of already logged in user - accept \n")
    tokenF = Security.loginUser(user3, pwd3)
    if (tokenF):
      passingCount += 1
      report += f"\n - Item {itemCounter} : PASSING - valid username and password - successful login of already logged in user... options vary - other token invalidated?"
    else:
      issuesCount += 1
      report += f"\n - Item {itemCounter} : FAILED - logged in user should be logged in normally"

  #endregion

  #region LOGOUT - LEVEL 3

  #endregion

  #region DATA Access - LEVEL 4

  #endregion

  #region

  #endregion

  #region closeout

  Security.shutdown()

  #endregion

  print(f"\n------ PASSWORD TEST FINISHED -- PASSING passingCount -- FAILING issuesCount ------\n\n")
  print(report)

if __name__ == '__main__':
  print("Running....")

  main()
