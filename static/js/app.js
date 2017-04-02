'use strict';   // See note about 'use strict'; below

var eaApp = angular.module('eaApp', [
    'ngRoute',
]);

myApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
        when('/', {
            templateUrl: '/static/partials/index.html',
        }).
        when('/about', {
            templateUrl: '../static/partials/about.html',
        }).
        otherwise({
            redirectTo: '/'
        });
    }]);