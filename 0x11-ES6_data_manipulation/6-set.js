// https://www.etnassoft.com/2016/09/13/el-objeto-set-en-javascript-los-nuevos-arrays-en-es6-teoria-ejemplos-y-rendimiento-comparado/
export default function setFromArray(arr) {
  const set = new Set(arr);
  return set;
}
