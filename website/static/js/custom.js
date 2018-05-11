function exists(element) {

		element.find('li').each(function(){
			// console.log($(this).text());
			// console.log($( "#indicators option:selected" ).text());
			if($(this).text() == $( "#indicators option:selected" ).text()) {
				console.log("Giorgi");
				return true;
			}
		});
		return false;
}

$( "#add" ).click(function() {
	exists($("#formula"));
	// if(!exists($("#formula"))) {
		$("#formula").append('<li class="list-group-item">'+ $( "#indicators option:selected" ).text() +'</li>');
	// }
	console.log(exists($("#formula")));

});