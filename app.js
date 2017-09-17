var app = angular.module('app', ['tableSort']);

app
  .controller('MainController', function MainController($scope, $http) {
    $scope.competitions = [];

    $http({
      method: 'GET',
      url: 'competitions.yaml'
    }).then(function successCallback(response) {
      $scope.competitions = jsyaml.load(response.data); // response data
    }, function errorCallback(error) {
      console.error(error);
    });
  })
  .filter('parseCurrency', function () {
    return function (input) {
      return input.replace('$', '').replace(/,/g, '');
    };
  });
