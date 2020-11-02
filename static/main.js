$(document).ready(function(){
    //select first item first
    var first = $('span.flash span:first');
    var z = 1;
    var speed;
    speed= '800'; // Defult speed
    if($('span.flash').attr('data-flash-spped')){
        speed =$('span.flash').attr('data-flash-spped');
    }

    //action starts here
    window.setInterval(function(){
        var el = first;
        var next = el.next();
        if(!next.length){
            next = $('span.flash span:first');
        }
        next.css('z-index', z);
        z++;
        first = next;
    }, speed);
});