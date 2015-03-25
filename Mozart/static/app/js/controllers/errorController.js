'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.controller:errorCtrl
 * @description
 * # errorCtrl
 * Controller of the mozArtApp
 */

app.controller('errorCtrl', ['$scope', 'worksRequest', function($scope, worksRequest){
  var cantidad = 3;
  $scope.cargar = function(){
    worksRequest.randomWorks.get(
      function(obras) {
        $scope.obras = obras;
      },
      function(data, status) {
        alert('Ha fallado la petición. Estado HTTP:' + status);
      },
      'aleatorio',
      'todas',
      'todos',
      cantidad
    );
  };
  $scope.cargar();
}]);