(function(window, undefined) {
  'use strict';

  /*
  NOTE:
  ------
  PLACE HERE YOUR OWN JAVASCRIPT CODE IF NEEDED
  WE WILL RELEASE FUTURE UPDATES SO IN ORDER TO NOT OVERWRITE YOUR JAVASCRIPT CODE PLEASE CONSIDER WRITING YOUR SCRIPT HERE.  */
})(window);

if ($("#chooseAmount").val() == null) {
		$("#createButton").attr("disabled", "");
}

$("#chooseAmount").on("change", function() {
	if ($("#chooseAmount").val() != null) {
		$("#createButton").removeAttr("disabled");
	}
});

var baseURL = window.location.protocol + "//" + window.location.hostname + ":" + window.location.port;

function createFormula() {

	document.location = baseURL + window.location.pathname + "?amount=" + $("#chooseAmount").val();
}


$('#data_table').DataTable( {
    "order": [[ parseInt(amount)+1, "desc" ]]
} );