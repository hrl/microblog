post_img_thumbnail_width = $('.post-img-thumbnail').width();
$('.post-img-thumbnail').height(post_img_thumbnail_width);

{% jinja %}
{% for i in range( post.get_image()|length ) %}
image_set_size("post-{{post.id}}-image-thumbnail-{{i}}", post_img_thumbnail_width);
thumbnail_set_onclick("post-{{post.id}}-image-carousel", "post-{{post.id}}-image-thumbnail-{{i}}", 'post-img-thumbnail', {{i}});
carousel_set_onclick("post-{{post.id}}-image-carousel", "post-{{post.id}}-image-carousel-{{i}}", 'post-img-thumbnail')
{% endfor %}
{% endjinja %}
