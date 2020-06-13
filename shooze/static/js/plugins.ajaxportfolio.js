window.scwAjaxPortfolioPlugin = window.scwAjaxPortfolioPlugin || {};

let $portfolioAjaxItems			= $('.portfolio-ajax').find('.portfolio-item'),
	$portfolioDetails			= $('#portfolio-ajax-wrap'),
	$portfolioDetailsContainer	= $('#portfolio-ajax-container'),
	$portfolioAjaxLoader		= $('#portfolio-ajax-loader'),
	prevPostPortId				= '';

SEMICOLON.portfolio.ajaxloadInit = function(){
	if( $('.portfolio-ajax').length < 1 ){
		return true;
	}

	$('.portfolio-ajax .portfolio-item a.portfolio-ajax-trigger').off( 'click' ).on( 'click', function(e) {
		var portPostId = $(this).parents('.portfolio-item').attr('id');
		if( !$(this).parents('.portfolio-item').hasClass('portfolio-active') ) {
			SEMICOLON.portfolio.loadItem(portPostId, prevPostPortId);
		}
		e.preventDefault();
	});
};

SEMICOLON.portfolio.newNextPrev = function( portPostId ){
	var portNext = SEMICOLON.portfolio.getNextItem(portPostId);
	var portPrev = SEMICOLON.portfolio.getPrevItem(portPostId);
	$('#next-portfolio').attr('data-id', portNext);
	$('#prev-portfolio').attr('data-id', portPrev);
};

SEMICOLON.portfolio.loadItem = function( portPostId, prevPostPortId, getIt ){
	if(!getIt) { getIt = false; }
	var portNext = SEMICOLON.portfolio.getNextItem(portPostId);
	var portPrev = SEMICOLON.portfolio.getPrevItem(portPostId);
	if(getIt == false) {
		SEMICOLON.portfolio.closeItem();
		$portfolioAjaxLoader.fadeIn();
		var portfolioDataLoader = $('#' + portPostId).attr('data-loader');
		$portfolioDetailsContainer.load(portfolioDataLoader, { portid: portPostId, portnext: portNext, portprev: portPrev },
		function(){
			SEMICOLON.portfolio.initializeAjax(portPostId);
			SEMICOLON.portfolio.openItem();
			$portfolioAjaxItems.removeClass('portfolio-active');
			$('#' + portPostId).addClass('portfolio-active');
		});
	}
};

SEMICOLON.portfolio.closeItem = function(){
	if( $portfolioDetails && $portfolioDetails.height() > 32 ) {
		$portfolioAjaxLoader.fadeIn();
		$portfolioDetails.find('#portfolio-ajax-single').fadeOut('600', function(){
			$(this).remove();
		});
		$portfolioDetails.removeClass('portfolio-ajax-opened');
	}
};

SEMICOLON.portfolio.openItem = function(){
	var noOfImages = $portfolioDetails.find('img').length;
	var noLoaded = 0;

	if( noOfImages > 0 ) {
		$portfolioDetails.find('img').on('load', function(){
			noLoaded++;
			var topOffsetScroll = SEMICOLON.initialize.topScrollOffset();
			if(noOfImages === noLoaded) {
				$portfolioDetailsContainer.css({ 'display': 'block' });
				$portfolioDetails.addClass('portfolio-ajax-opened');
				$portfolioAjaxLoader.fadeOut();
				setTimeout(function(){
					SEMICOLON.widget.loadFlexSlider();
					SEMICOLON.initialize.lightbox({ 'parent': $portfolioDetails });
					SEMICOLON.initialize.resizeVideos();
					SEMICOLON.widget.masonryThumbs();
					$('html,body').stop(true).animate({
						'scrollTop': $portfolioDetails.offset().top - topOffsetScroll
					}, 900, 'easeOutQuad');
				},500);
			}
		});
	} else {
		var topOffsetScroll = SEMICOLON.initialize.topScrollOffset();
		$portfolioDetailsContainer.css({ 'display': 'block' });
		$portfolioDetails.addClass('portfolio-ajax-opened');
		$portfolioAjaxLoader.fadeOut();
		setTimeout(function(){
			SEMICOLON.widget.loadFlexSlider();
			SEMICOLON.initialize.lightbox({ 'parent': $portfolioDetails });
			SEMICOLON.initialize.resizeVideos();
			SEMICOLON.widget.masonryThumbs();
			$('html,body').stop(true).animate({
				'scrollTop': $portfolioDetails.offset().top - topOffsetScroll
			}, 900, 'easeOutQuad');
		},500);
	}
};

SEMICOLON.portfolio.getNextItem = function( portPostId ){
	var portNext = '';
	var hasNext = $('#' + portPostId).next();
	if(hasNext.length != 0) {
		portNext = hasNext.attr('id');
	}
	return portNext;
};

SEMICOLON.portfolio.getPrevItem = function( portPostId ){
	var portPrev = '';
	var hasPrev = $('#' + portPostId).prev();
	if(hasPrev.length != 0) {
		portPrev = hasPrev.attr('id');
	}
	return portPrev;
};

SEMICOLON.portfolio.initializeAjax = function( portPostId ){
	prevPostPortId = $('#' + portPostId);

	$('#next-portfolio, #prev-portfolio').off( 'click' ).on( 'click', function() {
		var portPostId = $(this).attr('data-id');
		$portfolioAjaxItems.removeClass('portfolio-active');
		$('#' + portPostId).addClass('portfolio-active');
		SEMICOLON.portfolio.loadItem(portPostId,prevPostPortId);
		return false;
	});

	$('#close-portfolio').off( 'click' ).on( 'click', function() {
		$portfolioDetailsContainer.fadeOut('600', function(){
			$portfolioDetails.find('#portfolio-ajax-single').remove();
		});
		$portfolioDetails.removeClass('portfolio-ajax-opened');
		$portfolioAjaxItems.removeClass('portfolio-active');
		return false;
	});
};

