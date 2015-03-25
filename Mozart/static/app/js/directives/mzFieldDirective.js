'use strict';
/**
* @ngdoc function
* @name mozArtApp.directive:mzField
* @description
* # mzField
*
* Directive of the mozArtApp.
*/

app.directive('mzField', [function(){
  return {
    restrict: 'A',
    scope: false,
    transclude: false,
    link: function(scope, elem, attrs){
    	elem.focus(function(){
       	elem.prev('label').removeClass('initial-label');
       	elem.prev('label').addClass('active-label');
       	elem.removeClass('empty-initial-field'); 
       	elem.addClass('active-field');
    	});
    	elem.blur(function(){
       	if(elem.val()==''){
       	  elem.removeClass('active-field');
       	  elem.addClass('empty-initial-field'); 
       	}
       	elem.prev('label').removeClass('active-label');
       	elem.prev('label').addClass('initial-label');
    	});
    }
  }
}]);
