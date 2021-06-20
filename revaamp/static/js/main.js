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
})