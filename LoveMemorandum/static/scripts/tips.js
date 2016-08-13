var page = 1,
    name = "all";

function Masonry() {
    $('.grid').masonry({
        columnWidth: '.grid-item',
        itemSelector: '.grid-item',
        isAnimated: true
    });
}

function getContent(page, name) {
    $.get('ajax/', {
        p: page,
        name: name
    }, function(data, status) {
        if status
        posts = data["items"];
        a = ""
        for (var i = 0; i <= posts.length - 1; i++) {
            var compiled = _.template('<div class="grid-item"><div class="panel panel-default"><div class="panel-heading"><h3 class="panel-title"><% if (title !== "") { %><%= title %><% } else { %>无题<% } %></h3></div><div class="panel-body <%= sender %>"><p class="info">由 <%= sender %> 在 <% print(moment(time).fromNow()); %>发布。</p><p class="text"><%= text %></p></div><% if (url !== "") { %><div class="postPicture"><img src="<%= url %>"></div><% } %></div></div>');
            a += compiled(posts[i]);
        }
        $(".grid").html(a);
        $('.grid').imagesLoaded(Masonry);
    });
}
$(function() {
    $('.JSNotice').hide();
    $('.grid').imagesLoaded(Masonry);
    $(window).resize(Masonry);
});