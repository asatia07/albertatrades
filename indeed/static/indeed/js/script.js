
jQuery(document).ready(function() {
    jQuery('#trades').DataTable( {
        "lengthMenu": [[25, 50, 100, -1], [25, 50, 100, "All"]],        
    } );
    jQuery('#job_listing').DataTable( {
        "lengthMenu": [[200, 500, 1000, -1], [200, 500, 1000, "All"]],
         "aoColumns": [
              { "sWidth": "58%" }, // 1st column width 
              { "sWidth": "10%" }, // 2nd column width 
              { "sWidth": "20%" }, // 3rd column width 
              { "sWidth": "10%" } // 4th column width
            ]
    } );
} );
