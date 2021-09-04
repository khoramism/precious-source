$(document).ready(function() {
  "use strict";

  let rail      = $(".range-slider-container .range-rail");
  let sliderMin = $(".range-slider-container #range-slider-min");
  let sliderMax = $(".range-slider-container #range-slider-max");
  let draggedSlider;
  let mouseClickX, delta, initLeft, maxLeft, targetLeft;
  let sliderMinLeft, sliderMaxLeft;
  let overflowX = sliderMax.width() / 2;

  // const MOST_STARRED = 400e3;
  // const STAR_STEP    = 2000;
  // const WIDTH_STEP   = ( STAR_STEP / MOST_STARRED ) * rail.width();  

  // Initializing left property of sliders
  sliderMax.css({ 'left': rail.width() - overflowX });
  sliderMin.css({ 'left': -overflowX });

  $(".range-slider-container .range-slider").bind('mousedown', function(e){   
    draggedSlider = this.id === "range-slider-min" ? sliderMin : sliderMax;

    // If either of the sliders is dragged (clicked)
    // its z-index will be 2 and the other will be 1
    // so the same slider can be dragged again if they're overlaping
    draggedSlider.css({ "z-index": "2" });
    if (draggedSlider === sliderMax) sliderMin.css({ "z-index": "1" });
    else sliderMax.css({ "z-index": "1" });
    
    // mouseClickX is the x axis of mouseClick
    // initLeft is where the slider was from the beginnig
    // maxLeft is the maximum left sliders can have
    mouseClickX = e.clientX;
    initLeft    = parseInt(draggedSlider.css('left'));
    maxLeft     = rail.width() - overflowX;

    $(window).bind('mousemove', function(e){
      sliderMinLeft = parseInt(sliderMin.css('left'));
      sliderMaxLeft = parseInt(sliderMax.css('left'));

      // delta is how much mouse is moved
      // targetLeft is where the slider is about ot go (will be the value of left property)
      delta = e.clientX - mouseClickX;
      targetLeft = initLeft + delta;

      // The outer if-else checks that the min slider should always be in the left of max slider
      // Otherwise they both would be dragged together
      if ( sliderMaxLeft >= sliderMinLeft ) {
        // It checks the min and max possible value of left property
        if (Math.abs(targetLeft) <= maxLeft && targetLeft >= -overflowX) {
          draggedSlider.css({ 'left': targetLeft });
        }
      } else {
        if (draggedSlider === sliderMax) {
          sliderMin.css({ 'left': sliderMaxLeft });
        } else {
          sliderMax.css({ 'left': sliderMinLeft });
        }
      }
    });
  });
  
  // The mouseup event listener is set on window dom
  // so wherever the user releases the click
  // the the mousemove event gets unbound
  $(window).bind('mouseup', function(){

    // It ensures that the max slider is always at the right of the min slider
    setTimeout(() => {
      if (parseInt(sliderMax.css('left')) < parseInt(sliderMin.css('left'))) {
        sliderMin.css({ 'left': sliderMaxLeft });
        sliderMax.css({ 'left': sliderMinLeft });
      }
    }, 100);
    $(window).unbind('mousemove');
  });
});
