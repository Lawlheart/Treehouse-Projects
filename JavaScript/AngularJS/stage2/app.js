angular.module('treehouseCourse', [])
  .controller('stageTwoCtrl', function ($scope) {
    $scope.user = {
      name: "guide",
      bio: "<p>A towel, The Hitchhiker's Guide to the Galaxy says, is about the most massively useful thing an interstellar hitchhiker can have. Partly it has great practical value. You can wrap it around you for warmth as you bound across the cold moons of Jaglan Beta; you can lie on it on the brilliant marble-sanded beaches of Santraginus V, inhaling the heady sea vapors; you can sleep under it beneath the stars which shine so redly on the desert world of Kakrafoon; use it to sail a miniraft down the slow heavy River Moth; wet it for use in hand-to-hand-combat; wrap it round your head to ward off noxious fumes or avoid the gaze of the Ravenous Bugblatter Beast of Traal (such a mind-boggingly stupid animal, it assumes that if you can't see it, it can't see you); you can wave your towel in emergencies as a distress signal, and of course dry yourself off with it if it still seems to be clean enough.</p>"
    };
  })
  // hallo just creates a text editor on any html element with the hallo directive ( <div hallo>, etc)
  //the methods here that we made are basically just to make hallo do what input elements ALREADY do, i.e., two way data binding
  .directive('hallo', function () {
    return {
      //require ngModel so we can use ngModelCtrl for our $render method
      require: 'ngModel', 

      //$element refers to the DOM element that has the hallo directive, and is used with jqlite, basically as a jquery element
      //$attrs holds any attributes that the hallo'ed element has
      //ngModelCtrl is a built-in controller that's main purpose is to communicate information from the scope/model to the view/page.
      link: function ($scope, $element, $attrs, ngModelCtrl) {
        //this is calling on the hallo plugin for any DOM element with the hallo directive
        $element.hallo({
          plugins: {
            //these are just very basic formatting tools, like bold and italic, so the text editor is more like what we're used to
            'halloformat': {},
            'halloblock': {}, 
            'hallojustify': {},
            'hallolists': {},
            'halloreundo': {}
          }
        });
        //we use the built-in ngModelCtrl's $render method to put the model value into the hallo'ed element
        ngModelCtrl.$render = function() {
          var contents = ngModelCtrl.$viewValue;
          $element.hallo('setContents', contents);
        }
        //this is an event handler, bound to the hallo'ed elment, that get the contents of the hallo'ed element when it changes and resets the relevant $scope value, in this case, user.bio. $scope.$digest() reloads the view, so that the new user.bio is reflected in the pre element.
        $element.on('hallomodified', function() {
          var contents = $element.hallo('getContents');
          ngModelCtrl.$setViewValue(contents);
          $scope.$digest();
        });
      }
    }
  });