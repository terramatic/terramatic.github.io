/* ON PAGE LOAD */
function pageLoad() {

	// Config globe
	var config = {
		"control": {
			"stats": false,
			"disableUnmentioned": true,
			"lightenMentioned": true,
			"inOnly": false,
			"outOnly": true,
			"initCountry": "CN",
			"halo": true,
			"transparentBackground": false,
			"autoRotation": false,
			"rotationRatio": 1
		},
		"color": {
			"surface": 16777215,
			"selected": 16777215,
			"unmentioned": 16777215,
			"in": 4390905,
			"out": 4390905,
			"halo": 4390905,
			"background": 2369859
		},
		"brightness": {
			"ocean": 0.7,
			"mentioned": 1,
			"related": 1
		}
	};

    var container = document.getElementById( "globalArea" );
    var controller = new GIO.Controller( container );
    controller.configure(config);
    
    /* Default country to start with */
    controller.setInitCountry("ES");

    // use the onCountryPicked() to set callback when clicked country changed
    controller.onCountryPicked( callback );
    // the callback function can get parameter contains some country data, the detailed of the parameter can be found in the API document
    function callback ( selectedCountry ) {
        $( "#countryArea" ).text( selectedCountry.name + " picked!" );
        $( "#infoBoard" ).fadeIn( 1000 );
        setTimeout( function () {
            $( "#infoBoard" ).fadeOut( 1000 );
        }, 3000 );
    }
    $.ajax( {
        url: "data/countries_visited.json",
        type: "GET",
        contentType: "application/json; charset=utf-8",
        async: true,
        dataType: "json",
        success: function ( inputData ) {
            controller.addData( inputData );
            controller.init();
        }
    } );
}

