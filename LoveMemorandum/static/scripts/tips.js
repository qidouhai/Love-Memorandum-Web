function reMasonry() {
    $('.grid').masonry({
        columnWidth: '.grid-item',
        itemSelector: '.grid-item',
        isAnimated: true
    });
}

$(function() {
    reMasonry;
    $('.grid').imagesLoaded(reMasonry);
});

$(window).resize(reMasonry);