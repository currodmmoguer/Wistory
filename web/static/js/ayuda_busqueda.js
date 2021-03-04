let personas = [];
let dinastias = [];
let cargos = [];

/////////////////////////////////////
// AYUDA DE BÚSQUEDA PERSONA
/////////////////////////////////////

$("#buscar_persona").click(function () {
    let lista_dinastias = [];
    let lista_id_personas = [];

    let dic_personas = getPersonas();

    // Crea la lista de objetos personas, dinastías
    dic_personas["personas"].forEach((p) => {
        personas.push(p); // Lista de objetos persona

        // Añade los IDs de las dinastía a una lista
        if (
            lista_dinastias.indexOf(p["fields"]["dinastia"]) === -1 &&
            p["fields"]["dinastia"]
        ) {
            lista_dinastias.push(p["fields"]["dinastia"]);
        }

        // Añade los IDs de las personas a una lista
        if (lista_id_personas.indexOf(p.pk) === -1 && p.pk) {
            lista_id_personas.push(p.pk);
        }
    });

    // Obtiene las dinastias ({pk: nombre})
    dinastias = getDinastiaById(lista_dinastias);
    // Obtiene los cargos ({pk_persona: nombre_cargo})
    cargos = getCargos(lista_id_personas);

    // Añade los resultados a la lista
    console.log($("#lista_personas option"));
    $("#lista_personas option").remove();

    personas.forEach((p) => {
        $("#lista_personas").append(
            '<option value="' + p["pk"] + '">' + p["fields"]["nombre"] + "</option>"
        );
    });
});

// Añade los datos correspondiente a los campos del modal
$("#lista_personas").click(function () {
    var opt = $(this).children().filter(function () {
        return $(this)[0].selected;
    });

    persona = personas.find((p) => p.pk == opt[0].value);
    $("#modal_persona_nombre").val(persona["fields"]["nombre"]);    // Nombre persona
    $("#modal_persona_dinastia").val(dinastias[persona["fields"]["dinastia"]]); // Dinastía
    $("#modal_persona_cargo").val(cargos[persona.pk]);  // Cargo

});

// Cerrar modal
$("#submit_ayuda_persona").click(function () {
    $("#persona_filter").val($("#modal_persona_nombre").val());
    $("#dinastia_filter").val($("#modal_persona_dinastia").val());
});



/////////////////////////////////////
// AYUDA DE BÚSQUEDA DINASTÍA
/////////////////////////////////////

$('#buscar_dinastia').click(function () {
    dinastias = getDinastia($("#modal_dinastia_nombre").val());

    // Añade los resultados a la lista
    $("#lista_dinastias option").remove();

    for (let [id, value] of Object.entries(dinastias)) {
        $("#lista_dinastias").append(
            '<option value="' + id + '">' + value + "</option>"
        );
    }
});


// Añadir una dinastía
$('#modal_add_dinastia').click(function () {
    addDinastias($('#lista_dinastias').find(':selected'));
});

// Quitar una dinastía
$('#modal_remove_dinastia').click(function () {
    delDinastias($('#added_dinastias').find(':selected'));
});

// Añadir todas las dinastías de la lista
$('#modal_add_all_dinastia').click(function () {
    addDinastias($('#lista_dinastias option'));
});

// Quitar todas las dinastías de la lista
$('#modal_remove_all_dinastia').click(function () {
    delDinastias($('#added_dinastias option'));
});

// Cerrar modal
$("#submit_ayuda_dinastia").click(function () {
    $("#dinastia_filter").val($("#modal_dinastia_nombre").val());
});



// Cuando se clica un resultado se traspasa al campo persona
// NO FUNCIONA
// $("#lista_personas option").click(function () {
//   alert("Ljgulyhgkj")
//   persona = personas.find((p) => p.pk == this.value);
//   $("#modal_persona_nombre").val($(this).text());
//   $("#modal_persona_dinastia").val(dinastias[persona["fields"]["dinastia"]]);
//   $("#modal_persona_cargo").val(cargos[persona.pk]);
// });






// Funciones

/**
 * Obtiene los personajes a partir del formulario
 */
function getPersonas() {

    let personas = "";
    let nombre = $("#modal_persona_nombre").val();
    let dinastia = $("#modal_persona_dinastia").val();
    let cargo = $("#modal_persona_cargo").val();
    $.ajax({
        url: $('meta[name=url_get_personas]').attr('content'),
        cache: false,
        async: false,
        data: {
            nombre: nombre,
            dinastia: dinastia,
            cargo: cargo,
        },
        success: function (data) {
            personas = data;
        },
    });
    return personas;
}

/**
 * Obtiene las dinastías a partir de su nombre
 * Devuelve un diccionario de datos con formato: {pk: nombre}
 * @param {String} nombre - Nombre por el que busca la dinastía
 * @return {Json} dinastias - Diccionario de datos con las dinastías encontradas
 */
function getDinastia(nombre) {
    let dinastias = {};
    $.ajax({
        url: $('meta[name=url_get_dinastias]').attr('content'),
        cache: false,
        async: false,
        data: {
            nombre: nombre,
        },
        success: function (data) {
            dinastias = data;
        },
    });
    return dinastias;
}

/**
 * Obtiene las dinastías a partir de una lista de IDs
 * Devuelve un diccionario de datos con formato: {pk: nombre}
 * @param {Array} id - Lista de IDs
 * @return {Json} dinastia - Diccionario de datos con las dinastías encontradas
 */
function getDinastiaById(id) {
    let dinastia = "";

    $.ajax({
        url: $('meta[name=url_get_dinastias_by_id]').attr('content'),
        data: {
            id: id,
        },
        cache: false,
        async: false,
        success: function (data) {
            if (data) {
                dinastia = data;
            }
        },
    });

    return dinastia;
}

/**
 * Obtiene los cargos a partir de una lista de IDs de personas
 * Devuelve un diccionario de dato con formato: {personaID: nombreCargo}
 * @param {Array} id - Lista de IDs
 * @return {Json} cargos - Diccionario de datos con la relación cargo - persona
 */
function getCargos(id) {
    let cargos = "";

    $.ajax({
        url: $('meta[name=url_get_cargos]').attr('content'),
        data: {
            id: id,
        },
        cache: false,
        async: false,
        success: function (data) {
            if (data) {
                cargos = data;
            }
        },
    });

    return cargos;
}

/**
 * Obtiene los eventos filtrando por su nombre
 * @param {String} nombre - Nombre del evento
 */
function getEventos(nombre) {
    $.ajax({
        url: $('meta[name=url_get_eventos]').attr('content'),
        data: {
            nombre: nombre,
        },
        cache: false,
        async: false,
        success: function (data) {
            if (data) {
                alert(data);
            }
        },
    });
}
/**
 * Añade los elementos pasado por parámetros a la lista de dinastías seleccionadas
 * @param {Array[Option]} lista - Lista de Option de un Select que se añade a la lista de añadidos
 */
function addDinastias(lista) {

    let nombre_dinastias = "";
    let id_dinastias = [];

    lista.each((i, opt) => {

        if ($('#added_dinastias option[value=' + opt.value + ']').length == 0) {

            // Añade a la otra lista
            $("#added_dinastias").append(opt);

            // Almacena el valor del campo nombre dinastía
            nombre_dinastias = $("#modal_dinastia_nombre").val();

            // Almacena en un array los IDs de las dinastía

            try {
                id_dinastias = $("#modal_dinastia_nombre").attr('data-ids').split(",");
            } catch (TypeError) {
                // Se queda el array id_dinastias vacío
            }

            // Añade al campo nombre la nueva dinastía
            $("#modal_dinastia_nombre").val(nombre_dinastias + ", " + opt.text);

            ajustarTextoDinastia();

            // Añade a la lista el nuevo ID
            id_dinastias.push(opt.value);
            $("#modal_dinastia_nombre").attr('data-ids', id_dinastias);
        }

    });

}

/**
 * Quita los elementos de la lista de añadidos y los pone en la lista de buscados
 * @param {Array[Option]} lista 
 */
function delDinastias(lista) {
    let value = "";
    let id_dinastias = [];


    lista.each((i, opt) => {
        // Quitar y añadir a la otra lista
        $('#lista_dinastias').append(opt);

        // Borrar id del campo


        // Borrar texto del campo
        $("#modal_dinastia_nombre").val($("#modal_dinastia_nombre").val().replace(opt.text, ''));

        ajustarTextoDinastia();

        // Elimina de la lista el ID de la dinastía
        try {
            id_dinastias = $("#modal_dinastia_nombre").attr('data-ids').split(",");
            id_dinastias = id_dinastias.filter(i => i != opt.value);
            $("#modal_dinastia_nombre").attr('data-ids', id_dinastias);
        } catch (TypeError) {
            // No debería saltar esta excepción nunca
        }




    });
}

/**
 * Pone el campo de nombre dinastía más legible.
 *  * Quita comas repetidas
 *  * Quita comas al principio
 *  * Quita comas al final
 */
function ajustarTextoDinastia() {
    // Borra si hay comas seguidas
    $("#modal_dinastia_nombre").val($("#modal_dinastia_nombre").val().replace(', , ', ', '));

    // Borra la primera coma
    if ($("#modal_dinastia_nombre").val().startsWith(', ')) {
        $("#modal_dinastia_nombre").val($("#modal_dinastia_nombre").val().slice(2));
    }
    if ($("#modal_dinastia_nombre").val().endsWith(', ')) {
        $("#modal_dinastia_nombre").val($("#modal_dinastia_nombre").val().slice(0, -2));
    }
}