(function(){
  var app = angular.module('hatbot', []);
  app.controller('HatbotController', ['$http', function($http){
    this.state = 'hat-index';
    this.word = 'собака';
    this.wordIsHidden = true;
    this.nShown = 1;
    this.explanations = [
      { text: '*пропуск* на сене',
          id: '1358'},
      { text: 'синоним к словам шавка, дворняга',
          id: '1359'},
      { text: 'домашнее животное семейства псовых',
          id: '1360'},
      { text: 'Блохастое домашнее животное Блохастое домашнее животное Блохастое домашнее животное Блохастое домашнее животное Блохастое домашнее животное Блохастое домашнее животное Блохастое домашнее животное Блохастое домашнее животное Блохастое домашнее животное Блохастое домашнее животное',
          id: '1361'},
      { text: 'питомец собаковода',
          id: '1362'},
      { text: 'см. *пропуск*',
          id: '1363'}
    ];
    this.ratedExplanations = [];
    this.textRate = {
      '-2': 'Ужасно, это вообще не объяснение!',
      '-1': 'Плохо, объяснение нарушает правила шляпы',
       '0': 'Так себе, но вполне корректно',
       '1': 'Хорошо, но можно лучше',
       '2': 'Отлично, я сразу понял!',
    };
    
    this.showMore = function(){
      this.ratedExplanations.push(this.explanations[this.nShown]);
      this.ratedExplanations[this.nShown].score = '0';
      this.nShown = this.nShown + 1;
    };

    this.showAll = function(){
      while(this.nShown < this.explanations.length)
        this.showMore();
    };
    this.rateRandom = function(){
      var hatbot = this;
      this.state = 'hat-rate';
      this.wordIsHidden = true;
      this.nShown = 0;
      this.ratedExplanations = [];
      $http.get('/random_word').success(function(data){
        hatbot.word = data;
        $http({ method: 'GET',
                   url: '/explain_list',
                  params: {word: hatbot.word},
                  }).success(function(list){
          hatbot.explanations = list;
          hatbot.showMore();
        });
      });
    };

    this.sendRating = function(e) {
        var data = { result: e.score,
                         id: e.id
                   };
        
        //заглушка, а вообще статистику хочется обсудить
        switch(e.score) {
          case '-2':
          case '-1':
            data.result = 'BLAME';
            break;
          case '2':
          case '1':
            data.result = 'SUCCESS';
            break;
          case '0':
            data.result = 'FAIL';
            break;
        }
        //конец заглушки

        $http({  method: 'POST',
                    url: '/statistics/update',
                headers: { 'Content-Type': 'application/json'
                              },
                data: JSON.stringify(data),
               });  
    };

    this.sendRatingAndRateRandom = function(){
      for (var i = 0; i < this.ratedExplanations.length; i++)
      {
        this.sendRating(this.ratedExplanations[i]);
      }
      this.rateRandom();
    };    
  }]);
})();