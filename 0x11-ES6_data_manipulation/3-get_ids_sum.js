// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce
export default function getStudentIdsSum(studentsArray) {
  const reducer = (accumulator, currentValue) => accumulator + currentValue.id;
  const idSum = studentsArray.reduce(reducer, 0);
  return idSum;
}
