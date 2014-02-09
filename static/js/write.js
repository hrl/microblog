var add_error = new Array()
function push_image(image_url, image_number){
	switch (Math.ceil(image_number/3)){
		case 1:
			image_line = $('#image_line1').html() + '<div class="col-sm-4 post-img-thumbnail"><center><img id="image-' + image_number + '" src="'+image_url+'"></center></div>';
			$('#image_line1').html(image_line);
			break;
		case 2:
			image_line = $('#image_line2').html() + '<div class="col-sm-4 post-img-thumbnail"><center><img id="image-' + image_number + '" src="'+image_url+'"></center></div>';
			$('#image_line2').html(image_line);
			break;
		case 3:
			image_line = $('#image_line3').html() + '<div class="col-sm-4 post-img-thumbnail"><center><img id="image-' + image_number + '" src="'+image_url+'"></center></div>';
			$('#image_line3').html(image_line);
			break;
	}
}

function push_video(video_url, video_number){
	switch (Math.ceil(video_number/1)){
		case 1:
			video_line = $('#video_line').html() + '<video src="' + video_url +'"  width="320" height="240" controls="controls"></video>';
			$('#video_line').html(video_line);
			break;
	}
}

function push_audio(audio_url, audio_number){
	switch (Math.ceil(audio_number/1)){
		case 1:
			audio_line = $('#audio_line').html() + '<audio src="' + audio_url +'" controls="controls"></audio>';
			$('#audio_line').html(audio_line);
			break;
	}
}

$('#add_image_button')[0].onclick = function(){
	image_input = $('#add_image').val();
	image_re = RegExp(/[^'"?#]+\.jpeg$|[^'"?#]+\.jpg$|[^'"?#]+\.png$|[^'"?#]+\.bmp$/);
	if (image_input.search(image_re) == 0 ){
		new_image = $('#image').val() + '/////' + image_input;
		$('#image').val(new_image);
		image_number = $('#image').val().split('/////').length -1;
		push_image(image_input, image_number);
		post_img_thumbnail_width = $('.post-img-thumbnail').width();
		image_set_size("image-"+image_number, post_img_thumbnail_width);
		$('.post-img-thumbnail').height(post_img_thumbnail_width);
		if (image_number >= 9){
			$('#add_image').hide();
			$('#add_image_button').hide();
		}
	}
	else{
		alert('Invalid image.');
	}
}
$('#add_video_button')[0].onclick = function(){
	video_input = $('#add_video').val();
	video_re = RegExp(/[^'"?#]+\.mp4$|[^'"?#]+\.flv$|[^'"?#]+\.ogg$/);
	if (video_input.search(video_re) == 0 ){
		new_video = $('#video').val() + '/////' + video_input;
		$('#video').val(new_video);
		video_number = $('#video').val().split('/////').length -1;
		push_video(video_input, video_number);
		if (video_number >= 1){
			$('#add_video').hide();
			$('#add_video_button').hide();
		}
	}
	else{
		alert('Invalid video.');
	}
}
$('#add_audio_button')[0].onclick = function(){
	audio_input = $('#add_audio').val();
	audio_re = RegExp(/[^'"?#]+\.mp3$|[^'"?#]+\.wav$|[^'"?#]+\.ogg$/);
	if (audio_input.search(audio_re) == 0 ){
		new_audio = $('#audio').val() + '/////' + audio_input;
		$('#audio').val(new_audio);
		audio_number = $('#audio').val().split('/////').length -1;
		push_audio(audio_input, audio_number);
		if (audio_number >= 1){
			$('#add_audio').hide();
			$('#add_audio_button').hide();
		}
	}
	else{
		alert('Invalid audio.');
	}
}
