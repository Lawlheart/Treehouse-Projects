angular.module('treehouseCourse', [])
  .factory('People', ['$http', function($http) {
    var people = [];
    var otherPeople = [{
      "name": "Jane",
      "profession": "Designer",
      "hometown": "New York, NY"
    }, {
      "name": "Jerry",
      "profession": "Salesman",
      "hometown": "Detroit, MI" 
    }];
    return {
      get: function() {
        if(people.length == 0) {
          $http.get('people.json')
          .success(function(response) {
            for(var i = 0;i<response.length;i++) {
              people.push(response[i]);
            }
          });
        }
        return people;
      },
      add: function() {
        people.push(otherPeople.pop());
      },
      remove: function(person) {
        otherPeople.push(person);
        people.splice(people.indexOf(person),1);
      },
      save: function(person) {
        $http.post('people.json', person)
        .success(function() {
          alert('Saved');
        })
        .error(function(err) {
          alert(err);
        })
      }
    }
  }])
  .controller('stageThreeCtrl', function ($scope, People) {

    $scope.people = People.get();
    $scope.add = People.add;
    $scope.remove = People.remove;
    $scope.save = People.save;

    $scope.edit = function (person) {
      $scope.editingPerson = person;
    }


  });