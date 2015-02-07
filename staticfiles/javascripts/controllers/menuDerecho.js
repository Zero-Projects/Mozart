/**
 * @ngdoc function
 * @name mozArtApp.controller:menuDerechoCtrl
 * @description
 * # menuDerechoCtrl
 * Controller of the mozArtApp
 */
app.controller('menuDerechoCtrl', ['$scope', function($scope){
  $scope.visible = false;
  $scope.posicion1 = {
    'right' : '-305px'
  };
  $scope.posicion2 = {
    'right' : '0'
  };
  $scope.posicionDerecha = $scope.posicion1;
  $scope.mostrarMenu= function(){
    if($scope.visible == true){
      $scope.posicionDerecha = $scope.posicion1;
      $scope.visible = false;
    }
    else{
      $scope.posicionDerecha = $scope.posicion2
      $scope.visible = true;
    }
  };
}]);
