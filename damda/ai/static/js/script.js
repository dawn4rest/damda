$('.btn-submit').on('click', function () {
  var stage = ['feel','quiz','problem','face01','face02','draw'];
  var curStage = $('form').attr('action').match(/\/([^-]+)/)[1];
  var nextStage = stage[stage.indexOf(curStage) + 1];

  if(jQuery.inArray(curStage, stage) !== -1) {
    if (curStage.indexOf('quiz') != -1) {
      if (quizStage > 9) {
        nextStage = 'problem';
      } else {
        nextStage = 'quiz';
      }
    }

    console.log(curStage);
    console.log(nextStage);

    setTimeout(function() {
      $.ajax({
        url: `/${curStage}-result`,
        success: function (data) {
          $('.article-body').append(data);
        }
      });
    
      $.ajax({
        url: `/${nextStage}-form`,
        success: function (data) {
          $('.article-footer').html(data);
        }
      });

      $(".article-body").animate({
        scrollTop: $('.article-body').get(0).scrollHeight
      }, 500);
    }, 250);
  };
});