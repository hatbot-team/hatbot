(function(){
    var app = angular.module('hatbot', ['hatbot-menu-module']);

    app.controller('hatbotCtrl', function(){
        this.wordIsHidden = true;
        this.wordSource = "Пользователь";
        this.word = "рыба";
        this.hideWord = function() {
            this.wordIsHidden = true;
        };
        this.showWord = function() {
            this.wordIsHidden = false;
        };
    });



    app.directive('wordInfo', function() {
        return {
            restrict: 'E',
            transclude: true,
            templateUrl: 'word-info.html',
            scope: {
                source: '='
            }
        }
    });
})();
