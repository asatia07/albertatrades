jQuery(document).ready(function() {
  jQuery('#job_listing').DataTable( {
    "lengthMenu": [[200, 500, 1000, -1], [200, 500, 1000, "All"]],
    "aoColumns": [
      { "sWidth": "58%" }, // 1st column width 
      { "sWidth": "10%" }, // 2nd column width 
      { "sWidth": "20%" }, // 3rd column width 
      //{ "sWidth": "10%", "type": "natural" } // "type": "natural" : had to be removed to apply custom sorting 'age-custom-sort' on age column
      { "sWidth": "10%" } // 4th column width
    ],
    "order": [[ 3, "asc" ]],
    "columnDefs": [ { "type": "age-custom-sort", targets: 3 }]
  });

  $('#query').keyup(function() {
    $('#query').attr('value', $(this).val());
  });
  $('#location').keyup(function() {
    $('#location').attr('value', $(this).val());
  });
});
