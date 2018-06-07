(function(window, undefined) {
  'use strict';

  /*
  NOTE:
  ------
  PLACE HERE YOUR OWN JAVASCRIPT CODE IF NEEDED
  WE WILL RELEASE FUTURE UPDATES SO IN ORDER TO NOT OVERWRITE YOUR JAVASCRIPT CODE PLEASE CONSIDER WRITING YOUR SCRIPT HERE.  */
})(window);

/* BEGIN: Choose Amount for creating formula */
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
/* END: Choose Amount for creating formula */

for (var i=1; i <= parseInt(amount); i++){
  for(var j=1; j<=100; j++) {
    $("#weight"+i).append("<option value='"+j/100+"'>"+j+"%</option>");
  }
}


/* Sum should be 1 */
weightList = [0];
sum = 0;

function sumUp() {
  for (var i=1; i<=parseInt(amount); i++){
    if ($("#weight"+i).val() != null) {
      weightList.push($("#weight"+i).val());
    }
  }
  return weightList.reduce(function(acc, val) { return acc + val; });
}

$("#weight2").change(console.log(sumUp()));

$("#calculateButton").attr("disabled", "");

/* BEGIN: ORDER Data_TABLE by its value */
if(window.location.pathname == "/hdi/view/"){
  $('#data_table').DataTable( {
      "order": [[ parseInt(amount)+1, "desc" ]]
  } );
}
/* END: ORDER Data_TABLE by its value */

