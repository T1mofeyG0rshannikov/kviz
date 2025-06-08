$(document).ready(function () {
	setTimeout(() => {
		$('.open-modal').click()
	}, 1400)

	//marquee
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

	//progressbar
	function updateProgressBar() {
		var $modals = $('.modal');
		var $activeModal = $modals.filter('.active');
		var index = $modals.index($activeModal);
		var total = $modals.length;

		if (index !== -1) {
			var percent = ((index + 1) / total) * 100;
			$activeModal.find('.progressbar__value').css('width', percent + '%');
		}
	}

	$(".modal__close").click(function (e) {
		e.preventDefault();
		$(".modal").removeClass("zoom-in").addClass("zoom-out");

		setTimeout(() => {
			$(".modal").removeClass("active")
		}, 500);

		setTimeout(() => {
			$(".modal-overlay").removeClass("active");
			$("body").removeClass("body_modal");
		}, 500);

		updateProgressBar();
	});

	//modals
	$(".open-modal").click(function (e) {
		e.preventDefault();
		if ($(".modals-wrap .modal:first-child").hasClass("active")) {
			$(".modals-wrap .modal:first-child").removeClass("active").removeClass("zoom-in").addClass("zoom-out");
			$(".modal-overlay").removeClass("active");
			$("body").removeClass("body_modal");
		} else {
			$(".modals-wrap .modal:first-child").addClass("zoom-in").removeClass("zoom-out").addClass("active");
			$(".modal-overlay").addClass("active");
			$("body").addClass("body_modal");
		}

		updateProgressBar();
	});

$(".prev-modal").click(function (e) {
	e.preventDefault();
	modalIndex--;

	var $currentTab = $(this).parents(".modal");
	$currentTab.removeClass("active").removeClass("zoom-in").addClass("zoom-out");
	$(document.querySelectorAll('.modal')[modalIndex]).addClass("active").addClass("zoom-in").removeClass("zoom-out");

	updateProgressBar();
});

$(".next-modal").click(function (e) {
	e.preventDefault();
	modalIndex++;

	var $currentTab = $(this).parents(".modal");
	const newModalName = `modal${$($currentTab).attr('data-modal')}`;
	var $nextTab = document.getElementById(newModalName);
	console.log(newModalName);
	console.log($nextTab);

	const textField = $currentTab.find('input[type=text]').first();
	console.log(textField);
	console.log(textField.val());
	console.log($currentTab.attr('data-field'))
	if (textField.val() && textField.val().length > 0){
		sendAnswer(kviz, [$currentTab.attr('data-field')], [textField.val()])
	}
	if (modalIndex >= modalsHistory.length){
		modalsHistory.push(newModalName)
	}
	const type = $currentTab.attr('data-type');
	let inputs = $currentTab.find("input");
	console.log(inputs)
	if (type === "checkbox"){
		let checkedInputs = [];
		inputs.each(function(){
			if (this.checked){
				checkedInputs.push($(this).attr('data-field'))
			}
		});
		sendAnswer(kviz, checkedInputs, Array(checkedInputs.length).fill(true))
	}
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
		console.log('click')
		var $currentTab = $(this).parents('.modal');
		const newModalName = `modal${$(this).attr('data-modal')}`

		console.log($(this).attr('data-modal'));
		console.log(newModalName)
		var $nextTab = document.getElementById(newModalName);

		console.log($nextTab)
		modalIndex++;

		if ($nextTab) {
			if (modalsHistory.length === 1){
				modalsHistory.push(newModalName)
			}
			$currentTab.removeClass("active").removeClass("zoom-in").addClass("zoom-out");
			$($nextTab).addClass("active").addClass("zoom-in").removeClass("zoom-out");
			console.log(kviz)
			console.log($currentTab.attr('data-field'))
			console.log($(this).attr('data-value'))
			sendAnswer(kviz, [$currentTab.attr('data-field')], [$(this).attr('data-value')])
		}

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

  layout.style.transform = `scale(${scale})`;

  layout.classList.add('layout_visible'); 
}

window.addEventListener('resize', scaleLayout);
window.addEventListener('load', scaleLayout);

var modalsHistory = ["modalfirst"];
var modalIndex = 0;