function image_set_size(image_id, size){
	width = $('#'+image_id).width();
	height = $('#'+image_id).height();
	if (width < height){
		$('#'+image_id).height(size);
	}
	else{
		$('#'+image_id).width(size);
		vertical_margin = (size - $('#'+image_id).height())/2;
		$('#'+image_id)[0].style.margin = vertical_margin + "px 0";
	}
}

function thumbnail_set_onclick(carousel_id, image_id, thumbnail_class, number){
	$('#'+image_id)[0].onclick = function(){
		$('.'+thumbnail_class).hide();
		$('#'+carousel_id).carousel(Number(number));
		$('#'+carousel_id).show();
	}
}

function carousel_set_onclick(carousel_id, carousel_image_id, thumbnail_class){
	$('#'+carousel_image_id)[0].onclick = function(){
		$('#'+carousel_id).hide();
		$('.'+thumbnail_class).show();
	}
}

function insert_post(post_id, div_id){
	$.get('/get/post?action=post&datatype=html&postid='+post_id, function(data,status){
		if (status == 'success'){
			div_data = $('#'+div_id).html() + data;
			$('#'+div_id).html(div_data);
			$.getScript('/get/post?action=post&datatype=javascript&postid='+post_id);
		}
	});
}

function load_posts(post_type, post_information, page_id, div_id){
	if (post_type == "all"){
		$.get('/get/post?action=posts&datatype=html&pageid='+page_id+'&posttype='+post_type, function(data,status){
			if (status == 'success'){
				//div_data = $('#'+div_id).html() + data;
				div_data = data;
				$('#'+div_id).html(div_data);
				$.getScript('/get/post?action=posts&datatype=javascript&pageid='+page_id+'&posttype='+post_type);
			}
		});
	}
	else if (post_type == "user"){
		uid = post_information
		$.get('/get/post?action=posts&datatype=html&pageid='+page_id+'&posttype='+post_type+'&uid='+uid, function(data,status){
			if (status == 'success'){
				//div_data = $('#'+div_id).html() + data;
				div_data = data;
				$('#'+div_id).html(div_data);
				$.getScript('/get/post?action=posts&datatype=javascript&pageid='+page_id+'&posttype='+post_type+'&uid='+uid);
			}
		});
	}
}

function get_post_list(type, data, div_id){
	//type=='all'->data:page_id
	//type=='update'->data:datetime
	//type=='user'->data:uid
	//div_id:target_div_to_show_weibo
	$.get('/get/post-list?type='+type+'&data='+data, function(data,status){
		if (status == 'success'){
			post_list = data.split(',');
			for (i in post_list){
				insert_post(post_list[i], div_id);
			}
		}
	});
}

function like(like_id, unlike_id, target_type, target_id){
	$.get('/like?action=like&targettype='+target_type+ '&targetid='+target_id, function(data,status){
		if (status == 'success'){
			liker = $('#'+like_id).text();
			liker = Number(liker.substring(2, liker.length-1));
			liker += 1;
			$('#'+like_id).text('赞('+String(liker)+')');
			$('#'+unlike_id).text('取消赞('+String(liker)+')');
			$('#'+like_id).hide();
			$('#'+unlike_id).show();
		}
	});
}

function unlike(like_id, unlike_id, target_type, target_id){
	$.get('/like?action=unlike&targettype='+target_type+ '&targetid='+target_id, function(data,status){
		if (status == 'success'){
			liker = $('#'+like_id).text();
			liker = Number(liker.substring(2, liker.length-1));
			liker -= 1;
			$('#'+like_id).text('赞('+String(liker)+')');
			$('#'+unlike_id).text('取消赞('+String(liker)+')');
			$('#'+unlike_id).hide();
			$('#'+like_id).show();
		}
	});
}


function collect(collect_id, uncollect_id, target_type, target_id){
	$.get('/collect?action=collect&targettype='+target_type+ '&targetid='+target_id, function(data,status){
		if (status == 'success'){
			collector = $('#'+collect_id).text();
			collector = Number(collector.substring(3, collector.length-1));
			collector += 1;
			$('#'+collect_id).text('收藏('+String(collector)+')');
			$('#'+uncollect_id).text('取消收藏('+String(collector)+')');
			$('#'+collect_id).hide();
			$('#'+uncollect_id).show();
		}
	});
}

function uncollect(collect_id, uncollect_id, target_type, target_id){
	$.get('/collect?action=uncollect&targettype='+target_type+ '&targetid='+target_id, function(data,status){
		if (status == 'success'){
			collector = $('#'+collect_id).text();
			collector = Number(collector.substring(3, collector.length-1));
			collector -= 1;
			$('#'+collect_id).text('收藏('+String(collector)+')');
			$('#'+uncollect_id).text('取消收藏('+String(collector)+')');
			$('#'+uncollect_id).hide();
			$('#'+collect_id).show();
		}
	});
}

function reply(comment_id, user_name){
	text = $('#body').text() + '回复@' + js.lang.String.decodeHtml(user_name) + ' :';
	$('#body').text(text);
	$('#reco_id').val(comment_id);
}
