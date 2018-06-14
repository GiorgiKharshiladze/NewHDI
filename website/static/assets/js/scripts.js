(function(window, undefined) {
  'use strict';

  /*
  NOTE:
  ------
  PLACE HERE YOUR OWN JAVASCRIPT CODE IF NEEDED
  WE WILL RELEASE FUTURE UPDATES SO IN ORDER TO NOT OVERWRITE YOUR JAVASCRIPT CODE PLEASE CONSIDER WRITING YOUR SCRIPT HERE.  */
})(window);

// Helper for current date
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1; //January is 0!
var yyyy = today.getFullYear();

if(dd<10) {
    dd = '0'+dd
} 

if(mm<10) {
    mm = '0'+mm
}

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
/* BEGIN: validation */
function validation(){
  sum = 0;
  weightList = [];

  // indicator and weight validation
  for (var i=1; i<=parseInt(amount); i++){
    if ($("#weight"+i).val() != null) {
      weightList.push($("#weight"+i).val());
    }
  }
  sum = eval(weightList.join('+'));

  for (var i=1; i<=parseInt(amount); i++){
    if ($("#indicator"+i).val() == null || $("#weight"+i).val() == null || sum != 1) {
      $("#validSpace").show();
      $("#validSpace").html('<div class="alert alert-primary mb-2" role="alert"><ul><li id="alertOne"></li><li id="alertTwo"></li></ul></div>');

      $("#alertOne").html("All fields are required");
      $("#calculateButton").attr("disabled", "");
      if (sum != 1){
      (sum == undefined) ? sum = 0 : false;
      $("#alertTwo").html('Weights total should be 100%, current total = '+ Math.round(sum * 10000)/100+'%');
      }
      else {
        $("#alertOne").html("All fields are required");
        $("#alertTwo").hide();
      }
    }
    else {
        $("#calculateButton").removeAttr("disabled");
        $("#validSpace").hide();
    }
  }
}
/* END: validation */
for (var i=1; i<= parseInt(amount); i++){
  $("#weight"+i).change(function(){validation();});
  $("#indicator"+i).change(function(){validation();});
  if (i < parseInt(amount)){
  $("#operation"+i).change(function(){validation();});
  }
}


/* BEGIN: ORDER Data_TABLE by its value */
if(window.location.pathname == "/hdi/view/" || window.location.pathname == "/hdi/submit/"){

  // $('#data_table').DataTable( {
  //     "order": [[ parseInt(amount)+1, "desc" ]]
  // } );
  var formula = "<b><h1><i>f(x) = ";
  var letters = ['a', 'b', 'c', 'd', 'e']
  var weights = []
  $('#formula_table .weight').each(function(){
    weights.push($(this).html());
  });

  for (var i=0; i<=operations.length; i++){
    formula += letters[i] + "<sup> ("+ weights[i] +")</sup> ";
    if (i != operations.length){
      formula += operations[i] + " ";
    }
  }

  $("#formula").html(formula + "</i></h1></b>");
  
  var title = "MyHDI_Ranking: "+mm+"."+dd+"."+yyyy;
  var table = $('#data_table').DataTable({
        // "order": [[ parseInt(amount)+1, "desc" ]],
        responsive: true,
        "order": [[ 0, "desc" ]], // ordered by the first column
        "lengthMenu": [[10, 50, 100, -1], [10, 50, 100, "All"]],
        dom: "<'ui grid'"+
                 "<'row'"+
                    "<'col-md-6'B>"+
                    "<'col-md-6'f>"+
                 ">"+
                 "<'row dt-table'"+
                    "<'col-md-12'tr>"+
                 ">"+
                 "<'row'"+
                    "<'col-md-6'i>"+
                    "<'col-md-6'p>"+
                 ">"+
              ">",
        buttons: [
          'pageLength',
          'copy',
          {
            'extend': 'csv',
            'title' : title
          },
          {
            'extend': 'excel',
            'title' : title
          },
          {
            'extend': 'pdf',
            'title' : title
          },
          'print'
        ]
    });
  $('.buttons-copy, .buttons-csv, .buttons-print, .buttons-pdf, .buttons-excel').addClass('btn btn-info');

}
/* END: ORDER Data_TABLE by its value */

