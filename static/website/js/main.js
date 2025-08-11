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

// book_now modal - start

const toggle_bn_modal = (event) => {
	const modal = document.querySelector("#boon_now_modal");
	modal.classList.toggle("hidden");
};

document.querySelectorAll("#boon_now_btn")?.forEach((el) => {
	el.addEventListener("click", toggle_bn_modal);
});

// book now modal - end

const side_menu_drawer = document.querySelector("#side_menu_drawer");

const wind_nav_listener = (e) => {
	if (e.target == side_menu_drawer) {
		side_menu_drawer.classList.toggle("hidden");
		window.removeEventListener("click", wind_nav_listener);
	}
};
document.querySelector("#side_menu_btn").addEventListener("click", (e) => {
	side_menu_drawer.classList.toggle("hidden");
	window.addEventListener("click", wind_nav_listener);
});

// student feedbacks

const st_feedback_slides = document.querySelectorAll("#st_feedback");
let current_feedback_slide_index = 0;

function showSlide(index) {
	st_feedback_slides.forEach((slide) => slide.classList.add("hidden"));
	st_feedback_slides[index].classList.remove("hidden");
}

document.getElementById("prev_feedback_btn").addEventListener("click", () => {
	current_feedback_slide_index =
		(current_feedback_slide_index - 1 + st_feedback_slides.length) %
		st_feedback_slides.length;
	showSlide(current_feedback_slide_index);
});

document.getElementById("next_feedback_btn").addEventListener("click", () => {
	current_feedback_slide_index =
		(current_feedback_slide_index + 1) % st_feedback_slides.length;
	showSlide(current_feedback_slide_index);
});

showSlide(0);

function openModal(id) {
	document.getElementById(id).style.display = "flex";
}

function closeModal(id) {
	document.getElementById(id).style.display = "none";
}
