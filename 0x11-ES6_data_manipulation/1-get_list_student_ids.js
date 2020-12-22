// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map

export default function getListStudentIds(objArrayStudents) {
  if (Array.isArray(objArrayStudents)){
    return objArrayStudents.map((student) => student.id);
  }
  return [];
};
