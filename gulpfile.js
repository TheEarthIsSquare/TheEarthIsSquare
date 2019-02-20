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
gulp.task('Website SCSS', function() {
  return gulp.src('website/static/website/scss/style.scss')
    .pipe(sass())
    .pipe(cleanCSS())
    .pipe(gulp.dest('website/static/website/css'));
});

gulp.task('Dashboard SCSS', function() {
  return gulp.src('dashboard/static/dashboard/scss/style.scss')
    .pipe(sass())
    .pipe(cleanCSS())
    .pipe(gulp.dest('dashboard/static/dashboard/css'));
});

// Concatenate
gulp.task('Website Scripts', function() {
  return gulp.src('website/static/website/js/custom/*.js')
    .pipe(concat('all.js'))
    .pipe(gulp.dest('website/static/website/js'))
    .pipe(minify())
    .pipe(gulp.dest('website/static/website/js'));
});

// PostCSS processor
gulp.task('Website CSS', function () {
  var processors = [
    autoprefixer({browsers: ['last 1 version']}),
  ];
  return gulp.src('website/static/website/css/*.css')
    .pipe(postcss(processors))
    .pipe(gulp.dest('website/static/website/css'))
});

// Default Task
gulp.task('default', gulp.series('Website SCSS', 'Dashboard SCSS', 'Website CSS', 'Website Scripts'));
