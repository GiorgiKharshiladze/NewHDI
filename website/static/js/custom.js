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
	var index = $("#table").children().length;
	if(!exists($("#formula")) && index < 5) {
		$("#table").append('<div class="row" style="margin-top:1%;"><div class="col-md-2" id="coefficient"><input type="text" name="" style="height: 100%; width: 100%;" placeholder="Coefficient"></div><div class="col-md-10"><ul class="list-group" id="formula"><li class="list-group-item">'+ $( "#indicators option:selected" ).text() +'</li></ul></div></div>');
		// $("#coefficient").append('<input type="text" name="coefficient" style="width: 100%;" placeholder="Coefficient">');
		// $("#formula").append('<li class="list-group-item">'+ $( "#indicators option:selected" ).text() +'</li>');
	}

});