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
	if(!exists($("#formula"))) {
		$("#formula").append('<li class="list-group-item">'+ $( "#indicators option:selected" ).text() +'</li>');
	}

});