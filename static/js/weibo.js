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
