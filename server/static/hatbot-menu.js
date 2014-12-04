/**
 * Created by DKolodzey on 03.12.14.
 */
(function() {
    var app = angular.module('hatbot-menu-module', []);
        app.directive('hatbotMenu', function(){
            return {
                restrict: 'E',
                transclude: true,
                templateUrl: 'hatbot-menu.html',
                controllerAs: 'menu',
                controller: function() {
                    this.isHidden = true;
                    this.hide = function() {
                        this.isHidden = true;
                    };
                    this.show = function() {
                        this.isHidden = false;
                    };
                }
            };
        })
})();