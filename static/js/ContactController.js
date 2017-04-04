'use strict';

angular.module('eaApp.contact', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/contact', {
    templateUrl: '/static/partials/contact.html',
    controller: 'ContactController'
  });
}])

.controller('ContactController', function($scope, $http) {
    console.log('inside ctct Ctrl');
    
    $scope.info = {};
    $scope.submissionSuccess = false;

    $scope.addInquiry = function(){
					$http({
						method: 'POST',
						url: '/addInquiry',
						data: $.param($scope.info),
						headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
					}).then(function(response) {
						console.log($scope.info);
						console.log(response);
						$scope.msghidden = true;
						$scope.submissionSuccess = true;
						$scope.info = {}
					}, function(error) {
						console.log(error);
					});
	}
});