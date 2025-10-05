/** @jest-environment jsdom */

/** @type {import('jest').Config} */
module.exports = {
  testEnvironment: "jsdom",
  // only look for tests in static/js/__tests__ by convention
  testMatch: ["**/static/js/__tests__/trackher.test.js"],
  verbose: true,
};