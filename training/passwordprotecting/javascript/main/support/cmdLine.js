const readCmdLine = () => {
  const parsedCommands = [];
  const cmdLineLength = process.argv.length;

  if (cmdLineLength < 2) {
    return 1;
  }
  // console.log(process.argv);
  const runLevel = parseInt(process.argv[2]);
  // console.log("runLevel", runLevel);
  if (typeof runLevel == "number" && !isNaN(runLevel)) {
    return runLevel;
  }

  return 1;
}

export {
  readCmdLine
};
