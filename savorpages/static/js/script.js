// jQuery code for navbar, modal and category select functionality

$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('.dropdown-trigger').dropdown({hover: true});  
    $('.fixed-action-btn').floatingActionButton({direction: 'right', hoverEnabled: false});
    $('.modal').modal();
    $('select').formSelect();
  });

//  Updates current year in the footer
const currentYear = document.querySelector("#current-year");
currentYear.innerText = new Date().getFullYear();

