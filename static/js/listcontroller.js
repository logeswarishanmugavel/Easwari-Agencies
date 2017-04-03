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
    $scope.data = '';

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

    $scope.getdata = function(index){
        $http({
            method: 'POST',
            url: '/getBookListData',
            data: {id:index}
        }).then(function(response) {
            $scope.data = response['data'];
            console.log($scope.data);
            console.log(response);
        }, function (error) {
            console.log(error);
        });
    }

    $scope.showlist();
});