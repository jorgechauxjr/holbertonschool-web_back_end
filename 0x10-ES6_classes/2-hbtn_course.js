export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    this._name = name;
    if (typeof length !== 'number') throw TypeError('Length must be a number');
    this._length = length;
    if (Array.isArray(students) && students.every((val) => typeof (val) === 'string')) this._students = students;
    else throw new Error(TypeError('Students must be an array of strings'));
  }

  get name() {
    return this._name;
  }

  get students() {
    return this._students;
  }

  get length() {
    return this._length;
  }

  set name(value) {
    if (typeof value !== 'string') throw TypeError('Name must be a string');
    this._length = value;
  }

  set length(value) {
    if (typeof value !== 'number') throw TypeError('Length must be a number');
    this._length = value;
  }

  set students(value) {
    if (Array.isArray(value) && value.every((v) => typeof (v) === 'string')) this._students = value;
    else throw new Error(TypeError('Students must be an array of strings'));
  }
}
