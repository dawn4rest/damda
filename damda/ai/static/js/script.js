$('.btn-submit').on('click', function () {
  var stage = ['feel','problem','face01','face02','quiz-01','draw','quiz-02','quiz-03','quiz-04','quiz-05','quiz-06','quiz-07','quiz-08','quiz-09','quiz-10'];
  var curStage = $('form').attr('action').match(/\/([^-]+)/)[1];
  var nextStage = stage[stage.indexOf(curStage) + 1]
  console.log(nextStage);

  if(jQuery.inArray(curStage, stage) !== -1) {
    setTimeout(function() {
      $.ajax({
        url: `/${curStage}-result`,
        success: function (data) {
          $('.article-body').append(data)
        }
      });
    
      $.ajax({
        url: `/${nextStage}-form`,
        success: function (data) {
          $('.article-footer').html(data)
        }
      });
    }, 250);
  };
});