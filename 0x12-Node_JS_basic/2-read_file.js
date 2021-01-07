const fs = require('fs');

function countStudents(path) {
  if (!fs.existsSync(path)) throw Error('Cannot load the database'); // validate if  file exist

  try {
    const inFields = {}; // {field: {counter: # of students, students: [list of students in field]}}
    const content = fs.readFileSync(path, 'utf-8').split('\n');

    for (let i = 1; i < content.length; i += 1) {
      const line = content[i].split(','); // get each word
      if (inFields[line[3]]) { // line[3] is the field name
        inFields[line[3]].counter += 1;
        inFields[line[3]].students.push(` ${line[0]}`); // line[0] is firstname
      } else {
        inFields[line[3]] = { counter: 1, students: [`${line[0]}`] };
      }
    }
    console.log(`Number of students: ${content.length - 1}`);
    for (const key in inFields) {
      if (Object.prototype.hasOwnProperty.call(inFields, key)) {
        console.log(`Number of students in ${key}: ${inFields[key].counter}. List: ${inFields[key].students}`);
      }
    }
  } catch (e) {
    throw Error(e);
  }
}
module.exports = countStudents;
