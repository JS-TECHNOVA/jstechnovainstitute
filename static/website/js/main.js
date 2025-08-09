const a = document.querySelectorAll(".nav-links");
const span = document.querySelector(".nav-span");
const header = document.getElementById("header");
const fixed_demo_btn = document.getElementById("fixed-demo-btn");

const curentActive = () => {
	try {
		const active = document.querySelector(".active-nav");
		return { left: active.offsetLeft, width: active.offsetWidth };
	} catch (error) {
		return null;
	}
};

const setPosition = (o) => {
	if (o !== null) {
		span.style.left = o.left + 10 + "px";
		span.style.width = o.width - 20 + "px";
	}
};

const handleHover = (e) => {
	setPosition({ left: e.target.offsetLeft, width: e.target.offsetWidth });
};

const handleLeave = (e) => {
	let c = curentActive();
	if (c !== null) {
		setPosition(c);
	} else {
		setPosition({ width: 0 });
	}
};

for (let x of a) {
	x.addEventListener("mousemove", handleHover);
	x.addEventListener("mouseleave", handleLeave);
}

setPosition(curentActive());

var prev = 0;
window.addEventListener("scroll", (e) => {
	let previous = window.prev;
	let current = window.scrollY;

	if (current > previous) {
		header.style.transform = "translateY(-100px)";
		fixed_demo_btn.style.transform = "translateY(-100px)";
	} else {
		header.style.transform = "translateY(0px)";
		fixed_demo_btn.style.transform = "translateY(100px)";
	}
	window.prev = current;
});

var swiper = new Swiper(".mySwiper", {
	freeMode: true,
	speed: 20000,
	centeredSlides: true,
	slidesPerView: 1,
	spaceBetween: 50,
	autoplay: {
		disableOnInteraction: false,
		delay: 0.1,
	},
	loop: true,
	grabCursor: false,
	breakpoints: {
		640: {
			slidesPerView: 2,
		},
		768: {
			slidesPerView: 3,
		},
	},
});

// book_now modal - start

const toggle_bn_modal = (event) => {
	const modal = document.querySelector("#boon_now_modal");
	modal.classList.toggle("hidden");
};

document.querySelectorAll("#boon_now_btn")?.forEach((el) => {
	el.addEventListener("click", toggle_bn_modal);
});

// book now modal - end
