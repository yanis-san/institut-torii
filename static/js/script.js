let swiper = new Swiper(".mySwiper", {
    slidesPerView: 3,
    spaceBetween: 30,
    loop: true,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    // mousewheel: true, // Permet le glissement avec la molette de la souris (désactivé)
    keyboard: true,   // Permet la navigation avec les touches du clavier
    breakpoints: {
        // when window width is >= 320px
        320: {
            slidesPerView: 1,
            spaceBetween: 10
        },
        // when window width is >= 640px
        640: {
            slidesPerView: 2,
            spaceBetween: 20
        },
        // when window width is >= 1024px
        1024: {
            slidesPerView: 3,
            spaceBetween: 30
        }
    }
});