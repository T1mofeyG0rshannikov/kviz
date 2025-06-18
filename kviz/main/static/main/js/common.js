var kviz = 0

function closeModal(){
	$(".modal").removeClass("zoom-in").addClass("zoom-out");

	setTimeout(() => {
		$(".modal").removeClass("active")
	}, 500);

	setTimeout(() => {
		$(".modal-overlay").removeClass("active");
		$("body").removeClass("body_modal");
	}, 500);
	progressBarPercent = 0;
	modalIndex = 0;
	updateProgressBar();
}

function openInteres(){
	fetch(`/create-kviz`, {
		method: "POST",
		headers: {
			'Content-Type': 'application/x-www-form-urlencoded',
		},
		body: `client_id=${client}`
	}).then(response => response.json()).then(
		response => {
			kviz = response.kviz
		}
	)

	if ($("#modalinteres").hasClass("active")) {
		$("#modalinteres").removeClass("active").removeClass("zoom-in").addClass("zoom-out");
		$(".modal-overlay").removeClass("active");
		$("body").removeClass("body_modal");
	} else {
		$("#modalinteres").addClass("zoom-in").removeClass("zoom-out").addClass("active");
		$(".modal-overlay").addClass("active");
		$("body").addClass("body_modal");
	}

	updateProgressBar();
}

//progressbar
var progressBarPercent = 0;
function updateProgressBar() {
	var $modals = $('.modal');
	var $activeModal = $modals.filter('.active');
	var index = $modals.index($activeModal);
	$activeModal.closest('form').trigger('reset')
	const maxsteps = +$activeModal.attr('data-maxsteps')
	const $buttons = $activeModal.find(".modal__buttons").first();
	if ($buttons.attr("data-hide") !== "false"){
		$buttons.css("display", "none")
	}
	const $next = $buttons.find(".next-modal").first();
	if ($next.attr("data-hide") !== "false"){
		$next.css("display", "none")
	}
	
	/*if ($activeModal.attr("data-moda") == "-callback" || $activeModal.attr("data-modal") == "-cooperation"){

	}*/
	$activeModal.find('.checkbox_another').each(function(){
		this.classList.remove("active")
	});
		
	if (index !== -1) {
		if (isNaN(maxsteps)){
			progressBarPercent = 0;
		}
		else{
			console.log(((modalIndex + 1) / (modalIndex + 1 + maxsteps)) * 100)
			console.log(progressBarPercent)
			var percent = Math.max(((modalIndex + 1) / (modalIndex + 1 + maxsteps)) * 100, progressBarPercent);
			progressBarPercent = percent;
			console.log(progressBarPercent)
			$activeModal.find('.progressbar__value').css('width', percent + '%');
		}
	}
}

$(document).ready(function () {
	setTimeout(() => {
		$('.open-modal').click()
	}, 1400)

	const $marquee = $('.marquee');
	const speed = 60; 

	const text = $marquee.html();
	while ($marquee[0].scrollWidth < $marquee.parent().width() * 60) {
		$marquee.append(text);
	}

	const scrollWidth = $marquee[0].scrollWidth;
	const duration = scrollWidth / speed;

	$marquee.css({
		'animation-duration': duration + 's',
		'width': scrollWidth + 'px'
	});


	//mask
	$(".input-phone").mask("+7 (999) 999-99-99");

	//share
	  $('.share-unit').on('click', function () {
		const $btn = $(this);
		const text = $btn.find('.share-unit__value').text().trim();

		const tempInput = $('<input>');
		$('body').append(tempInput);
		tempInput.val(text).select();
		document.execCommand('copy');
		tempInput.remove();

		let $tooltip = $('<div class="copy-tooltip">Ссылка скопирована</div>');
		$btn.append($tooltip);
		setTimeout(() => $tooltip.addClass('active'), 10); 

		setTimeout(() => {
		$tooltip.removeClass('active');
		setTimeout(() => $tooltip.remove(), 300); 
		}, 1500);
  });

	$(".modal__close").click(function (e) {
		e.preventDefault();
		closeModal()
	});

	//modals
	$(".open-modal").click(function (e) {
		e.preventDefault();

		fetch(`/kviz-count?client_id=${client}`, {
			method: "GET",
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded',
			}
		}).then(response => response.json()).then(
			response => {
				kviz_count = response.kviz_count
				console.log(kviz_count)

				if (kviz_count > 0){
					$("#modalrepeat").addClass("zoom-in").removeClass("zoom-out").addClass("active");
					$(".modal-overlay").addClass("active");
					$("body").addClass("body_modal");
				}
				else{
					openInteres()
				}
			}
		)
	});

$(".prev-modal").click(function (e) {
	e.preventDefault();
	modalIndex--;
	console.log(modalIndex)
	console.log(modalsHistory)
	console.log(modalsHistory[modalIndex])

	var $currentTab = $(this).parents(".modal");
	$currentTab.removeClass("active").removeClass("zoom-in").addClass("zoom-out");
	$(document.getElementById(modalsHistory[modalIndex])).addClass("active").addClass("zoom-in").removeClass("zoom-out");

	updateProgressBar();
});
$('.another-input').on('input', function (e) {
	e.preventDefault();
	$(this).parents('.modal').find(".modal__buttons").first().css("display", "flex");
	$(this).parents('.modal').find(".next-modal").first().css("display", "flex");
})
$(".next-modal").click(function (e) {
	e.preventDefault();
	modalIndex++;

	var fieldsToUpdate = [];
	var valuesToUpdate = [];

	var $currentTab = $(this).parents(".modal");
	const newModalName = `modal${$($currentTab).attr('data-modal')}`;
	var $nextTab = document.getElementById(newModalName);

	const textField = $currentTab.find('input[type=text], input[type=number]').first();
	if (textField.val() && textField.val().length > 0){
		if (textField.hasClass("another-input")){
			fieldsToUpdate.push(textField.attr('data-field'));
		}
		else{
			fieldsToUpdate.push($currentTab.attr('data-field'));
		}
		valuesToUpdate.push(textField.val())
	}
	console.log(modalIndex >= modalsHistory.length);
	if (modalIndex >= modalsHistory.length){
		modalsHistory.push(newModalName)
	}
	console.log(modalIndex);
	console.log(modalsHistory);

	const type = $currentTab.attr('data-type');
	let inputs = $currentTab.find("input[type=checkbox], input[type=radio]");

	if (type === "checkbox"){
		inputs.each(function(){
			fieldsToUpdate.push($(this).attr('data-field'))
			valuesToUpdate.push(this.checked)
		});
	}
	sendAnswer(kviz, fieldsToUpdate, valuesToUpdate)

	if ($currentTab.find('input[type="radio"], input[type="checkbox"]').length > 0) {

		const isChecked = $currentTab.find('input[type="radio"]:checked, input[type="checkbox"]:checked').length > 0;
		const $another = $currentTab.find('.checkbox_another input[type="text"]');
		const anotherHasText = $another.length > 0 && $another.val().trim() !== "";

		if (isChecked || anotherHasText) {
			$currentTab.removeClass("active zoom-in").addClass("zoom-out");
			$($nextTab).addClass("active zoom-in").removeClass("zoom-out");
		}
	} else {
		$currentTab.removeClass("active zoom-in").addClass("zoom-out");
		$($nextTab).addClass("active zoom-in").removeClass("zoom-out");
	}

	if ($(".modal_success").hasClass("active")) {
		setTimeout(() => {
			$(".modal_success").removeClass("active flip-in").addClass("flip-out");
			$(".modal_success").next(".modal").addClass("active flip-in").removeClass("flip-out");
		}, 2000);
	}

	updateProgressBar();
});

	$('.modal').on('click', '.radio input[type="radio"]', function () {
		var $currentTab = $(this).parents('.modal');
		const newModalName = `modal${$(this).attr('data-modal')}`

		var $nextTab = document.getElementById(newModalName);

		modalIndex++;

		sendAnswer(kviz, [$currentTab.attr('data-field')], [$(this).attr('data-value')])

		if ($nextTab) {
			if (modalIndex >= modalsHistory.length){
				modalsHistory.push(newModalName)
			}
			$currentTab.removeClass("active").removeClass("zoom-in").addClass("zoom-out");
			$($nextTab).addClass("active").addClass("zoom-in").removeClass("zoom-out");
		}
		console.log(modalIndex)
		console.log(modalsHistory)

		if ($(".modal_success").hasClass("active")) {
			setTimeout(() => {
				$(".modal_success").removeClass("active").removeClass("flip-in").addClass("flip-out");
				$(".modal_success").next(".modal").addClass("active").addClass("flip-in").removeClass("flip-out");
			}, 1400);
		}

		updateProgressBar();
	});

	$('.modal').each(function () {
		if ($(this).find('input[type="checkbox"]').length > 0) {
			$(this).addClass("no-filled");
		}
	});

	$('.modal').on('change input', '.checkbox input[type="checkbox"], .checkbox input[type="text"]', function () {
		var $currentTab = $(this).closest('.modal');
		var hasChecked = $currentTab.find('.checkbox input[type="checkbox"]:checked').length > 0;
		var hasText = false;

		$currentTab.find('.checkbox input[type="text"]').each(function () {
			if ($(this).val().trim() !== '') {
				hasText = true;
				return false;
			}
		});

		if (hasChecked || hasText) {
			$currentTab.removeClass("no-filled").addClass('filled');
		} else {
			$currentTab.removeClass('filled').addClass("no-filled");
		}
	});

	$('.radio_cooperation').click(function (e) {
		var $currentTab = $(this).parents('.modal');

		$currentTab.removeClass("active").removeClass("zoom-in").addClass("zoom-out");
		$("#modal-cooperation").addClass("active").addClass("zoom-in").removeClass("zoom-out");

		updateProgressBar();
	});

	$('.checkbox__click').click(function (e) {
		$(this).parents('.checkbox_another').toggleClass("active");
	});

	$('#modal-cooperation .btn-main').click(function (e) {

		const $form = $(this).closest('form');
		let isValid = true;

		var data = $form.serializeArray();
		let fieldsToUpdate = [];
		let valuesToUpdate = [];

		for (let p of data){
			fieldsToUpdate.push(p.name);
			valuesToUpdate.push(p.value);
		}

		sendAnswer(kviz, fieldsToUpdate, valuesToUpdate)

		$form.find('input[required]').each(function () {
			if ($(this).val().trim() === '') {
				isValid = false;
			}
		});

		if (isValid) {
			e.preventDefault();
			var $currentTab = $(this).parents('.modal');

			$currentTab.removeClass("active").removeClass("zoom-in").addClass("zoom-out");
			$(".modal_success").addClass("active").addClass("zoom-in").removeClass("zoom-out");
		}
		updateProgressBar();
	});

	$('#modal-callback .btn-main').click(function (e) {

		const $form = $(this).closest('form');
		let isValid = true;

		$form.find('input[required]').each(function () {
			if ($(this).val().trim() === '') {
				isValid = false;
			}
		});

		if (isValid) {
			const data = $form.serializeArray()

			let fieldsToUpdate = [];
			let valuesToUpdate = [];

			for (let p of data){
				fieldsToUpdate.push(p.name);
				valuesToUpdate.push(p.value);
			}

			sendAnswer(kviz, fieldsToUpdate, valuesToUpdate)

			e.preventDefault();
			var $currentTab = $(this).parents('.modal');

			$currentTab.removeClass("active").removeClass("zoom-in").addClass("zoom-out");
			$(".modal_success").addClass("active").addClass("zoom-in").removeClass("zoom-out");

			setTimeout(() => {
				$(".modal_success").removeClass("active").removeClass("flip-in").addClass("flip-out").removeClass("zoom-in").removeClass("zoom-out");
				$(".modal_success").next(".modal").addClass("active").addClass("flip-in").removeClass("flip-out").removeClass("zoom-in").removeClass("zoom-out");
			}, 1400);
		}
		updateProgressBar();
	});

	//name
	  $('.input-name').on('input', function() {
		const name = $(this).val().trim();
		$('.title-share span').text(name !== '' ? name : 'Имя');
	}); 

});


if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
  document.body.classList.add('theme-dark');
}
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
  if (e.matches) {
    document.body.classList.add('theme-dark');
  } else {
    document.body.classList.remove('theme-dark');
  }
});

function checkAspectRatio() {
  const width = window.innerWidth;
  const height = window.innerHeight;
  const ratio =  height / width;

  const body = document.body;

  if (ratio >= 2) {
    body.classList.add('hight-ratio');
  } else {
    body.classList.remove('hight-ratio');
  }
}

// Выполнить при загрузке
checkAspectRatio();

// И при изменении размера окна
window.addEventListener('resize', checkAspectRatio);

function scaleLayout() {
  const layout = document.querySelector('.layout');
  const scaleX = window.innerWidth / 320;
  const scaleY = window.innerHeight / 568;
  const scale = Math.min(scaleX, scaleY);

  /*layout.style.transform = `scale(${scale})`;*/

  layout.classList.add('layout_visible'); 
}

window.addEventListener('resize', scaleLayout);
window.addEventListener('load', scaleLayout);

var modalsHistory = ["modalinteres"];
var modalIndex = 0;


$(".theme-change").on('click', function(){
	if (document.body.classList.contains("theme-dark")){
		document.body.classList.remove("theme-dark")
		document.getElementById("moon").style.display = "block"
		document.getElementById("sun").style.display = "none"
	}
	else{
		document.getElementById("sun").style.display = "block"
		document.getElementById("moon").style.display = "none"
		document.body.classList.add("theme-dark")
	}
})