$(function(){
	$("#item_form").submit(function(e){
		e.preventDefault();
		$.ajax({
			url: $(this).attr('action'),
			type: "post",
			data: $(this).serialize(),
			success: function(d) {
				$('#listTable').html(d);	
			},
			error: function(d){
				console.log(d);
			},
		});
		return false;
	});	
});

$(function(){
	$("#category_form").submit(function(e){
		e.preventDefault();
		$.ajax({
			url: $(this).attr('action'),
			type: "post",
			data: $(this).serialize(),
			success: function(d) {
				$('#catList').html(d);			
				$('#category_form')[0].reset();
			},
			error: function(){
				console.log("unsuccessful attempt");
			},
		});
		return false;
	});	
});
