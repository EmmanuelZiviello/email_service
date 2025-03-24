  function cambia_password() {
            const ucase = new RegExp("[A-Z]+");
            const lcase = new RegExp("[a-z]+");
            const num = new RegExp("[0-9]+");




            const params = new Proxy(new URLSearchParams(window.location.search), {
                get: (searchParams, prop) => searchParams.get(prop),
            });



            if ($("#password1").val().length >= 8 && ucase.test($("#password1").val())
                && lcase.test($("#password1").val()) && num.test($("#password1").val())
                && $("#password1").val() == $("#password2").val()) {
                let user = {
                    "id_paziente": params.id,
                    "password": $("#password1").val()
                }

                // Options to be given as parameter
                // in fetch for making requests
                // other then GET
                let options = {
                    method: 'PATCH',
                    headers: {
                        'Content-Type':
                            'application/json;charset=utf-8',
                    'Authorization': 'Bearer '+params.jwt
                    },
                    body: JSON.stringify(user)
                }

                // Fake api for making post requests
                let fetchRes = fetch(
                    "https://f-taste.bcsoft.net/paziente/password",
                    options);
                fetchRes.then(res =>
                    res.json()).then(d => {
                        if(d.esito=="successo"){
                        window.location.replace("https://f-taste.bcsoft.net/success");
                        }else{
                        window.location.replace("https://f-taste.bcsoft.net/failure");
                        }
                    })
            }
        }






        $("input[type=password]").keyup(function () {
            var ucase = new RegExp("[A-Z]+");
            var lcase = new RegExp("[a-z]+");
            var num = new RegExp("[0-9]+");

            if ($("#password1").val().length >= 8) {
                $("#8char").removeClass("glyphicon-remove");
                $("#8char").addClass("glyphicon-ok");
                $("#8char").css("color", "#00A41E");
            } else {
                $("#8char").removeClass("glyphicon-ok");
                $("#8char").addClass("glyphicon-remove");
                $("#8char").css("color", "#FF0004");
            }

            if (ucase.test($("#password1").val())) {
                $("#ucase").removeClass("glyphicon-remove");
                $("#ucase").addClass("glyphicon-ok");
                $("#ucase").css("color", "#00A41E");
            } else {
                $("#ucase").removeClass("glyphicon-ok");
                $("#ucase").addClass("glyphicon-remove");
                $("#ucase").css("color", "#FF0004");
            }

            if (lcase.test($("#password1").val())) {
                $("#lcase").removeClass("glyphicon-remove");
                $("#lcase").addClass("glyphicon-ok");
                $("#lcase").css("color", "#00A41E");
            } else {
                $("#lcase").removeClass("glyphicon-ok");
                $("#lcase").addClass("glyphicon-remove");
                $("#lcase").css("color", "#FF0004");
            }

            if (num.test($("#password1").val())) {
                $("#num").removeClass("glyphicon-remove");
                $("#num").addClass("glyphicon-ok");
                $("#num").css("color", "#00A41E");
            } else {
                $("#num").removeClass("glyphicon-ok");
                $("#num").addClass("glyphicon-remove");
                $("#num").css("color", "#FF0004");
            }

            if ($("#password1").val() == $("#password2").val()) {
                $("#pwmatch").removeClass("glyphicon-remove");
                $("#pwmatch").addClass("glyphicon-ok");
                $("#pwmatch").css("color", "#00A41E");
            } else {
                $("#pwmatch").removeClass("glyphicon-ok");
                $("#pwmatch").addClass("glyphicon-remove");
                $("#pwmatch").css("color", "#FF0004");
            }
        });

