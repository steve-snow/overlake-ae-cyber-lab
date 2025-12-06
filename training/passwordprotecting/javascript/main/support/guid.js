import * as uuid from "uuid";

const random_uuid = uuid.v4;

/** generateGUID
 *
 * @param {number | null | undefined} count of GUID's to generate, defaults to 1
 * @returns Array of string GUIDs
 */
export default function generateGUID(count = 1) {
  //   console.log(" > FIRING >> - generateGUID", count);
  if (!count) {
    count = 1;
  }
  const result = [];
  let i = 0;
  while (i < count) {
    result.push(random_uuid());
    i++;
  }
  return result;
}
