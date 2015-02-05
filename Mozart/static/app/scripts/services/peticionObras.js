'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.service:peticionObras
 * @description
 * #peticionObras
 * Service of the mozArtApp
 */

app.service('peticionObras', ['$http',  function($http){
  this.get=function(fnOK,fnError, modo, categoria, autor, cantidad) {
    $http({
      method: 'GET',
      url: 'data/obras' + cantidad + '.json'
    })
    .success(function(data, status, headers, config) {
      fnOK(data);
    })
    .error(function(data, status, headers, config) {
      fnError(data,status);
    });
  };
}]);
