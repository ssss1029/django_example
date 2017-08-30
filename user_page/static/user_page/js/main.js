$(document).ready(function() { 
	$('.form').find('input, textarea').on('keyup blur focus', function (e) {
		
		var $this = $(this),
				label = $this.prev('label');

			if (e.type === 'keyup') {
				if ($this.val() === '') {
						label.removeClass('active highlight');
					} else {
						label.addClass('active highlight');
					}
			} else if (e.type === 'blur') {
				if( $this.val() === '' ) {
					label.removeClass('active highlight'); 
				} else {
					label.removeClass('highlight');   
				}   
			} else if (e.type === 'focus') {
				
				if( $this.val() === '' ) {
					label.removeClass('highlight'); 
				} 
				else if( $this.val() !== '' ) {
					label.addClass('highlight');
				}
			}

	});

	$('.tab a').on('click', function (e) {
		e.preventDefault();
		
		$(this).parent().addClass('active');
		$(this).parent().siblings().removeClass('active');
		
		target = $(this).attr('href');

		$('.tab-content > div').not(target).hide();
		
		$(target).fadeIn(600);
		
	}); 

	$('#submit_new_favorite_book').on('click', function(e) {
		e.preventDefault();

		var title               = $('#title_input').val();
		var author              = $('#author_input').val();
		var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

		console.log("Sending: " + title + ", by " + author);

		if (title == "" || author == "") {
			// There is a mistake
			alert("Please complete the form before submitting. Both the author and title are required")
		} else {
			// Good to go. Send to server
			/**
			 * This part is actually pretty intricate to understand. Here are the main points I could gather from various docs: 
			 *	 - jQuery's $.ajax() actually sends cookies with the payload data to any POST request. This is why we can get the logged-in user as request.user in the Django backend. This is just a nice feature of jQuery's $.ajax() function.
			 *   - We need to send the csrfmiddlewaretoken along with every request. If you inspect element/view source, you can see that we have a hidden text <input> with a name=csrfmiddlewaretoken and a random string for a value. This is pre-set by Django in order to stop CSRF attacks (read more about how you can do a CSRF attack online). If you look at the source code for index.html on the Django template, there is a {% csrf_token %} tag, and all it does is drop the csrfmiddlewaretoken <input> into our html page. All we have to do to take advantage of this security is send the csrfmiddlewaretoken value with every request we make to the backend.
			 **/
			var request = $.ajax({
				url : '/user_page/processChange/',
				method : 'POST',
				data : {
					'title'               : title,
					'author'              : author, 
					'csrfmiddlewaretoken' : csrfmiddlewaretoken
				}
			}).done(function(msg) {
				console.log(msg)
			}).fail(function(jqXHR, textStatus) {
				console.log("Failed: " + textStatus)
			});
		}
	});
});