angular.module('treehouseCourse', [])
  .controller('stageFiveCtrl', function ($scope, $http) {
    $scope.user = {
      name: "world",
      bio: ""
    };

    $http.get('markdown.md').success(function (bio) {
      $scope.user.bio = bio;
    });
  })
  .directive('hallo', function () {
    return {
      require: 'ngModel', 
      link: function ($scope, $element, $attrs, ngModelCtrl) {
        $element.hallo({
          plugins: {
            'halloformat': {},
            'halloblock': {},
            'hallojustify': {},
            'hallolists': {},
            'halloreundo': {}
          }
        });

        
        ngModelCtrl.$formatters.push(function(markdown) {
          var converter = new Showdown.converter();
          return converter.makeHtml(markdown)
        })

        ngModelCtrl.$parsers.push(function(html) {
          return toMarkdown(html)
        })


        ngModelCtrl.$render = function () {
          var contents = ngModelCtrl.$viewValue;
          $element.hallo('setContents', contents);
        }



        $element.on('hallomodified', function () {
          var contents = $element.hallo('getContents');
          ngModelCtrl.$setViewValue(contents);
          $scope.$digest();
        });
      }
    }
  });