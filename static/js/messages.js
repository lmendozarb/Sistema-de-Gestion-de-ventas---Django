function messageeco(mensaje='EcoSolution something',tipomensaje='info',titulomensaje='EcoSolution'){
	swal({
		title: titulomensaje,
		text: mensaje,
		icon: tipomensaje,
		button: "Aceptar",
		timer: 3000,
	});
}
