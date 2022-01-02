const { parse } = require("date-fns");

const date = parse("19-03-2019  16:13:33", "dd-MM-yyyy  HH:mm:ss", new Date());

console.log(date);