$(document).ready(() => {
  $('#add_item').click(() => {
    $('<li>Item</li>').appendTo('ul.my_list');
  });

  $('#remove_item').click(() => {
    $('ul.my_list li:last-child').remove();
  });

  $('#clear_list').click(() => {
    $('ul.my_list').empty();
  });
});
