/**
 * Created by DKolodzey on 05.12.14.
 */
(function() {
    var app = angular.module('hatbot-rate', []);

    app.directive('hatbotRateRadio', function(){
        return {
            restrict: 'E',
            templateUrl: 'hatbot-rate-radio.html',
            scope: {
                score: '='
            },
            controller: function() {
                this.textScore = {
                    '-2': 'Ужасно, это вообще не объяснение!',
                    '-1': 'Плохо, объяснение нарушает правила шляпы',
                    '0': 'Так себе, но вполне корректно',
                    '1': 'Хорошо, но можно лучше',
                    '2': 'Отлично, я сразу понял!'
                };
            },
            controllerAs: 'scoreCtrl'
        }
    });

    app.directive('hatbotRate', function(){
        return {
            restrict: 'E',
            templateUrl: 'hatbot-rate.html',
            scope: {
                hatbot: '='
            }
        }
    });
})();