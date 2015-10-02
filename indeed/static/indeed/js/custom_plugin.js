jQuery.extend( jQuery.fn.dataTableExt.oSort, {
	"age-custom-sort-pre": function ( age ) {
        untis = parseInt(age.split(" ")[0])
		return (age.search("day") > 0) ? untis*24:untis
	},
} );
