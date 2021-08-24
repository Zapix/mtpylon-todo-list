/**
 * Waits while `func` param would not return true;
 * @param {Function<boolean>} func - function that returns boolean values
 * @param {number} refreshTime - period to check
 * @return {Promise<boolean>}
 */
export default function waitFor(func, refreshTime = 500) {
  return new Promise(resolve => {
    function checkFunc() {
      if (func()) {
        resolve(true);
      } else {
        setTimeout(checkFunc, refreshTime);
      }
    }

    checkFunc();
  });
}