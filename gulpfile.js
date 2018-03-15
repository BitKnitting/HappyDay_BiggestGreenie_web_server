'use strict';


var gulp = require('gulp');
var svgstore = require('gulp-svgstore');
var inject = require('gulp-inject');
var debug = require('gulp-debug');

gulp.task('svgstore', function() {
  var svgs = gulp
    .src('static/img/svg/*.svg')
    .pipe(debug())
    .pipe(svgstore({
      inlineSvg: true
    }));

  function fileContents(filePath, file) {
    return file.contents.toString();
  }

  return gulp
    .src('static/img/svg/inline-svg.html')
    .pipe(inject(svgs, {
      transform: fileContents
    }))
    .pipe(gulp.dest('static/img/svg'));

});
