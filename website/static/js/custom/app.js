$(document).ready(function() {

  // Show navbar background on scroll.
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

  // Contact Form
  $('#contact-why .coffee').click(function() {
    $('#contact-why-wrapper').toggleClass('hide');
    $('#contact-form-coffee').toggleClass('show');
  });

  $('#contact-why .work').click(function() {
    $('#contact-why-wrapper').toggleClass('hide');
    $('#contact-why-wrapper').removeClass('fade');
    $('#contact-form-work').toggleClass('show');
  });

  $('#contact-why .other').click(function() {
    $('#contact-why-wrapper').toggleClass('hide');
    $('#contact-why-wrapper').toggleClass('fade');
    $('#contact-form-other').toggleClass('show');
  });

  $('#contact-form-coffee #contact-go-back').click(function() {
    $('#contact-why-wrapper').toggleClass('hide');
    $('#contact-form-coffee').toggleClass('show');
  });

  $('#contact-form-work #contact-go-back').click(function() {
    $('#contact-why-wrapper').toggleClass('hide');
    $('#contact-why-wrapper').toggleClass('fade');
    $('#contact-form-work').toggleClass('show');
  });

  $('#contact-form-other #contact-go-back').click(function() {
    $('#contact-why-wrapper').toggleClass('hide');
    $('#contact-why-wrapper').toggleClass('fade');
    $('#contact-form-other').toggleClass('show');
  });

});
