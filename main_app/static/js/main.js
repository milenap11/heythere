// const elemsBtns = document.querySelectorAll(".fixed-action-btn");
// const floatingBtn = M.FloatingActionButton.init(elemsBtns, {
//   direction: "left",
//   hoverEnabled: false
// });

// const elemsDropdown = document.querySelectorAll(".dropdown-trigger");
// const instancesDropdown = M.Dropdown.init(elemsDropdown, {
//   coverTrigger: false
// });

elemsSidenav = document.querySelectorAll(".sidenav");
const instancesSidenav = M.Sidenav.init(elemsSidenav, {
  edge: "left"
});

document.addEventListener('DOMContentLoaded', function() {
  const elems = document.querySelectorAll('.dropdown-trigger');
  const instances = M.Dropdown.init(elems, {
    CoverTrigger: false
  });
});