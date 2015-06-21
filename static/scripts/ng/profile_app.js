
var app = angular.module('profile-app', [])

app.service('ProfileService', function($http) {
	this.fetch = function() {
		return $http.get('/api/profile');
	}
})

app.controller('ProfileController', function($scope, ProfileService) {
	$scope.username = {'username': 'Will Redington'};
})

