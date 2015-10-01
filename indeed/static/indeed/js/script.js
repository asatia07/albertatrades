jQuery(document).ready(function() {
  jQuery('#job_listing').DataTable( {
    "lengthMenu": [[200, 500, 1000, -1], [200, 500, 1000, "All"]],
    "aoColumns": [
      { "sWidth": "58%" }, // 1st column width 
      { "sWidth": "10%" }, // 2nd column width 
      { "sWidth": "20%" }, // 3rd column width 
      { "sWidth": "10%", "type": "natural" } // 4th column width
    ],
    "order": [[ 3, "asc" ]]
  });
});
