$(document).ready(function(){
    // Ouvrir le volet coulissant
    $('#open-sidebar').click(function(){
      $('#sidebar').animate({width:'250px'});
      $('#content').animate({marginLeft:'250px'});
    });
  
    // Fermer le volet coulissant
    $('#sidebar-close').click(function(){
      $('#sidebar').animate({width:'0'});
      $('#content').animate({marginLeft:'0'});
    });
  });
  