// «Липкий» код
$(function(){
  $.fn.followTo = function (pos) {
    var $this = this,
        $window = $(window);

    $window.scroll(function (e) {
        if ($window.scrollTop() > pos) {
            $this.css({
                position: 'fixed',
                top: 20,
                right: 20
            });
        } else {
            $this.css({
                position: 'absolute',
                top: 120
            });
        }
    });
};

$('.float-block').followTo(140);
});