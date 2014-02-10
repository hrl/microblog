{% for inform in user.information.all %}
$("#inform-{{inform.id}}")[0].onclick = function(){
	{% if inform.inform_type == 0 or inform.inform_type == 2 %}
	window.open('/post/{{inform.body}}');
	{% elif inform.inform_type == 1 %}
	window.open('/post/{{inform.get_target.post.id}}#comment-{{inform.get_target.id}}');
	{% endif %}
	del_inform("{{inform.id}}");
	load_inform();
}
{% endfor %}
