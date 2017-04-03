'use strict';

angular.module('eaApp.appform', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/application', {
    templateUrl: '/static/partials/application.html',
    controller: 'ApplicationController'
  });
}])

.controller('ApplicationController', function( $scope, $http ) {
    console.log('inside appl Ctrl');
    $scope.addapplication = function(){
        $http({
            method: 'POST',
            url: '/addapplication',
        }).then(function(response) {
            $scope.pubs = response.data;
            console.log('pubs',$scope.pubs);
        }, function (error) {
            console.log(error);
        });
    }
});