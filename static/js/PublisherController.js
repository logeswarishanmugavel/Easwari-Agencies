'use strict';

angular.module('eaApp.publist', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/publist', {
    templateUrl: '/static/partials/publishers.html',
    controller: 'PublisherController'
  });
}])

.controller('PublisherController', function( $scope, $http ) {
    console.log('inside pub Ctrl');
    $scope.showpublist = function(){
        $http({
            method: 'POST',
            url: '/getPubList',
        }).then(function(response) {
            $scope.pubs = response.data;
            console.log('pubs',$scope.pubs);
        }, function (error) {
            console.log(error);
        });
    }
    $scope.showpublist();
});