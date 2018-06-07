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



$("#calculateButton").attr("disabled", "");
$("#validSpace").html('<div class="alert alert-info mb-2" role="alert">All fields are required</div>');

/* BEGIN: Sum should be 1 */
function sumUp() {
  sum = 0;
  weightList = [];

  for (var i=1; i<=parseInt(amount); i++){
    if ($("#weight"+i).val() != null) {
      weightList.push($("#weight"+i).val());
    }
  }
  sum = eval(weightList.join('+'));
  if (sum == 1) {
    $("#calculateButton").removeAttr("disabled");
    $("#alertSpace").html('');
  }
  else {
    $("#calculateButton").attr("disabled", "");
    $("#alertSpace").html('<div class="alert alert-primary mb-2" role="alert">Weights total should be 100%, current total = '+Math.round(sum * 10000)/100+'%</div>');
  }
}

/* BEGIN: validation */
function validation(){
  for (var i=1; i<=parseInt(amount); i++){
    if ($("#indicator"+i).val() == null || $("#weight"+i).val() == null) {
      $("#calculateButton").attr("disabled", "");
    }
    else {
      $("#calculateButton").removeAttr("disabled");
      $("#validSpace").html('');
    }

  }
}
/* END: validation */

for (var i=1; i<= parseInt(amount); i++){
  $("#weight"+i).change(function(){sumUp();validation();});
  $("#indicator"+i).change(function(){validation();});
  if (i < parseInt(amount)){
  $("#operation"+i).change(function(){validation();});
  }
}

/* END: Sum should be 1 */


/* BEGIN: ORDER Data_TABLE by its value */
if(window.location.pathname == "/hdi/view/"){
  $('#data_table').DataTable( {
      "order": [[ parseInt(amount)+1, "desc" ]]
  } );
}
/* END: ORDER Data_TABLE by its value */

