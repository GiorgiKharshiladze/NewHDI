(function(window, undefined) {
  'use strict';

  /*
  NOTE:
  ------
  PLACE HERE YOUR OWN JAVASCRIPT CODE IF NEEDED
  WE WILL RELEASE FUTURE UPDATES SO IN ORDER TO NOT OVERWRITE YOUR JAVASCRIPT CODE PLEASE CONSIDER WRITING YOUR SCRIPT HERE.  */
})(window);

var amount = $("#chooseAmount").val();

if (amount == null) {
		$("#createButton").attr("disabled", "");
}

$("#chooseAmount").on("change", function() {
	if ($("#chooseAmount").val() != null) {
		$("#createButton").removeAttr("disabled");
	}
});

function createFormula() {

	document.location = window.location.href + "?amount=" + amount;
}