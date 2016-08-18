function Masonry() {
    $('.grid').masonry({
        columnWidth: '.grid-item',
        itemSelector: '.grid-item',
        isAnimated: true
    });
}

function getContent() {
    var nextPage = parseInt($('#page').text()) + 1;
    $.get('ajax/', {
        page: nextPage,
        name: $('#name').text()
    }, function(data) {
        $('#page').text(nextPage);
        var posts = data["items"];
        var a = ""
        for (var i = 0; i <= posts.length - 1; i++) {
            var compiled = _.template('<div class="grid-item"><div class="panel panel-default"><div class="panel-heading"><h3 class="panel-title"><% if (title !== "") { %><%= title %><% } else { %>无题<% } %></h3></div><div class="panel-body <%= sender %>"><p class="info">由 <%= sender %> 于 <% print(moment(time).fromNow()); %><% if (location !== "") { %>在<span id="location"><%= location %></span><% } %>发布</p><p class="text"><%= text %></p></div><% if (url !== "") { %><div class="postPicture"><img src="<%= url %>"></div><% } %></div></div>');
            a += compiled(posts[i]);
        }
        $(".grid").html($(".grid").html() + a);
        $('.grid').masonry('destroy');
        $('.grid').imagesLoaded(Masonry);
        getAddresses();
    });
}
$(function() {
    $('.JSNotice').addClass('hide');
    $('.Pager').addClass('hide');
    $('#load').removeClass('hide');
    $('.grid').imagesLoaded(Masonry);
    getAddresses();
    $(window).resize(Masonry);
});