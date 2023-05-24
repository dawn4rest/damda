var posAnswers = [
  '당신은 (주제)에 대해 잘 해결하려고 하고 있군요, 그럼 앞으로 어떻게 해결할 것인지도 알려주세요.',
  '그렇군요, 당신이 생각한대로 다 잘 될 거예요. 그 생각이 변치 않고 쭉 가지고 있으면 좋겠어요.',
  '당신이 이겨내려고 하는 모습이 존경스러워요.',
  '앞으로의 당신의 모습이 무척 기대가 되는걸요.',
];
var negAnswers = [
  '당신은 지금 (주제)에 대해 많은 걱정을 하고 있군요, 그동안 힘들었겠어요. 그렇다면 앞으로 어떻게 하고 싶은지 얘기해줄래요?',
  '그런 일이 있었군요. 잘 해결하기가 어려운 부분이라 고민이 많았을 것 같아요.',
  '지금은 힘들더라도 이겨낼 수 있을거라 믿어요.',
  '이야기를 하기 까지 많은 일들이 있었겠어요, 고생이 많네요.',
];

var setPush = function() {
  var $targetEl = $('.article-body p:not(.active)');
  var time = 0;

  $targetEl.each(function() {
    var _this = $(this)
    setTimeout( function(){ 
      var type = _this.attr('class');
      new Audio(`/static/media/push_${type}.mp3`).play();
      _this.addClass('active');

      $(".article-body").animate({
        scrollTop: $('.article-body').get(0).scrollHeight
      }, 1000);
    }, time);
    time += 1000;
  });
};

$('document').ready(function() {
  setPush();

  $('.btn-submit').on('click', function () {
    $(this).css('pointer-events', 'none');
    setTimeout(function () {
      $('.btn-submit').css('pointer-events', 'auto');
    }, 1000);
    if($('.article-footer form textarea').val() === '') {
      return false;
    }

    var stage = ['feel', 'quiz', 'problem', 'face01', 'face02', 'draw'];
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
  
      setTimeout(function() {
        $.ajax({
          url: `/${curStage}-result`,
          success: function (data) {
            $('.article-body').append(data);
            setPush();
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
});