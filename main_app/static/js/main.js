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