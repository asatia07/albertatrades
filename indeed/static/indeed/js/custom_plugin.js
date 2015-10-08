jQuery.extend( jQuery.fn.dataTableExt.oSort, {
	"age-custom-sort-pre": function ( age ) {
        untis = parseInt(age.split(" ")[0])
        if (age.search("day") >= 0)
            return untis*60*24
        if (age.search("hour") >= 0)
            return untis*60
        return untis
	},
} );
