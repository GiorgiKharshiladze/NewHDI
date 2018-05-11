function exists(element) {

		var bool = false;

		element.find('li').each(function(){

			if($(this).text() == $( "#indicators option:selected" ).text()) {
				bool = true;
				return bool;
			}
		});
		return bool;
}

$( "#add" ).click(function() {
	console.log(exists($("#formula")));
	if(exists($("#formula")) != true) {
		$("#formula").append('<li class="list-group-item">'+ $( "#indicators option:selected" ).text() +'</li>');
	}

});