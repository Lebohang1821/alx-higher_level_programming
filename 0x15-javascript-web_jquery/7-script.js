$(document).ready(() => {
  $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", data => $('#character').text(data.name));
});
