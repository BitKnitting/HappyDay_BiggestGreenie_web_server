
var placeSearch, autocomplete;
var componentForm = {
  street_number: 'short_name',
  route: 'long_name',
  locality: 'long_name',
  administrative_area_level_1: 'short_name',
  country: 'long_name',
  postal_code: 'short_name'
};

function initAutocomplete() {

  // Create the autocomplete object, restricting the search to geographical
  // location types.
  autocomplete = new google.maps.places.Autocomplete(
    /** @type {!HTMLInputElement} */
    (document.getElementById('autocomplete')), {
      types: ['geocode']
    });

  // When the user selects an address from the dropdown, populate the address
  // fields in the form.
  autocomplete.addListener('place_changed', fillInAddress);
}

function fillInAddress() {
  // Get the place details from the autocomplete object.
  var place = autocomplete.getPlace();
  var components_by_type = {};
  for (var i = 0; i < place.address_components.length; i++) {
    var c = place.address_components[i];
    components_by_type[c.types[0]] = c;
  }
  document.getElementById('street').textContent =
  components_by_type['street_number'].short_name + '  ' +
  components_by_type['route'].long_name
  document.getElementById('city_state').textContent =
  components_by_type['locality'].long_name + ',  ' +
  components_by_type['administrative_area_level_1'].short_name + '   ' +
  components_by_type['postal_code'].short_name
  $('#address').collapse('show');
}

// Bias the autocomplete object to the user's geographical location,
// as supplied by the browser's 'navigator.geolocation' object.
// Putting cursor in text field calls geolocate and also triggers
// the collapse section.  This is why collapse('hide') is at the
// bottom of this function.
function geolocate() {
  // in case already ran...
  $('#address').collapse('hide');
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var geolocation = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      var circle = new google.maps.Circle({
        center: geolocation,
        radius: position.coords.accuracy
      });
      autocomplete.setBounds(circle.getBounds());
    });
  }
}
