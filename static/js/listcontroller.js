'use strict';

angular.module('eaApp.booklist', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/booklist', {
    templateUrl: '/static/partials/booklist.html',
    controller: 'ListCtrl'
  });
}])

.controller('ListCtrl', function( $scope, $http ) {
    console.log('insideCtrl');
    $scope.showlist = function(){
        $http({
            method: 'POST',
            url: '/getBookList',
        }).then(function(response) {
            $scope.books = response.data;
            console.log('books',$scope.books);
        }, function (error) {
            console.log(error);
        });
    }
    $scope.showlist();
});