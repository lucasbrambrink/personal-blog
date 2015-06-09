/**
 * Created by lb on 4/20/15.
 */
function fadeTriggers() {
    return setTimeout(function() {
        $('.pt-trigger').animate({
            opacity: 0
        }, 1000)
    }, 3000);
}

$(document).ready(function() {
    // initializing page transition.
    PageTransitions.init();

    // Mouse move
    var idle = null;
    window.onload = function() {
        idle = fadeTriggers();
    };

    $(document).on('mousemove', function() {
        clearTimeout(idle);
        $('.pt-trigger').css('opacity', '1.0');
        idle = fadeTriggers();
    });

    // Arrow Keys
    var directionMap = {37: '.left', 39: '.right', 40: '.down', 38: '.top'};
    var inQueue = false;

    $("body").keydown(function(e) {
        idle = false;
        if (!inQueue) {
            if (e.keyCode <= 40 && e.keyCode >= 37) {
                var direction = directionMap[e.keyCode],
                    transition = false;

                var availableTriggers = [],
                    homeDirection = 'top';
                $('.pt-trigger').each(function(){
                    if ($(this).css('visibility') == 'visible') {
                        if (this.className.split(' ')[1] === 'home') {
                            homeDirection = "." + this.className.split(' ')[0]
                        }
                        availableTriggers.push(this.className.split(' ')[0])
                    }
                });
                for (var i = 0; i < availableTriggers.length; i++) {
                    if ("." + availableTriggers[i] == direction) {
                        transition = true;
                    }
                }
                if (transition) {
                    inQueue = true;
                    var identifier = direction == homeDirection ? '.home' : direction;
                    $(identifier).each(function() {
                        if ($(this).css('visibility') == 'visible') {
                            $(this).trigger('click');
                        }
                    });
                    setTimeout(function(){ inQueue = false}, 1000);
                }
            }
        }
    });
});
