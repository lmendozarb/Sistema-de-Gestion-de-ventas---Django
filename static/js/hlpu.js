$(document).ready(function() {
    $("#PagoHacklibreURL").click(function() {
        amount = $("#amount").val();
        amount = amount.replace(",", ".");
        amount = amount * 100;
        denomination = $("#denomination").val();
        Culqi.publicKey = 'aca va tu cable de culqi';
        Culqi.settings({
            title: 'Vilsoft PAGO URL',
            currency: 'PEN',
            description: denomination,
            amount: amount
        });
        Culqi.open();
    });
});

function culqi() {
    if (Culqi.token) {
        $(document).ajaxStart(function() {
            run_waitMe();
        });
        // Imprimir Token
        $.ajax({
            type: 'POST',
            url: '/processpayment/',
            data: {
                csrfmiddlewaretoken: $("#csrf").val(),
                token: Culqi.token.id,
                mail: Culqi.token.email,
                denomination: $("#denomination").val(),
                amount: $("#amount").val(),
                CodigoPublico: $("#CodigoPublico").val()
            },
            datatype: 'json',
            success: function(data) {
                var result = "";
                if (data.constructor == String) {
                    result = JSON.parse(data);
                }
                if (data.constructor == Object) {
                    result = JSON.parse(JSON.stringify(data));
                }
                if (result.object === 'charge') {
                    resultdiv("<div class='pay-tabs'><h2>Mensaje</h2>" + result.outcome.user_message + "</div>");
                    location.reload();
                }
                if (result.object === 'error') {
                    resultdiv(result.user_message);
                }
            },
            error: function(error) {
                resultdiv(error);
            }
        });
    } else {
        resultdiv(Culqi.error.user_message);
    }
}

function run_waitMe() {
    $('body').waitMe({
        effect: 'orbit',
        text: 'Procesando pago...',
        bg: 'rgba(255,255,255,0.7)',
        color: '#c83737'
    });
}

function resultdiv(message) {
    $('#horizontalTab').html(message);
    $('body').waitMe('hide');
}
