function localizar(elemento,direccion) {
    var geocoder = new google.maps.Geocoder();

    var map = new google.maps.Map(document.getElementById(elemento), {
      zoom: 16,
      scrollwheel: true,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });
<<<<<<< Updated upstream
    
    geocoder.geocode({'address': direccion}, function(results, status) {
=======

    infoWindow = new google.maps.InfoWindow();
    const locationButton = document.createElement("button");
    locationButton.textContent = "Ver tu ubicación";
    locationButton.classList.add("custom-map-control-button");
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(
        locationButton
    );

    geocoder.geocode({ 'address': direccion }, function(results, status) {
>>>>>>> Stashed changes
        if (status === 'OK') {

            var bounds = new google.maps.LatLngBounds();

            var resultados = results[0].geometry.location,
                resultados_lat = resultados.lat(),
                resultados_long = resultados.lng();
            
<<<<<<< Updated upstream
=======
            bounds.extend(results[0].geometry.location)
                
            // own location

            locationButton.addEventListener("click", () => {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(
                        (position) => {
                            const pos = {
                                lat: position.coords.latitude,
                                lng: position.coords.longitude,
                            };
                            map.setCenter(pos);

                            bounds.extend(pos)

                            
                            /*
                            new google.maps.Marker({
                                position: pos,
                                map,
                                label: "home",
                                title: "Hello World!",
                            }); 
                            */

                            infoWindow.setPosition(pos);
                            infoWindow.setContent("Tu Ubicación");
                            infoWindow.open(map);
                            map.setCenter(pos);
                            
                            map.fitBounds(bounds);
                        }, 
                        () => {
                            handleLocationError(true, infoWindow, map.getCenter());
                        }
                    );
                } else {
                    handleLocationError(false, infoWindow, map.getCenter());
                }
            });
            // own location

>>>>>>> Stashed changes
            map.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location
            });
            

        } else {
            var mensajeError = "";
            if (status === "ZERO_RESULTS") {
                mensajeError = "No hubo resultados para la dirección ingresada.";
            } else if (status === "OVER_QUERY_LIMIT" || status === "REQUEST_DENIED" || status === "UNKNOWN_ERROR") {
                mensajeError = "Error general del mapa.";
            } else if (status === "INVALID_REQUEST") {
                mensajeError = "Error de la web. Contacte con Name Agency.";
            }
            alert(mensajeError);
        }
    });
}

$.getScript("https://maps.googleapis.com/maps/api/js?key=AIzaSyCWoCrz3TSv3kEaA_MstpeIfagivpPGiKw", function() {
    $("#buscar").click(function() {
        var direccion = $("#direccion").val();
<<<<<<< Updated upstream
        if (direccion !== "") {
            localizar("mapa-geocoder", direccion);
        }
=======
        localizar("mapa-geocoder", direccion);
>>>>>>> Stashed changes
    });
});
