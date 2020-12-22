// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter
export default function getStudentsByLocation(studentsArray, city) {
  const arrayByCity = studentsArray.filter((student) => student.location === city);
  return arrayByCity;
}
