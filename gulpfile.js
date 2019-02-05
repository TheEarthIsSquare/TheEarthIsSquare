// Include Gulp
var gulp = require('gulp');
let cleanCSS = require('gulp-clean-css');
const minify = require('gulp-minify');

// Include Our Plugins
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var autoprefixer = require('autoprefixer');
var postcss = require('gulp-postcss');

// Compile Our Sass
gulp.task('sass', function() {
  return gulp.src('website/static/scss/style.scss')
    .pipe(sass())
    .pipe(cleanCSS())
    .pipe(gulp.dest('website/static/css'));
});

// Concatenate
gulp.task('scripts', function() {
  return gulp.src('website/static/js/custom/**/*.js')
    .pipe(concat('all.js'))
    .pipe(gulp.dest('website/static/js'))
    .pipe(minify())
    .pipe(gulp.dest('website/static/js'));
});

// PostCSS processor
gulp.task('css', function () {
  var processors = [
    autoprefixer({browsers: ['last 1 version']}),
  ];
  return gulp.src('website/static/css/*.css')
    .pipe(postcss(processors))
    .pipe(gulp.dest('website/static/css'))
});

// Watch Files For Changes
gulp.task('watch', function() {
  gulp.watch('website/static/js/*.js', gulp.series('scripts'));
  gulp.watch('website/static/scss/*.scss', gulp.series('sass'));
  // gulp.watch('collection/static/css/*.css' gulp.series('css'));
});

// Default Task
gulp.task('default', gulp.series('sass', 'css', 'scripts'), 'watch');
