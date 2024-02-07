$(document).ready(() => {
  $('#btn_translate').click(() => {
    const languageCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, data => {
      $('#hello').text(data.hello);
    });
  });
});
