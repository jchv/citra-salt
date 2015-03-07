var app = angular.module('LoginApp', ['ui.bootstrap']);

app.config(function($httpProvider) {
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
});

app.controller('LoginCtrl', function($scope, $http, $window, $location) {
    $scope.credentials = {
        username: '',
        password: ''
    };
    $scope.logIn = (function() {
        $http.post('/api/account/login/', $scope.credentials)
            .success(function(data, status, headers, config) {
                if ($location.search().next)
                    $window.location.href = $location.search().next;
                else
                    $window.location.href = '/';
            })
            .error(function(data, status, headers, config) {

            });
    });
});
