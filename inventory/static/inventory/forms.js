$(function(){
	$(".add").click(function(e){

		var prevTD = $(this).closest('td').prev('td');
		
		$.ajax({
			url: $(this).parent().attr('action'),
			type: "post",
			data: $(this).parent().serialize(),
			success: function(d) {
			prevTD.html(d);
			},
			error: function(){
				alert("Ooops! It broke.");
			},
		});

		return false;
	});	
});

$(function(){
	$(".subtract").click(function(e){

		var prevTD = $(this).closest('td').prev('td');
		
		$.ajax({
			url: $(this).parent().attr('action'),
			type: "post",
			data: $(this).parent().serialize(),
			success: function(d) {
			prevTD.html(d);
			},
			error: function(){
				alert("Ooops! It broke.");
			},
		});

		return false;
	});	
});
