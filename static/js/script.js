(function () {
  'use strict';

  /**
   * CONSTRUCTOR
   * SITE SEARCH
   * MODAL ACCOUNT
   * MODAL MAP
   * MASKS FOR INPUTs
   * VALIDATION FORM
   * BOOKING FORMs
   * CUSTOM SELECT
   * RATINGS
   * HOME PAGE - MAIN SLIDER
   * HOME PAGE - SEARCHBAR
   * CATEGORY - SIDEBAR
   * CATEGORY - SORTBAR
   * CATEGORY - GRID LIST
   * CATEGORY - ITEM BANNER
   * HOTEL - SIDEBAR SEARCH
   * HOTEL - FORM CHANGE
   * GRID MASONRY FOR SORTING
   * HOTEL GALLERY
   */

  var isIE11 = !!window.MSInputMethodContext && !!document.documentMode;

  var small = 992;
  var debounce;

  var $window = $(window);
  var $html = $('html');
  var $body = $('body');
  var $header = $('.page-header');
  var $headerTop = $('.js-header-top');
  var $main = $('.page-main');
  var $pageContent = $('.page-content');
  var $footer = $('.page-footer');
  var $sidebarFilter = $('#sidebarFilter');
  var $stickyTop = $('.js-sticky-top');
  var $btnUp = $('.js-scroll-up');
  var $introContent = $('.js-intro-content');

  window.isMobile = false;

  if (/Android|webOS|iPhone|iPod|iPad|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    window.isMobile = true;
  }

  if (isIE11) {
    $html.addClass('ie11');
  }

  if (window.isMobile) {
    $html.addClass('mobile');
  }

  // OBJECT-FIT POLYFILL RUN
  objectFitImages();

  /**
   * https://github.com/nk-o/jarallax
   */
  var prlx = new jarallax(document.querySelectorAll('.jarallax'));
  var prlxKeep = new jarallax(document.querySelectorAll('.jarallax-keep-img'), {
    keepImg: true
  });

  $('.js-tooltip-call').tooltip();

  $('[data-toggle="popover"]').popover();

  $('.js-scrollbar').mCustomScrollbar({
    scrollInertia: 200,
    scrollButtons: {
      enable: true
    }
  });

  /**
   * CONSTRUCTOR
   */
  var App = (function (window) {
    return {
      init: function () {
        $body.removeClass('load');

        this.siteMenu();
        this.btnLoader();
        this.progressBars();
        this.dropdownOffset();
        this.buttonScrolls();
      },

      scroll: function () {
        this.scrollIntro();
        this.scrollAnim();

        var $fromTop = $pageContent.offset().top - $header.height();
        var $fromBottom = $body.height() - $window.height() - $footer.height();

        if ($window.scrollTop() > $header.height()) {
          $headerTop.addClass('fixed-top-active');
        } else {
          $headerTop.removeClass('fixed-top-active');
        }

        if ($window.scrollTop() > $fromTop) {
          $btnUp.fadeIn();
        } else {
          $btnUp.fadeOut();
        }

        if ($window.scrollTop() > $fromBottom) {
          $btnUp.addClass('bottom');
        } else {
          $btnUp.removeClass('bottom');
        }
      },

      resize: function () {
        this.scrollPanels();
        this.resizeIntro();
        this.dropdownOffset();

        if (!isIE11) {
          this.stickyFooter();
        }
      },

      resizeIntro: function () {
        $introContent.css({
          minHeight: 'calc(100vh - ' + $header.height() + 'px)'
        });
      },

      scrollIntro: function () {
        var $introBg = $('.js-intro-bg');
        var $introH = $('.intro').height();

        var $scrollDown = $introH + $header.height();

        if ($scrollDown > $window.scrollTop()) {
          $introBg.addClass('sticky');
        } else {
          $introBg.removeClass('sticky');
        }
      },

      stickyFooter: function () {
        $main.css({
          marginBottom: $footer.height() + 'px'
        });
        $footer.addClass('sticky');
      },

      scrollAnim: function () {
        var $wTop = $window.scrollTop();

        $('.prlx-scroll').each(function () {
          var $this = $(this);

          var $fromTop = $this.offset().top;
          var $elHeight = $this.height();

          var opacity = -((1 - ($fromTop - $wTop) / $elHeight) / 2) + 0.4;

          if (opacity > 1) {
            opacity = 1;
          } else if (opacity < 0) {
            opacity = 0;
          }

          $this.css({
            opacity: opacity
          });
        });
      },

      scrollPanels: function () {
        var $h = $headerTop.height();

        var $panels = [];
        var $sum = 0;

        $('.js-top-panel').each(function (index, el) {
          $panels[index] = $(this).height();

          $sum += $panels[index];
        });

        $headerTop.waypoint({
          handler: function (direction) {
            $headerTop.addClass('fixed-top');
            $headerTop.parent().css('height', $h);
          },
          offset: 0
        });

        if ($stickyTop.length && !isIE11) {
          $stickyTop.stick_in_parent({
            offset_top: $sum + 10
          });
        }
      },

      btnLoader: function () {
        var $button = $('.btn-load');
        var $spinner = '<i class="spinner"></i>';
        var $checked = '<i class="fa fa-check"></i>';

        $button.on('click', function () {
          var $this = $(this);
          $this.addClass('loading').html($spinner);

          setTimeout(function () {
            $this.removeClass('loading').addClass('complete').html($checked);
          }, 1500);
        });
      },

      progressBars: function () {
        $('.js-point-progress').each(function () {
          var $this = $(this);
          $this.waypoint(function (direction) {
            if (direction === 'down') {
              $this.find('.progress-bar').css("width", function () {
                return $(this).attr("aria-valuenow") + "%";
              });
            }
          }, {
            offset: $window.height() / 3
          });
        });
      },

      siteMenu: function () {
        var $navPanel = $('#navPanel');
        var $navMenu = $('#navMenu');
        var $backdrop = '<div class="modal-backdrop show"></div>';
        var $toggleMenu = $('.btn-toggle-nav');

        $navPanel
          .on('show.bs.collapse', function () {
            $body.addClass('modal-open menu-open').append($backdrop);
            $navPanel.css('transition', 'transform 300ms ease-in-out 150ms');
            $toggleMenu.css('transition', 'transform 300ms ease-in-out 150ms');
          })
          .on('hide.bs.collapse', function () {
            $body.removeClass('menu-open');

            $('.modal-backdrop').animate({
              opacity: 0
            }, 300, function () {
              $(this).remove();
              $body.removeClass('modal-open');
            });
          })
          .on('hidden.bs.collapse', function () {
            $navPanel.css('transition', 'transform 0s 0s');
            $toggleMenu.css('transition', 'transform 0s 0s');
          });

        $body.on('click', '.modal-backdrop', function () {
          $navPanel.collapse('hide');
          $body.removeClass('menu-open');

          $(this).animate({
            opacity: 0
          }, 300, function () {
            $(this).remove();
            $body.removeClass('modal-open');
          });
        });

        $navMenu.on('click', 'a', function (e) {
          var $this = $(this);

          if ($this.attr('href') === '#') {
            e.preventDefault();

            $this.next().slideToggle(300).parent().toggleClass('show')
              .siblings().removeClass('show')
              .children('.dropdown-menu').slideUp(300);
          }
        });
      },

      dropdownOffset: function () {
        $('.dropdown-menu .dropdown-menu').each(function () {
          var $drop = $(this);
          var $dropW = $drop.width();
          var $dropL = $drop.offset().left;

          if ($window.width() > 767) {
            if ($window.width() < $dropW + $dropL) {
              $drop.css({
                left: '-100%'
              });
            } else if ($dropL < $dropW) {
              $drop.css({
                left: '100%'
              });
            }
          }
        });
      },

      buttonScrolls: function () {
        $('.js-intro-btn-jump').on('click', function (e) {
          var $introSearch = $introContent.find('.intro__search').innerHeight();
          var $top = $introContent.offset().top;

          $('html, body').animate({
            scrollTop: $top - ($window.height() - $introSearch) / 2
          }, 500);
        });

        $btnUp.on('click', function (e) {
          e.preventDefault();

          if ($(this).hasClass('bottom')) {
            $('html, body').animate({
              scrollTop: 0
            }, 1000, 'swing');
          } else {
            $('html, body').animate({
              scrollTop: $body.height()
            }, 1000, 'swing');
          }
        });

        $('.js-nav-scroll').on('click', 'a', function (e) {
          e.preventDefault();

          var target = this.hash;
          var $target = $(target);

          $('html, body').animate({
            scrollTop: $target.offset().top - ($headerTop.height() + 10)
          }, 600, 'swing');

          window.location.hash = target;
        });
      }
    };
  })(window);

  /**
   * Custom collapse
   */
  function filterModalClose() {
    if ($sidebarFilter.hasClass('show')) {
      $sidebarFilter.modal('hide');
    }
  }

  $(window).on('resize', function () {
    App.resize();

    clearTimeout(debounce);

    debounce = setTimeout(function () {
      if ($(window).width() > small) {
        filterModalClose();
      }
    }, 200);
  });

  $(window).on('scroll', function () {
    App.scroll();
  });

  $(document).ready(function () {
    App.init();
    App.resize();

    /*
     * MODAL MAP
     */
    $('#modalMap').on('show.bs.modal', function (event) {
      var button = $(event.relatedTarget);
      var title = button.data('title');
      var modal = $(this);

      modal.find('.modal-title .title').text(title);
    });

    /*
     * MASKS FOR INPUTs
     */
    $('#zip').mask('00000-000');
    $('#card_number').mask('0000-0000-0000-0000');
    $('#card_date').mask('0000/00');
    $('#card_cv2').mask('000');
    $('#phone').mask('(000) 000-0000');

    /**
     * VALIDATION FORM
     * https://github.com/1000hz/bootstrap-validator
     */
    $.fn.validator.Constructor.FOCUS_OFFSET = $headerTop.height() + 10;

    /**
     * BOOKING FORMs
     */
    $('.js-form-booking-example').validator().on('submit', function (e) {
      if (e.isDefaultPrevented()) {} else {
        e.preventDefault();
        window.location = $(this).data('next');
      }
    });

    // Active form for demo
    $('.js-form-booking').on('submit', function (e) {
      e.preventDefault();
      window.location = $(this).data('next');
    });

    /**
     * CUSTOM SELECT
     */
    $('.select2').on('select2:open', function (e) {
      var $selectOptions = $('.select2-results__options');

      $selectOptions.mCustomScrollbar('destroy');

      $('.select2-search input').prop('focus', false);

      setTimeout(function () {
        $selectOptions.mCustomScrollbar({
          scrollInertia: 200,
          scrollButtons: {
            enable: true
          }
        });
      }, 0);
    });

    $('.js-form-select').each(function () {
      $(this).select2({
        width: '100%',
        minimumResultsForSearch: Infinity
      });
    });

    /**
     * SITE SEARCH
     */
    var $navbarSearch = $('#navbarSearch');
    var $navbarSearchInput = $navbarSearch.find('.form-control');

    $navbarSearch.on('shown.bs.collapse', function () {
      $navbarSearchInput.focus();
    });

    $navbarSearch.on('hidden.bs.collapse', function () {
      $navbarSearchInput.blur();
    });

    /**
     * MODAL ACCOUNT
     */
    var $modalAccount = $('#modalAccount');

    $modalAccount.on('hide.bs.modal', function () {
      var $this = $(this);

      $this.find('.form-group').removeClass('has-error');
      $this.find('.js-help-block').remove();
    });

    var $accountForm = $('.js-account-form');

    $accountForm.validator().on('submit', function (e) {
      if (e.isDefaultPrevented()) {} else {
        e.preventDefault();

        window.location = 'index.html';
      }
    });

    $accountForm.find('.form-control').on('focus change', function () {
      errMessage($(this).closest('form'));
    });

    $accountForm.on('submit', function () {
      errMessage($(this));
    });

    /**
     * @param {object} $el - object $()
     */
    function errMessage($el) {
      var $errMessage = $el.find('.js-help-block');
      var $helpBlock = '<div class="alert alert-danger ' +
        'js-help-block collapse"></div>';

      var $err = $el.find('.has-error').eq(0).find('.help-block').text();

      if ($err.length) {
        $errMessage.text($err).collapse('show');
      } else {
        $errMessage.collapse('hide');
      }

      if ($el.find($('.js-help-block')).length < 1) {
        $el.prepend($helpBlock);
      }
    }

    $('.js-toggle-account').on('click', function (e) {
      e.preventDefault();

      var $this = $(this).data('account');

      switch ($this) {
        case 'login':
          $('a[href="#accountLogin"]').tab('show');
          break;
        case 'regist':
          $('a[href="#accountRegist"]').tab('show');
          break;
        case 'forgot':
          $('a[href="#accountForgot"]').tab('show');
          break;
        default:
          break;
      }
    });

    /**
     * RATINGS
     */
    var $ratingFilter = $('.js-rating-filter');
    var $ratingCurrent = $('.js-rating-filter').data('current-rating');
    var $ratingAmount = $ratingFilter.parent().find('.amount .val');
    var $ratingClear = $ratingFilter.parent().find('.clear-rating');

    $('.js-rating-stat').barrating({
      theme: 'fontawesome-stars-o',
      readonly: true
    });

    $('.js-rating').barrating({
      theme: 'fontawesome-stars-o'
    });

    $ratingAmount.html($ratingCurrent);

    $ratingClear.on('click', function (e) {
      e.preventDefault();
      $ratingFilter.barrating('clear');
    });

    $ratingFilter.barrating({
      theme: 'fontawesome-stars-o',
      showSelectedRating: false,
      initialRating: $ratingCurrent,
      onSelect: function (value, text) {
        if (value === false) {
          $ratingFilter.barrating('clear');
        } else {
          $ratingAmount.html(value + ' of more');
        }
      },
      onClear: function (value, text) {}
    });

    /**
     * HOME PAGE - MAIN SLIDER
     */
    var $introSliderBg = new Swiper('.js-intro-slider-bg', {
      effect: 'fade',
      loop: true,
      speed: 1500,
      simulateTouch: false,
      allowSwipeToNext: false,
      allowSwipeToPrev: false,
      autoplay: {
        delay: 8000
      }
    });

    var $introSliderDesc = new Swiper('.js-intro-slider-desc', {
      effect: 'fade',
      loop: true,
      speed: 1500,
      simulateTouch: false,
      allowSwipeToNext: false,
      allowSwipeToPrev: false,
      autoplay: {
        delay: 8000
      }
    });

    var $introHotels = $('.js-intro-hotels');

    var $introHotelsSlider = new Swiper($introHotels, {
      loop: true,
      spaceBetween: 25,
      slidesPerView: 5,
      slidesPerGroup: 5,
      clickable: false,
      speed: 1200,
      navigation: {
        nextEl: $introHotels.next().find('.js-next'),
        prevEl: $introHotels.next().find('.js-prev')
      },
      breakpoints: {
        1600: {
          slidesPerView: 4,
          slidesPerGroup: 4
        },
        1200: {
          spaceBetween: 20,
          slidesPerView: 3,
          slidesPerGroup: 3
        },
        992: {
          spaceBetween: 15,
          slidesPerView: 2,
          slidesPerGroup: 2
        },
        567: {
          slidesPerView: 1,
          slidesPerGroup: 1
        }
      }
    });

    $('.js-input-date').on('input blur', function () {
      var $input = $(this);
      $input.next('label').text($input.val());
    });

    $('.js-input-date').each(function () {
      var $input = $(this);

      setTimeout(function () {
        $input.next('label').text($input.val());
      }, 100);
    });

    /**
     * HOME PAGE - SEARCHBAR
     */
    $('.js-select-locality').each(function () {
      var $this = $(this);
      var $contain = $this.parent();

      $this.select2({
        width: '100%',
        allowClear: true,
        placeholder: function () {
          return $(this).data('placeholder');
        },
        dropdownParent: $contain
      });
    });

    var $spinner = $(".js-qty");
    $spinner.spinner({
      min: 0
    });

    $('#hotelDate1').flatpickr({
      dateFormat: "d M",
      plugins: [
        new rangePlugin({
          input: '#hotelDateTo1'
        })
      ],
      disableMobile: true,
      defaultDate: ["2016-10-20", "2016-11-04"]
    });

    $('#hotelDate2').flatpickr({
      dateFormat: "d M",
      plugins: [
        new rangePlugin({
          input: '#hotelDateTo2'
        })
      ],
      disableMobile: true,
      defaultDate: ["2016-10-20", "2016-11-04"]
    });

    $('#flyingDate1').flatpickr({
      dateFormat: "d M",
      plugins: [
        new rangePlugin({
          input: '#flyingDateTo1'
        })
      ],
      disableMobile: true,
      defaultDate: ["2016-10-20", "2016-11-04"]
    });

    $('#flyingDate2').flatpickr({
      dateFormat: "d M",
      plugins: [
        new rangePlugin({
          input: '#flyingDateTo2'
        })
      ],
      disableMobile: true,
      defaultDate: ["2016-10-20", "2016-11-04"]
    });

    /**
     * CATEGORY - SIDEBAR
     */
    $('.js-show-more').on('click', function (e) {
      e.preventDefault();

      var $this = $(this);

      $this.toggleClass('active').prev().collapse('toggle');

      if ($this.hasClass('active')) {
        $this.text('Show less');
      } else {
        $this.text('Show more');
      }
    });

    $('.js-hotel-show-more').on('click', function (e) {
      var $this = $(this);

      $this.toggleClass('active');

      $this.closest('.hotel-package').find('.js-addition').collapse('toggle');

      if ($this.hasClass('active')) {
        $this.text('More info -');
      } else {
        $this.text('More info +');
      }
    });

    $sidebarFilter.modal({
      show: false,
      backdrop: false
    }).on('show.bs.modal', function (e) {
      $('.page-content').addClass('modal-open');
    }).on('hidden.bs.modal', function (e) {
      $('.page-content').removeClass('modal-open');
    });

    var userRating = document.getElementById('userRatingChange');
    var userRatingMin = document.getElementById('userRatingMin');

    if (userRating) {
      noUiSlider.create(userRating, {
        start: 6,
        connect: [true, false],
        range: {
          min: 0,
          max: 10
        },
        format: wNumb({
          decimals: 0
        })
      });

      userRating.noUiSlider.on('update', function (values, handle) {
        userRatingMin.innerHTML = values[handle];
      });
    }

    /**
     * CATEGORY - SORTBAR
     */
    $('.js-sorting').on('click', 'a', function (e) {
      e.preventDefault();

      var $this = $(this);

      $this.addClass('active').toggleClass('asceding')
        .siblings().removeClass('active asceding asc desc');

      if ($this.hasClass('asceding')) {
        $this.addClass('asc').removeClass('desc');
      } else {
        $this.removeClass('asc').addClass('desc');
      }
    });

    /**
     * CATEGORY - GRID LIST
     */
    $('.js-toggle-grid').on('click', function (e) {
      e.preventDefault();

      var $this = $(this);
      var $columns = $this.data('cols');
      var $item = $('.js-grid-item');
      var $grid = $item.parent().parent();

      $this.addClass('active').siblings().removeClass('active');
      $item.parent().attr('class', $columns);

      if ($this.data('grid') === 'grid') {
        $grid.removeClass('row-list');
        $item.removeClass('product--list');
      } else {
        $grid.addClass('row-list');
        $item.addClass('product--list');
      }
    });

    /**
     * CATEGORY - ITEM BANNER
     */
    $('.js-banner-slider').each(function () {
      var $bannerSlider = new Swiper(this, {
        effect: 'fade',
        loop: true,
        speed: 1000,
        simulateTouch: false,
        allowSwipeToNext: false,
        allowSwipeToPrev: false,
        autoplay: {
          delay: 3000
        }
      });
    });

    /**
     * HOTEL - SIDEBAR SEARCH
     */
    $('#hotelInDate').flatpickr({
      dateFormat: "l, M d, Y",
      plugins: [
        new rangePlugin({
          input: '#hotelOutDate'
        })
      ],
      defaultDate: [new Date, new Date()]
    });

    /**
     * HOTEL - FORM CHANGE
     */
    $('#statusDateFrom').flatpickr({
      dateFormat: "D, M d Y",
      plugins: [
        new rangePlugin({
          input: '#statusDateTo'
        })
      ],
      defaultDate: [new Date, new Date()]
    });

    /**
     * FLIGHTS - SEARCHBAR
     */
    $('#searchFlightDate').flatpickr({
      dateFormat: "l, M d, Y",
      defaultDate: [new Date]
    });

    /**
     * HOTEL PAGES
     * GRID MASONRY FOR SORTING
     * http://masonry.desandro.com/
     */
    var $gridMasonry = $('.js-grid-masonry');
    var $gridItem = $gridMasonry.find('.grid-item');

    $gridItem.hide();

    $gridMasonry.imagesLoaded(function () {
      $gridItem.fadeIn();

      $gridMasonry.masonry({
        columnWidth: '.grid-sizer',
        itemSelector: '.grid-item',
        percentPosition: true
      });

      var $gridFilter = $gridMasonry.isotope({
        itemSelector: '.grid-item',
        resizable: false,
        percentPosition: true,
        masonry: {
          columnWidth: '.grid-sizer'
        },
        hiddenStyle: {
          opacity: 0
        },
        visibleStyle: {
          opacity: 1
        }
      });

      $('.js-grid-filter').on('click', 'a', function (e) {
        e.preventDefault();

        var $this = $(this);

        if ($gridItem.hasClass('grid-item--hide')) {
          $gridItem.removeClass('grid-item--hide');
        }

        $this.parent().siblings().children().removeClass('active');
        $this.addClass('active');

        $gridFilter.isotope({
          filter: $this.attr('data-filter')
        });
      });
    });

    /**
     * HOTEL GALLERY
     */
    var $hotelSlider;
    var $hotelSliderThumbs;
    var $galleryThumbsInit;

    var $hotelCarousel = $('.js-hotel-carousel');
    var $galleryThumbs = $('.js-gallery-modal-thumbs');

    if ($hotelCarousel.length) {
      $hotelSlider = new Swiper($hotelCarousel, {
        spaceBetween: 10,
        effect: 'fade',
        navigation: {
          nextEl: '.js-next',
          prevEl: '.js-prev'
        }
      });

      $hotelSliderThumbs = new Swiper('.js-hotel-carousel-thumbs', {
        spaceBetween: 5,
        centeredSlides: true,
        slidesPerView: 'auto',
        touchRatio: 0.2,
        slideToClickedSlide: true
      });

      $hotelSlider.controller.control = $hotelSliderThumbs;
      $hotelSliderThumbs.controller.control = $hotelSlider;

      $('a[aria-controls="hotel"]').on('shown.bs.tab', function (e) {
        $hotelSlider.update();
        $hotelSliderThumbs.update();
      });

      $galleryThumbsInit = new Swiper($galleryThumbs, {
        spaceBetween: 10,
        touchRatio: 0.2,
        centeredSlides: true,
        slidesPerView: 'auto',
        slideToClickedSlide: true,
        freeMode: true,
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        }
      });
    }

    // Blueimp lightbox
    // https://github.com/blueimp/Gallery
    // Add the following JavaScript code after including the Gallery script,
    // to display the images in the Gallery lightbox on click of the links
    var $galleryModal = $(".js-gallery-link");

    $galleryModal.on('click', function (e) {
      e.preventDefault();

      var $modalPanelBottom = $('.js-gallery-modal-panel');

      blueimp.Gallery($galleryModal, {
        index: $galleryModal.index(this),
        event: e,
        indicatorContainer: '.indicator',
        fullscreen: true,
        hidePageScrollbars: true,
        disableScroll: true,
        startSlideshow: true,
        slideshowInterval: 6000,

        onopen: function () {
          $modalPanelBottom.css({
            opacity: 1,
            transition: '300ms linear 300ms'
          });

          setTimeout(function () {
            $galleryThumbs.find('li').addClass('swiper-slide');
            $galleryThumbsInit.update();
          }, 100);
        },
        onslide: function (index, slide) {
          var text = this.list[index].getAttribute('data-description');
          var node = this.container.find('.description');
          var count = this.getIndex() + 1 + '/' + this.getNumber() + ': ';

          node.empty();

          if (text) {
            node[0].appendChild(document.createTextNode(count + text));
          }

          $galleryThumbsInit.slideTo(index);
        },
        onclose: function () {
          $modalPanelBottom.css({
            opacity: 0,
            transition: '300ms ease'
          });
        }
      });
    });

    $('#galleryThumbs').on('shown.bs.collapse', function () {
      $galleryThumbsInit.update();
      $galleryThumbs.css({
        opacity: 1,
        transition: '300ms linear'
      });
    });

    $('#galleryThumbs').on('hidden.bs.collapse', function () {
      $galleryThumbs.css({
        opacity: 0
      });
    });
  });


  // Set the date we're counting down to
  var countDownDate = new Date("October 9 2018 20:17:00").getTime();

  // Update the count down every 1 second
  var x = setInterval(function () {

    // Get todays date and time
    var now = new Date().getTime();

    // Find the distance between now and the count down date
    var distance = countDownDate - now;

    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Output the result in an element with id="demo"
    document.getElementById("demo").innerHTML = days + "d " + hours + "h " +
      minutes + "m " + seconds + "s ";

    // If the count down is over, write some text 
    if (distance < 0) {
      clearInterval(x);
      document.getElementById("demo").innerHTML = "EXPIRED";
    }
  }, 1000);

  $(".modal").each( function(){
    $(this).wrap('<div class="overlay"></div>')
  });
  
  $(".open-modal").on('click', function(e){
    e.preventDefault();
    e.stopImmediatePropagation;
    
    var $this = $(this),
        modal = $($this).data("modal");
    
    $(modal).parents(".overlay").addClass("open");
    setTimeout( function(){
      $(modal).addClass("open");
    }, 350);
    
    $(document).on('click', function(e){
      var target = $(e.target);
      
      if ($(target).hasClass("overlay")){
        $(target).find(".modal").each( function(){
          $(this).removeClass("open");
        });
        setTimeout( function(){
          $(target).removeClass("open");
        }, 350);
      }
      
    });
    
  });
  
  $(".close-modal").on('click', function(e){
    e.preventDefault();
    e.stopImmediatePropagation;
    
    var $this = $(this),
        modal = $($this).data("modal");
    
    $(modal).removeClass("open");
    setTimeout( function(){	
      $(modal).parents(".overlay").removeClass("open");
    }, 350);
    
  });	

})();