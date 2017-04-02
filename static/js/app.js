'use strict'; 

angular.module('eaApp', [
 'ngRoute',
 'eaApp.booklist',
 'eaApp.contact'
 ]).
config(['$routeProvider',
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