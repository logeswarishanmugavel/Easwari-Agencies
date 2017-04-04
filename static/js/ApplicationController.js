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

    $scope.info = {};
    $scope.submissionSuccess = false;
    
    $scope.addApplication = function(){
        $http({
            method: 'POST',
            url: '/addApplication',
            data: $.param($scope.info),
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        }).then(function(response) {
            console.log($scope.info);
            console.log(response);
            $scope.formhidden = true;
            $scope.submissionSuccess = true;
            $scope.info = {};
        }, function (error) {
            console.log(error);
        });
    }
});