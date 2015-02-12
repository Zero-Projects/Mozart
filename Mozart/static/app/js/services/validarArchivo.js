'use strict';

/**
 * @ngdoc function
 * @name mozArtApp.service:validateFile
 * @description
 * # validateFile
 * Service of the mozArtApp
 */

app.service('validateFile', function(){
  this.getExtension = function(fileObject){
    var divisions = fileObject.name.split('.');
    var fileExtension = divisions[divisions.length -1];
    return fileExtension;
  };
  this.validateFormat = function(fileExtension){
    var validFormats = ['pdf', 'mp3', 'aac', 'wma', 'mp4', 'mpeg', 'avi', '3gp'];
    for(var i = 0; i < validFormats.length; i++){
      if(fileExtension == validFormats[i]){
        return true;
      }
    }
    return false;
  };
  this.isAnImage = function(fileExtension){
    var imageFormats = ['png', 'gif', 'jpg', 'jpeg', 'bmp', 'tiff'];
    for(var i = 0; i < imageFormats.length; i++){
      if(fileExtension == imageFormats[i]){
        return true;
      }
    }
    return false;
  };
});