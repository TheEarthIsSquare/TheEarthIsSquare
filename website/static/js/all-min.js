$(document).ready(function(){$(window).scroll(function(){var e=$("#navbar");e.toggleClass("scrolled",$(this).scrollTop()>e.height())}),setTimeout(function(){$("#wrapper").addClass("loaded")},4500),$("#opener").click(function(){$(".nav-container").toggleClass("open"),$(".white-logo").toggleClass("open"),$("#opener").toggleClass("open"),$("#particles-js").toggleClass("show"),$(".opener i").hasClass("fa-bars")?($(".opener i").removeClass("fa-bars"),$(".opener i").addClass("fa-times")):($(".opener i").removeClass("fa-times"),$(".opener i").addClass("fa-bars"))})});