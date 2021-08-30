$(document).ready(function () {
  $('#main-navbar .navbar-search-button').click(function() {
    $('#main-navbar .navbar-search-input').toggle(300);
    $('#main-navbar .navbar-search-submit').toggle(300);

    $('#main-navbar .navbar-search').hasClass('active-item')
      ? $('#main-navbar .navbar-search').removeClass('active-item')
      : $('#main-navbar .navbar-search').addClass('active-item');


    $('#main-navbar .navbar-search-button .search-icon').toggle(300);
    $('#main-navbar .navbar-search-button .close-icon').toggle(300);
  });


  document.querySelector('#main-navbar .navbar-search-input input').addEventListener('input', function (e) {
    if (e.target.value.trim() === '') {
      $("#main-navbar .navbar-search-submit button").attr('disabled');
    } else {
      $("#main-navbar .navbar-search-submit button").removeAttr('disabled');
    }
  });
});
