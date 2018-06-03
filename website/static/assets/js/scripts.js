(function(window, undefined) {
  'use strict';

  /*
  NOTE:
  ------
  PLACE HERE YOUR OWN JAVASCRIPT CODE IF NEEDED
  WE WILL RELEASE FUTURE UPDATES SO IN ORDER TO NOT OVERWRITE YOUR JAVASCRIPT CODE PLEASE CONSIDER WRITING YOUR SCRIPT HERE.  */
})(window);

var baseURL = window.location.protocol + "//" + window.location.hostname + ":" + window.location.port;

function createFormula(){
	
	amount = $("#chooseAmount").val();
	indicators = [];

	apiIndicators = baseURL + "/api/id/all?format=json";

	$.getJSON(apiIndicators, function(indicators) {

		$("#formulaCard").html($('<div class="card-header"><h4 class="card-title">Create Your Formula</h4></div><div class="card-content collapse show"><div class="card-body"><form action="" method="POST" id="form"></form></div></div></div>'));

		var indicatorsHTML = '<div class="col-md-12"><select class="select2 form-control col-md-7"><optgroup label="WorldBank">';

    	for (var i=0; i < indicators.length; i++) {
			indicatorsHTML += '<option value="'+ indicators[i].my_id +'">'+ indicators[i].description +'</option>';
		}
		indicatorsHTML += '</optgroup></select></div>';

		$('#form').html($(indicatorsHTML));

	});

	


	// formHTML = '<div class="row text-center">
 //                                        <div class="col-md-12">
 //                                            <select class="select2 form-control col-md-7">
 //                                                <optgroup label="WorldBank">
 //                                                  {% for indicator in data.indicators %}
 //                                                  <option value="{{ indicator.my_id }}">{{ indicator.description }}</option>
 //                                                  {% endfor %}
 //                                                </optgroup>
 //                                            </select>
 //                                            <select class="select2 form-control col-md-1">
 //                                                <optgroup label="Weight">
 //                                                  {% for weight in data.weights %}
 //                                                  <option value="{{ weight }}">{{ weight }}</option>
 //                                                  {% endfor %}
 //                                                </optgroup>
 //                                            </select>
 //                                        </div>
 //                                    </div>'

	
}