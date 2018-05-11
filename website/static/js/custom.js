function exists(element) {

	element.each(function(){
		var li = $(this).find('li');

		console.log(li.text());
		console.log($( "#indicators option:selected" ).text());

		// if(li.text() == $( "#indicators option:selected" ).text()) {
		// 	return true;
		// }
	});
	return false;
}

$( "#add" ).click(function() {

	if(!exists($("#formula"))) {
		$("#formula").append('<li class="list-group-item">'+ $( "#indicators option:selected" ).text() +'</li>');
	}

});