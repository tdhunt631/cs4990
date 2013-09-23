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

$(function(){
	$("#item_form").submit(function(e){
		$.ajax({
			url: $(this).attr('action'),
			type: "post",
			data: $(this).serialize(),
			success: function(d) {
				console.log("successful");		
			},
			error: function(){
				console.log("unsuccessful attempt");
			},
		});
		//return false;
	});	
});

$(function(){
	$("#category_form").submit(function(e){
		$.ajax({
			url: $(this).attr('action'),
			type: "post",
			data: $(this).serialize(),
			success: function(d) {
				console.log("successful");		
			},
			error: function(){
				console.log("unsuccessful attempt");
			},
		});
		//return false;
	});	
});



