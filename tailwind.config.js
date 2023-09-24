/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/login.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

