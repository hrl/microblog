{% jinja %}
{% for i in range(posts.count()) %}
{% set post = posts[i] %}


post_img_thumbnail_width = $('.post-img-thumbnail').width();
$('.post-img-thumbnail').height(post_img_thumbnail_width);

{% for i in range( post.get_image()|length ) %}
image_set_size("post-{{post.id}}-image-thumbnail-{{i}}", post_img_thumbnail_width);
thumbnail_set_onclick("post-{{post.id}}-image-carousel", "post-{{post.id}}-image-thumbnail-{{i}}", 'post-{{post.id}}-img-thumbnail', {{i}});
carousel_set_onclick("post-{{post.id}}-image-carousel", "post-{{post.id}}-image-carousel-{{i}}", 'post-{{post.id}}-img-thumbnail')
{% endfor %}

$('#post-{{post.id}}-like')[0].onclick = function(){like('post-{{post.id}}-like', "post-{{post.id}}-unlike", "post", {{post.id}});}
$('#post-{{post.id}}-unlike')[0].onclick = function(){unlike('post-{{post.id}}-like', "post-{{post.id}}-unlike", "post", {{post.id}});}

$('#post-{{post.id}}-collect')[0].onclick = function(){collect('post-{{post.id}}-collect', 'post-{{post.id}}-uncollect', "post", {{post.id}});}
$('#post-{{post.id}}-uncollect')[0].onclick = function(){uncollect('post-{{post.id}}-collect', 'post-{{post.id}}-uncollect', "post", {{post.id}});}
{% if post.user == user %}
$('#post-{{post.id}}-delete')[0].onclick = function(){del_post("{{post.id}}");}
{% endif %}
//repo
{% if post.repo %}
{% if post.repo.is_active %}
post_repo_img_thumbnail_width = $('.post-repo-img-thumbnail').width();
$('.post-repo-img-thumbnail').height(post_repo_img_thumbnail_width);
{% for i in range( post.repo.get_image()|length ) %}
image_set_size("post-{{post.id}}-repo-{{post.repo.id}}-image-thumbnail-{{i}}", post_repo_img_thumbnail_width);
thumbnail_set_onclick("post-{{post.id}}-repo-{{post.repo.id}}-image-carousel", "post-{{post.id}}-repo-{{post.repo.id}}-image-thumbnail-{{i}}", 'post-{{post.id}}-repo-{{post.repo.id}}-img-thumbnail', {{i}});
carousel_set_onclick("post-{{post.id}}-repo-{{post.repo.id}}-image-carousel", "post-{{post.id}}-repo-{{post.repo.id}}-image-carousel-{{i}}", 'post-{{post.id}}-repo-{{post.repo.id}}-img-thumbnail')
{% endfor %}


$('#post-{{post.id}}-repo-{{post.repo.id}}-like')[0].onclick = function(){like('post-{{post.id}}-repo-{{post.repo.id}}-like', "post-{{post.id}}-repo-{{post.repo.id}}-unlike", "post", {{post.repo.id}});}
$('#post-{{post.id}}-repo-{{post.repo.id}}-unlike')[0].onclick = function(){unlike('post-{{post.id}}-repo-{{post.repo.id}}-like', "post-{{post.id}}-repo-{{post.repo.id}}-unlike", "post", {{post.repo.id}});}

$('#post-{{post.id}}-repo-{{post.repo.id}}-collect')[0].onclick = function(){collect('post-{{post.id}}-repo-{{post.repo.id}}-collect', 'post-{{post.id}}-repo-{{post.repo.id}}-uncollect', "post", {{post.repo.id}});}
$('#post-{{post.id}}-repo-{{post.repo.id}}-uncollect')[0].onclick = function(){uncollect('post-{{post.id}}-repo-{{post.repo.id}}-collect', 'post-{{post.id}}-repo-{{post.repo.id}}-uncollect', "post", {{post.repo.id}});}
{% endif %}
{% endif %}

{% endfor %}



{% if max_page %}
	{% if page > 2 %}
	$('#posts-page-{{page-2}}')[0].onclick = function(){load_posts("{{post_type}}", "{{post_information}}", "{{page-2}}", "posts");}
	{% endif %}
	{% if page > 1 %}
	$('#posts-page-{{page-1}}')[0].onclick = function(){load_posts("{{post_type}}", "{{post_information}}", "{{page-1}}", "posts");}
	{% endif %}
	//$('#posts-page-{{page}}')[0].onclick = function(){load_posts("{{post_type}}", "{{post_information}}", "{{page}}", "posts");}
	{% if page < max_page %}
	$('#posts-page-{{page+1}}')[0].onclick = function(){load_posts("{{post_type}}", "{{post_information}}", "{{page+1}}", "posts");}
	{% endif %}
	{% if page+1 < max_page %}
	$('#posts-page-{{max_page}}')[0].onclick = function(){load_posts("{{post_type}}", "{{post_information}}", "{{max_page}}", "posts");}
	{% endif %}
{% endif %}

$('#check_posts-a')[0].onclick = function(){load_posts("{{post_type}}", "{{post_information}}", "1", "posts");}
function check_post(){
	$.get('/check/post?date={{date}}', function(data,status){
		if (status == 'success'){
			count = Number(data)
			if (count > 0){
				$('#check_posts').show();
				clearInterval(check_post_timer);
			}
		}
	});
}
check_post_timer = setInterval(check_post, 10000);
{% endjinja %}
