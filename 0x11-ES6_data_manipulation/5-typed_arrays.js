// http://blog.enriqueoriol.com/2016/04/novedades-es6-typed-arrays.html
export default function createInt8TypedArray(length, position, value) {
  if (position >= length) throw Error('Position outside range');
  const buffer = new ArrayBuffer(length);
  const int8View = new Int8Array(buffer);
  int8View[position] = value;
  return int8View;
}
