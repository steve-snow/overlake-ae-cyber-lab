import cmdLine
import guid
import storage
import security 

def main():
  print("\n------ PASSWORD TEST STARTING ----- PYTHON -----\n")
  passingCount = 0
  issuesCount = 0
  itemCounter = 0
  report = "Password Test Report"

  guardian = security.Security()

  runLevel = cmdLine.readCmdLine()
  print(f"::: Run Level : runLevel :::")

  #region INSERT NEW USER

  user1 = "alpha@mail.com"

  user2 = "bravo@mail.com"
  pwd2 = "123456"

  user3 = "charlie@mail.com"
  pwd3 = guid.generateGUID()
  pwd3b = guid.generateGUID()

  user4 = "delta@mail.com"
  pwd4 = guid.generateGUID()

  # const user5 = "echo@mail.com";

  # call security.postNewUser with username only - should be rejected

  itemCounter += 1
  if security.Security.insertUser(user1, None, None):
    issuesCount += 1
    report += f"\n - Item ${itemCounter} : FAILED - reported adding user without password"
  else:
    passingCount += 1
    report += f"\n - Item ${itemCounter} : PASSING - user without password blocked"
  
  if storage.Storage.doesUserExist(user1, None, None):
    issuesCount += 1
    report += f"\n - Item ${itemCounter} : FAILED - added user without password"
  else:
    passingCount += 1
    report += f"\n - Item ${itemCounter} : PASSING - user without password not added to storage"

  # call security.postNewUser with username and password - not robust enough - should be rejected

  if security.Security.insertUser(user2, pwd2):
    issuesCount += 1
    report += f"\n - Item ${itemCounter} : FAILED - password not complex enough"
  else:
    passingCount += 1
    report += f"\n - Item ${itemCounter} : PASSING - successfully rejected poor password - lacks sufficient complexity"

  if storage.Storage.doesUserExist(user2):
    issuesCount += 1
    report += f"\n - Item ${itemCounter} : FAILED - added user without password"
  else:
    passingCount += 1
    report += f"\n - Item ${itemCounter} : PASSING - user without password not added to storage"

  # call security.postNewUser with username and diff password - robust - successful

  if security.Security.insertUser(user3, pwd3):
    passingCount += 1
    report += f"\n - Item ${itemCounter} : PASSING - user added sucessfully"
  else:
    issuesCount += 1
    report += f"\n - Item ${itemCounter} : FAILED - new valid user rejected"

  if storage.Storage.doesUserExist(user3):
    passingCount += 1
    report += f"\n - Item ${itemCounter} : PASSING - user exists in storage"
  else:
    issuesCount += 1
    report += f"\n - Item ${itemCounter} : FAILED - user missing from storage"

  # call security.postNewUser with username and diff password - repeat uersname - should be rejected

  if security.Security.insertUser(user3, pwd3b):
    issuesCount += 1
    report += f"\n - Item ${itemCounter} : FAILED - new user incorrectly added when username already exists"
  else:
    passingCount += 1
    report += f"\n - Item ${itemCounter} : PASSING - user rejected because username already exists"

  if storage.Storage.doesUserExist(user3):
    issuesCount += 1
    report += f"\n - Item ${itemCounter} : FAILED - inserted new user but one already exists"
  else:
    passingCount += 1
    report += f"\n - Item ${itemCounter} : PASSING - duplicate user correctly not added to storage"

  # call security.postNewUser with diff username and diff robust password - successful

  if security.Security.insertUser(user4, pwd4):
    passingCount += 1
    report += f"\n - Item ${itemCounter} : PASSING - user added sucessfully"
  else:
    issuesCount += 1
    report += f"\n - Item ${itemCounter} : FAILED - new valid user rejected"

  if storage.Storage.doesUserExist(user3):
    passingCount += 1
    report += f"\n - Item ${itemCounter} : PASSING - user exists in storage"
  else:
    issuesCount += 1
    report += f"\n - Item ${itemCounter} : FAILED - user missing from storage"

  #endregion

  #region LOGIN - LEVEL 2

  #endregion

  #region LOGOUT - LEVEL 3

  #endregion

  #region DATA Access - LEVEL 4

  #endregion

  #region

  #endregion

  #region

  #endregion

  print(f"\n------ PASSWORD TEST FINISHED -- PASSING passingCount -- FAILING issuesCount ------\n\n")
  print(report)

if __name__ == '__main__':
  print("Running....")

  main()
