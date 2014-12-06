(function(){
    var app = angular.module('hatbot', ['hatbot-rate', 'hatbot-menu']);

    app.controller('hatbotController', function(){
        this.wordIsHidden = true;
        this.wordSource = "разработчик";
        this.word = "собака";
        this.state = "rate";
        this.wordLoadError = false;
        this.explanationsLoadError = false;
        this.explanationsOnDisplay = [];
        this.srcChoice = 'random';
        this.explanationsInMind = [
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
        this.displayOneMore = function() {
            if (this.explanationsInMind.length != 0) {
                this.explanationsOnDisplay.push(this.explanationsInMind.pop());
                this.explanationsOnDisplay[this.explanationsOnDisplay.length - 1].score = '0';
            }
        };

        this.displayAll = function() {
            while (this.explanationsInMind.length != 0) {
                this.displayOneMore();
            }
        };

        this.hideWord = function() {
            this.wordIsHidden = true;
        };
        this.showWord = function() {
            this.wordIsHidden = false;
        };

        /*
        this.play = function(srcType, givenWord) {
            var hatbot = this;
            hatbot.state = "play";
            if (srcType === 'random') {
                $http.get('/random_word').success(loadExplanations).error(raiseWordLoadError);
            } else {
                loadExplanations(givenWord);
            }
        };
        thi

        this.loadExplanations = function(word){
            hatbot.word = data;
            hatbot.wordSource = 'случайность';
            $http({ method: 'GET',
                url: '/explain_list',
                params: {word: hatbot.word}
            }).success(function(list){
                hatbot.explanationsInMind = list;
                hatbot.displayOneMore();
            }).error(raiseExplanationLoadError);
        };

        this.raiseWordLoadError = function() {
            this.word = '';
            this.wordLoadError = true;
            this.wordSource = 'ошибка';
            this.wordIsHidden = false;
        };

        this.raiseExplanationLoadError = function() {
            this.explanationsLoadError = true;
            this.wordIsHidden = false;
        };
        */
    });

    app.directive('wordInfo', function() {
        return {
            restrict: 'E',
            transclude: true,
            templateUrl: 'word-info.html',
            scope: {
                hatbot: '='
            }
        }
    });
})();
