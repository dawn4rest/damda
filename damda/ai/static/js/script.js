$('body').keyup(function(e){
  if (e.keyCode === 32 && $('.space-link').length) {
    window.location.href = $('.space-link').attr('href');
  }
});

$('.btn-submit').on('click', function () {
  var curStage = $('.cur-stage').text();
  var nextStage = $('.next-stage').text();

  setTimeout(function() {
    $.ajax({
      url: `/${curStage}-result`,
      success: function (data) {
        console.log(data)
        $('.article-body').append(data)
      }
    });
  
    $.ajax({
      url: `/${nextStage}-form`,
      success: function (data) {
        console.log(data)
        $('.article-footer').html(data)
      }
    });
  }, 250)
});