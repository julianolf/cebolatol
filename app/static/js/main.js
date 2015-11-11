// Assign a new service based on a resource from cebalatol API
var cebolatolServices = angular
  .module('cebolatolServices', ['ngResource'])
  .factory('Translate', ['$resource', function($resource) {
    return $resource('api/tlanslate');
  }]);

// Define app controllers
var cebolatolControllers = angular
  .module('cebolatolControllers', []);

cebolatolControllers.controller('TranslateCtrl', ['$scope', 'Translate',
  function($scope, Translate) {
    var translate = this;

    translate.send = function() {
      var translation = new Translate();
      translation.message = translate.usrText;
      translation.$save(function(response) {
        if (response.hasOwnProperty('phlase')) {
          translate.trsText = response['phlase'];
        }
      });
    };
  }
]);

cebolatolControllers.controller('ToolbarCtrl', ['$scope', '$mdDialog',
  function($scope, $mdDialog) {
    var toolbar = this;

    toolbar.about = function() {
      alert = $mdDialog.alert({
        title: 'About Cebolatol',
        content: 'Cebolatol is a simple tool to turn any text in a kind of dialect that all "r" letters are swaped to "l". It came from the funny way of speaking of a very popular character of brazilian culture, Cebolinha from Turma da Monica comic books, created by Mauricio de Sousa.',
        ok: 'Close'
      });
      $mdDialog
        .show(alert)
        .finally(function() {
               alert = undefined;
        });
    };
  }
]);

// Initializes and configure a new Angular application
var cebolatolApp = angular
  .module('cebolatol', ['ngMaterial', 'cebolatolServices', 'cebolatolControllers'])
  .config(function($mdThemingProvider) {
    $mdThemingProvider.theme('default');
  });
