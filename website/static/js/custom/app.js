$(document).ready(function() {

  setTimeout(function(){
      $('body').addClass('loaded');
  }, 4500);

  $('#opener').click(function() {
    console.log('click has worked');
    $('.nav-container').toggleClass('open');
    $('.white-logo').toggleClass('open');
    if($('.opener i').hasClass('fa-bars')){
      console.log('has bars');
      $('.opener i').removeClass('fa-bars');
      $('.opener i').addClass('fa-times');
    } else {
      console.log('no bars');
      $('.opener i').removeClass('fa-times');
      $('.opener i').addClass('fa-bars');
    }
  });
});

/* particlesJS.load(@dom-id, @path-json, @callback (optional)); */
particlesJS.load('particles-js', 'static/js/custom/particles/particles.json', function() {
  console.log('callback - particles.js config loaded');
});
