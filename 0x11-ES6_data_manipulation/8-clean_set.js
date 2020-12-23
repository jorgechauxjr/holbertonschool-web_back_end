export default function cleanSet(set, startString) {
  let str = '';
  if (typeof (startString) === 'string' && startString !== '') {
    set.forEach((val) => {
      if (val.includes(startString)) str = str.concat(`-${val.replace(startString, '')}`);
    });
    str = str.substring(1);
  }
  return str;
}
