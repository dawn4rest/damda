$('body').keyup(function(e){
  if (e.keyCode === 32 && $('.space-link').length) {
    window.location.href = $('.space-link').attr('href');
  }
});
