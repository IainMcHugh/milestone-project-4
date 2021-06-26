$.fn.isOnScreen = function(){

    var win = $(window);

    var viewport = {
        top : win.scrollTop(),
        left : win.scrollLeft()
    };
    viewport.right = viewport.left + win.width();
    viewport.bottom = viewport.top + win.height();

    var bounds = this.offset();
    bounds.right = bounds.left + this.outerWidth();
    bounds.bottom = bounds.top + this.outerHeight();

    return (!(viewport.right < bounds.left || viewport.left > bounds.right || viewport.bottom < bounds.top || viewport.top > bounds.bottom));

};

$(document).ready(() => {
    let isOpen = false;
    $('.toggle-dropdown').on('click', () => {
        if(isOpen) {
            $('.toggle-dropdown').prop('disabled', true);
            $('.fa-times').removeClass("fa-times").addClass("fa-bars");
            $('.header-dropdown').addClass('dropdown-close');
            setTimeout(() => {
                $('.header-dropdown').removeClass("dropdown-close")
                $('.header-dropdown').hide();
                $('.toggle-dropdown').prop('disabled', false);
            }, 800);
            isOpen = false;
        } else {
            $('.fa-bars').removeClass("fa-bars").addClass("fa-times"); 
            $('.header-dropdown').show();
            isOpen = true;
        }    
    });

    let isFooterVisible = false;

    $(window).scroll(function(){
        if ($('footer').isOnScreen()) {
            // The element is visible, do something
            if(!isFooterVisible){ 
                $('.sticky-buttons-wrapper').css('transform', 'translateY(56px)');
                isFooterVisible = true;
            }
        } else {
            // The element is NOT visible, do something else
            if(isFooterVisible){
                $('.sticky-buttons-wrapper').css('transform', 'translateY(0)');
                isFooterVisible = false;
            }
        }
    });
})