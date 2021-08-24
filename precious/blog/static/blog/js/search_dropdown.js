$( document ).ready(function() {
	"use strict";
	let header = $(".dropdown .dropdown-header");
	let optionsContainer = $(".dropdown .dropdown-options-container");
	let options = $(".dropdown .dropdown-options-container .dropdown-options");
	
	// Add any dropdown section name in here, has to be specific obviously
	let sections = ["lang", "category"];
	let sectionId = "";
	let sectionIndex = null;

	// Pushes an empty array for each of the sections
	let selected = [];
	for (let i = 0; i < sections.length; i++) selected.push([]);

	header.click(function(e) {
		// Toggles the dropdown if clicked on the header of the dropdown
		$(this).siblings(".dropdown-options-container").slideToggle(300);

		$(this).hasClass("dropdown-header-radiusTop")
		? $(this).removeClass("dropdown-header-radiusTop")
		: $(this).addClass("dropdown-header-radiusTop");
	});

	options.click(function(){
		// Toggles the selected class for dropdown options
		$(this).hasClass("dropdown-options-selected")
		? $(this).removeClass("dropdown-options-selected")
		: $(this).addClass("dropdown-options-selected");


		$(this).children("p").children("i").hasClass("fas fa-check-square")
		? $(this).children("p").children("i").removeClass("fas fa-check-square")
		&& $(this).children("p").children("i").addClass("far fa-square")
		: $(this).children("p").children("i").removeClass("far fa-square")
		&& $(this).children("p").children("i").addClass("fas fa-check-square");

		// Parses the sectioName out of the parent id
		// The id would be #dropdown-sectionName
		sectionId = $(this).parent(".dropdown-options-container")[0].id
		.substring(	$(this).parent(".dropdown-options-container")[0].id.indexOf("-") + 1 );

		for (const i in sections) {
			if (sections[i] === sectionId) {
				sectionIndex = i;
				break;
			} else {
				continue;
			}
			throw new Error("Undefined section. It might be a typo in your code or you didn\'t add it in the sections array.");
		}

		// Toggles selected option text in its own array in selected
		if (selected[sectionIndex].indexOf(this.innerText) >= 0) {
			selected[sectionIndex] = selected[sectionIndex].filter(el => el !== this.innerText);
		}
		else {
			selected[sectionIndex].push(this.innerText);
		}

		renderTags(selected[sectionIndex], sectionId);
	});

	function renderTags(arr, secId) {
		const langTags = document.getElementById("selected-tags-" + secId);
		while (langTags.lastElementChild) {
			langTags.removeChild(langTags.lastElementChild);
		}
		for (const item of arr) {
			document.getElementById("selected-tags-" + secId).appendChild(createTagDom(item));
		}
	}

	function createTagDom(text) {
		// HTML Sample:
		// <div>
        //   <span><i class="fas fa-times-circle"></i></span>
        //   <span>tag</span>
        // </div>

		let tag = document.createElement("div");
		let span = document.createElement("span");
		let name = document.createElement("span");
		let icon = document.createElement("i");

		icon.classList.add("fas", "fa-times-circle");
		span.appendChild(icon);
		tag.appendChild(span)

		name.innerText = text;
		tag.appendChild(name)

		return tag;
	}
});
