# Sass Notes

  - Sass can use nesting, with higher levels acting as parents of lower levels
  - using >, you can specify a direct relation
  - with &, you can include advanced nesting like so:
 			"&:hover" nested in "a" returns "a:hover"
 			"main &" nested in "div" returns "main div"
  - You can declare variables like so: 
	 		$color: #222;
	 		$variable: 5px * 2; 
	 		Variable works as expected
  - You can declare mixins like so: 
			@mixin dark_side() {
				background-color: #222;
				color: #fff; }
		  (AND ARE CALLED LIKE SO):
			@include dark_side();
  - mixins can have variables like so:
			@mixin boxy($width) {
				height: $width / 2;
				width: $width; }
		  (AND ARE CALLED LIKE SO):
			@include boxy(45px);
  - You can create custom inheritance with @extend like so:
 			.bar {
				width: 100%;
				height: 40px; }
 			.navbar {
				@extend .bar; }
  - To make artificial tags just for extend, use % like so:
 			%green {
				background-color: #242;
				color: #fff; 
				border-color: #353; }
			.navbar {
				@extend %green; }
  - Using @import, you can separate your project logically
  - Typical Layout from main.scss might be like so:
				@import "_reset.scss";
				@import "bourbon/_bourbon.scss";
				@import "_variables.scss";
				@import "_mixins.scss";
				@import "_globals.scss";
				@import "pages/home.scss";
				@import "pages/about.scss";
  - Desaturate can soften bright colors like so:
				$background: desaturate(#187, 30%);
  - Mix can combine colors like so:
 				$text-color: mix(#F00, #0F0);
  - Lighten and Darken can change the shade of colors like so:
				$highlighted-text: lighten($text-color, 20%);
				$shadowed-text: darken($text-color, 20%);
  - You can declare functions that work as expected like so:
 				@function pxify($value) {
					@return unquote($value + "px");}
  - You can nest media queries as expected, like so:
 				.content {
					.sidebar {
						color: red;
						@media screen and (max-width: 480px) {
							background-color: purple; } } }
  - Libraries like Bourbon come installed with tons of prebuilt mixins that you can use as expected by @importing them.
  - You can interpolate a variable into a string or tag like so:
  			@mixin colored-box($color) {
					.box.#{color} {
						background-color: $color;
						background-image: url("images/#{$color}.jpg");
						border-color: darken($color, 20%); } }
  - You can use if/else statements as expected, like so:
  			@mixin box($width) {
					@if $width > 100px {
						padding: 0px;
					} @else if $width == 100px {
						padding: 5px;
					}	@else {
						padding: 10px; } }
  - You can loop using numbers like so:
  			@for $i from 1 through 100 {
					.box:nth-child(#{$i}) {
						background-color: darken(white, $i); } }
	- You can loop over a list like so: 
				@each $member in thom, johnny, colin, phil {
					.bandmember.#{$member} {
						background: url("images/#{$member}.jpg"); } }
	- You can loop over an arbitrary number of inputs like so:
				@mixin band($name, $members...) {
					@each $member in $members {
						.#{$name}.#{$member} {
							background: url("images/#{$name}/#{$member}.jpg"); } } }
				(AND YOU CALL IT WITH)
				@include band(radiohead, thom, johnny, colin, phil);
 - OR, you can omit the ... and add the list space separated like so:
				@mixin band($name, $members) {
					@each $member in $members {
						.#{$name}.#{$member} {
							background: url("images/#{$name}/#{$member}.jpg"); } } }
				(AND YOU CALL IT WITH)
				@include band(radiohead, thom johnny colin phil);
  - You can also declare default values like so:
				@mixin box($size: 10px, $color: black, $display: block) {
					height: $size;
					width: $size;
					background: $color;
					display: $display; }
	- And call those values in any order by declaring them in the call:
				@include box($color: red, $display: inline, $size: 20px);