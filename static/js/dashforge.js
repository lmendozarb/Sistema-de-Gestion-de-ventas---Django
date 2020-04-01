
$(function(){
  'use strict'

  feather.replace();

  ////////// NAVBAR //////////

  // Initialize PerfectScrollbar of navbar menu for mobile only
  if(window.matchMedia('(max-width: 991px)').matches) {
    const psNavbar = new PerfectScrollbar('#navbarMenu', {
      suppressScrollX: true
    });
  }

  // Showing sub-menu of active menu on navbar when mobile
  function showNavbarActiveSub() {
    if(window.matchMedia('(max-width: 991px)').matches) {
      $('#navbarMenu .active').addClass('show');
    } else {
      $('#navbarMenu .active').removeClass('show');
    }
  }

  showNavbarActiveSub()
  $(window).resize(function(){
    showNavbarActiveSub()
  })

  // Initialize backdrop for overlay purpose
  $('body').append('<div class="backdrop"></div>');


  // Showing sub menu of navbar menu while hiding other siblings
  $('.navbar-menu .with-sub .nav-link').on('click', function(e){
    e.preventDefault();
    $(this).parent().toggleClass('show');
    $(this).parent().siblings().removeClass('show');

    if(window.matchMedia('(max-width: 991px)').matches) {
      psNavbar.update();
    }
  })

  // Closing dropdown menu of navbar menu
  $(document).on('click touchstart', function(e){
    e.stopPropagation();

    // closing nav sub menu of header when clicking outside of it
    if(window.matchMedia('(min-width: 992px)').matches) {
      var navTarg = $(e.target).closest('.navbar-menu .nav-item').length;
      if(!navTarg) {
        $('.navbar-header .show').removeClass('show');
      }
    }
  })

  $('#mainMenuClose').on('click', function(e){
    e.preventDefault();
    $('body').removeClass('navbar-nav-show');
  });

  $('#sidebarMenuOpen').on('click', function(e){
    e.preventDefault();
    $('body').addClass('sidebar-show');
  })

  // Navbar Search
  $('#navbarSearch').on('click', function(e){
    e.preventDefault();
    $('.navbar-search').addClass('visible');
    $('.backdrop').addClass('show');
  })

  $('#navbarSearchClose').on('click', function(e){
    e.preventDefault();
    $('.navbar-search').removeClass('visible');
    $('.backdrop').removeClass('show');
  })



  ////////// SIDEBAR //////////

  // Initialize PerfectScrollbar for sidebar menu
  if($('#sidebarMenu').length) {
    const psSidebar = new PerfectScrollbar('#sidebarMenu', {
      suppressScrollX: true
    });


    // Showing sub menu in sidebar
    $('.sidebar-nav .with-sub').on('click', function(e){
      e.preventDefault();
      $(this).parent().toggleClass('show');

      psSidebar.update();
    })
  }


  $('#mainMenuOpen').on('click touchstart', function(e){
    e.preventDefault();
    $('body').addClass('navbar-nav-show');
  })

  $('#sidebarMenuClose').on('click', function(e){
    e.preventDefault();
    $('body').removeClass('sidebar-show');
  })

  // hide sidebar when clicking outside of it
  $(document).on('click touchstart', function(e){
    e.stopPropagation();

    // closing of sidebar menu when clicking outside of it
    if(!$(e.target).closest('.burger-menu').length) {
      var sb = $(e.target).closest('.sidebar').length;
      var nb = $(e.target).closest('.navbar-menu-wrapper').length;
      if(!sb && !nb) {
        if($('body').hasClass('navbar-nav-show')) {
          $('body').removeClass('navbar-nav-show');
        } else {
          $('body').removeClass('sidebar-show');
        }
      }
    }
  });

})

$(document).ready(function() {
	$('#bftable').dataTable( {
		"language": {
			"sProcessing":	 "Procesando...",
			"sLengthMenu":	 "Mostrar _MENU_ registros",
			"sZeroRecords":	"No se encontraron resultados",
			"sEmptyTable":	 "Ningún dato disponible en esta tabla",
			"sInfo":			"Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
			"sInfoEmpty":	  "Mostrando registros del 0 al 0 de un total de 0 registros",
			"sInfoFiltered":	"(filtrado de un total de _MAX_ registros)",
			"sInfoPostFix":	"",
			"sSearch":		 "Buscar: ",
			"sUrl":			"",
			"sInfoThousands":  ",",
			"sLoadingRecords": "Cargando...",
			"oPaginate": {
				"sFirst":	"<i class='fas fa-angle-double-left' style='color:#f26122;'></i>",
				"sLast":	 "<i class='fas fa-angle-double-right' style='color:#f26122;'></i>",
				"sNext":	 "<i class='fas fa-chevron-right' style='color:#005d98;'></i>",
				"sPrevious": "<i class='fas fa-chevron-left' style='color:#005d98;'></i>"
			},
			"oAria": {
				"sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
				"sSortDescending": ": Activar para ordenar la columna de manera descendente"
			}
		}

	} );
	$('#bftable2').dataTable( {
		"language": {
			"sProcessing":	 "Procesando...",
			"sLengthMenu":	 "Mostrar _MENU_ registros",
			"sZeroRecords":	"No se encontraron resultados",
			"sEmptyTable":	 "Ningún dato disponible en esta tabla",
			"sInfo":			"Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
			"sInfoEmpty":	  "Mostrando registros del 0 al 0 de un total de 0 registros",
			"sInfoFiltered":	"(filtrado de un total de _MAX_ registros)",
			"sInfoPostFix":	"",
			"sSearch":		 "Buscar: ",
			"sUrl":			"",
			"sInfoThousands":  ",",
			"sLoadingRecords": "Cargando...",
			"oPaginate": {
				"sFirst":	"<i class='fas fa-angle-double-left' style='color:#f26122;'></i>",
				"sLast":	 "<i class='fas fa-angle-double-right' style='color:#f26122;'></i>",
				"sNext":	 "<i class='fas fa-chevron-right' style='color:#005d98;'></i>",
				"sPrevious": "<i class='fas fa-chevron-left' style='color:#005d98;'></i>"
			},
			"oAria": {
				"sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
				"sSortDescending": ": Activar para ordenar la columna de manera descendente"
			}
		}

	} );
} );
