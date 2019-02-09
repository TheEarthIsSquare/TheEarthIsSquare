$(document).ready(function() {

  $(window).scroll(function(){
    var $nav = $("#navbar");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });

  // Open loading screen.
  setTimeout(function(){
      $('#loader-wrapper').addClass('loaded');
  }, 4500);

  // Navigation Menu
  $('#opener').click(function() {
    $('.nav-container').toggleClass('open');
    $('.white-logo').toggleClass('open');
    $('#opener').toggleClass('open');
    $('#particles-js').toggleClass('show');
    if($('.opener i').hasClass('fa-bars')){
      $('.opener i').removeClass('fa-bars');
      $('.opener i').addClass('fa-times');
    } else {
      $('.opener i').removeClass('fa-times');
      $('.opener i').addClass('fa-bars');
    }
  });
});
