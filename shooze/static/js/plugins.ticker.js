window.scwTickerPlugin = window.scwTickerPlugin || {};

SEMICOLON.widget.tickerInit = function( $tickerEl ){

	$tickerEl = $tickerEl.filter(':not(.customjs)');

	if( $tickerEl.length < 1 ){
		return true;
	}

	$tickerEl.each( function(){

		let element			= $(this),
			elItem			= element.find('.scw-ticker-item'),
			elWidth			= 0,
			elCount			= elItem.length,
			eltickerWidth	= 0,
			elementSpeed	= element.attr('data-speed') || 30000,
			elementHover	= element.attr('data-hover'),
			elItems			= element.attr('data-items') || 5,
			elItemsXl		= element.attr('data-items-xl') || Number(elItems),
			elItemsLg		= element.attr('data-items-lg') || Number(elItemsXl),
			elItemsMd		= element.attr('data-items-md') || Number(elItemsLg),
			elItemsSm		= element.attr('data-items-sm') || Number(elItemsMd),
			elItemsXs		= element.attr('data-items-xs') || Number(elItemsSm);

		elWidth = windowWidth / elItems;
		eltickerWidth = ( elWidth * elCount );

		element.find('.scw-ticker-wrap').after('<div class="scw-ticker-wrap-clone"></div>');

		let elementWrap = element.find('.scw-ticker-wrap,.scw-ticker-wrap-clone');

		elItem.css({ 'width':elWidth });

		setTimeout( function(){
			elementWrap.css({ 'width': eltickerWidth });
			element.css({ 'width': (eltickerWidth*2) });
			elItem.clone().appendTo( element.find('.scw-ticker-wrap-clone') );
		}, 300);

		if( elementHover == 'false' ) { elementHover = false; } else { elementHover = true; }

		let speedFactor = eltickerWidth / windowWidth;

		elementWrap.css({ 'animation-duration': ( Number(elementSpeed)*speedFactor )+'ms' });

		if( elementHover == true ) {
			element.on( 'mouseover', function(){
				elementWrap.addClass('scw-ticker-paused');
			});

			element.on( 'mouseout', function(){
				elementWrap.removeClass('scw-ticker-paused');
			});
		}
	});

};

