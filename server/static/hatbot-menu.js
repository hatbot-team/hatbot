/**
 * Created by DKolodzey on 03.12.14.
 */
(function() {
    var app = angular.module('hatbot-menu', []);
        app.controller('menuCtrl', function() {
            this.isHidden = true;
            this.marginStyle = {'margin-left': '40px'};
            this.hide = function() {
                this.isHidden = true;
                this.marginStyle = {'margin-left': '40px'};
            };
            this.show = function() {
                this.isHidden = false;
                this.marginStyle = {'margin-left': '310px'};
            };
        });
        app.directive('hatbotMenu', function(){
            return {
                restrict: 'E',
                transclude: true,
                templateUrl: 'hatbot-menu.html',
                scope: {
                    menuCtrl : '=ctrl'
                }
            };
        });
})();