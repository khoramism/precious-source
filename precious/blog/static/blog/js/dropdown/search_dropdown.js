// import DROPDOWN_OPTIONS from './dropdown_list.js';

$( document ).ready(function() {
  "use strict";

  // Initially renders the dropdown list according to dropdown_optoins.js
  (function renderDropdownOptionsInitially(dropdownArr) {
    let parent, inner, icon, id;
    // HTML Sample:
    // <div id="dropdown-option__TXT" class="dropdown-options">
    //     <p><i class="far fa-square"></i>TXT</p>
    // </div>
    
    for (const dropdown of dropdownArr) {
      for (const item of dropdown.options) {
        parent = document.createElement("div");
        inner = document.createElement("p");
        icon = document.createElement("i");

        inner.append(icon, item);
        parent.append(inner);

        icon.classList.add("far", "fa-square");
        parent.classList.add("dropdown-options");
        
        
        parent.setAttribute("id", "dropdown-option__" + toKebabCase(item));

        document.getElementById("dropdown__" + dropdown.title).appendChild(parent);
      }
    }
  })(DROPDOWN_OPTIONS);

  function toKebabCase(str) {
    let kebab = str.toLowerCase();  
    for (const char of kebab) {
      if ("abcdefghijklmnopqrstuvwxyz".indexOf(char) < 0) {
        kebab = kebab.replace(char, "-");
      }
    }
    return kebab;
  }

  let header = $(".dropdown .dropdown-header");
  let optionsContainer = $(".dropdown .dropdown-options-container");
  let options = $(".dropdown .dropdown-options-container .dropdown-options");
  let tags = $(".tag-search-container .selected-tags > div");
  let dropdownOptions_lang = $("#dropdown__lang .dropdown-options");
  let dropdownOptions_category = $("#dropdown__category .dropdown-options");
  
  // Add any dropdown section name in here, has to be specific obviously
  let sections = ["lang", "category"];

  // Pushes an empty array for each of the sections
  let selected = [];
  for (let i = 0; i < sections.length; i++) selected.push([]);


  // Managing z-index of the dropdowns
  for (let i = optionsContainer.length; i > 0; i--) {
    $(optionsContainer[i]).css({ 'z-index': i });
  }


  header.click(function(e) {
    // Toggles the dropdown if clicked on the header of the dropdown
    $(this).siblings(".dropdown-options-container").slideToggle(300);

    $(this).hasClass("dropdown-header-radiusTop")
    ? $(this).removeClass("dropdown-header-radiusTop")
    : $(this).addClass("dropdown-header-radiusTop");
  });

  options.click(handleOptionsClick);

  tags.click(handleTagsClick);

  document.querySelector(".dropdown #tag-search-input__lang").addEventListener("input", function(e) {
    let { value } = e.target;

    $(".dropdown #dropdown__lang").slideDown(300);

    for (let i = 0; i < dropdownOptions_lang.length; i++) {
      $(dropdownOptions_lang[i]).css({ "display": "none"  });

      if (dropdownOptions_lang[i].textContent.toLowerCase().indexOf(value.toLowerCase()) >= 0) {
        $(dropdownOptions_lang[i]).css({ "display": "block" });
      }
    }

    for (let i = 0; i < dropdownOptions_lang.length; i++) {      
      if ($(dropdownOptions_lang[i]).css("display") === "block") {
        $("#dropdown__lang .dropdown-noresult").hide();
        break;
      }
      else {
        $("#dropdown__lang .dropdown-noresult").show();
      }
    }
  });

  document.querySelector(".dropdown #tag-search-input__category").addEventListener("input", function(e) {
    let { value } = e.target;

    $(".dropdown #dropdown__category").slideDown(300);

    for (let i = 0; i < dropdownOptions_category.length; i++) {
      $(dropdownOptions_category[i]).css({ "display": "none"  });

      if (dropdownOptions_category[i].textContent.toLowerCase().indexOf(value.toLowerCase()) >= 0) {
        $(dropdownOptions_category[i]).css({ "display": "block" });
      }
    }

    for (let i = 0; i < dropdownOptions_category.length; i++) {      
      if ($(dropdownOptions_category[i]).css("display") === "block") {
        $("#dropdown__category .dropdown-noresult").hide();
        break;
      }
      else {        
        $("#dropdown__category .dropdown-noresult").show();
      }
    }
  });

  function handleTagsClick(e) {
    // Parses the sectionName out of the parent id
    // The id would be #selected-tags__sectionId
    let sectionId = $(e.currentTarget).parent(".selected-tags")[0].id
      .substring( $(e.currentTarget).parent(".selected-tags")[0].id.indexOf("__") + 2 );

    updateSelected(e.currentTarget.textContent, getSectionIndexById(sectionId));
    renderBySelected(selected);
  }

  function handleOptionsClick(e) {
    let clickedItemTxt = e.currentTarget.textContent;
    

    // Parses the sectionName out of the parent id
    // The id would be #dropdown__sectionId
    let sectionId = $(this).parent(".dropdown-options-container")[0].id
      .substring( $(this).parent(".dropdown-options-container")[0].id.indexOf("__") + 2 );

    updateSelected(clickedItemTxt, getSectionIndexById(sectionId));
    renderBySelected(selected);
  }

  function getSectionIndexById(sectionId) {
    let sectionIndex;
    for (const i in sections) {
      if (sections[i] === sectionId) {
        sectionIndex = i;
        break;
      } else {
        continue;
      }
      throw new Error("Undefined section. It might be a typo in your code or you didn\'t add it in the sections array.");
    }

    return sectionIndex;
  }

  function updateSelected(selectedItem, secIndex) {
    // Toggles selected option text in its own array in selected
    if (selected[secIndex].indexOf(selectedItem) >= 0) {
      selected[secIndex] = selected[secIndex].filter(el => el !== selectedItem);
    }
    else {
      selected[secIndex].push(selectedItem);
    }
  }

  function renderBySelected(selected) {
    renderDropdowns(selected);
    renderTags(selected);
  }

  function renderDropdowns(selected) {
    let secId = 0;
    
    let dropdowns = $(".dropdown .dropdown-options-container");

    for (const section of selected) {
      $(dropdowns[secId]).children(".dropdown-options").removeClass("selected");
      $(dropdowns[secId]).children(".dropdown-options").children("p").children("i").removeClass("fas fa-check-square");
      $(dropdowns[secId]).children(".dropdown-options").children("p").children("i").addClass("far fa-square");
      for (const item of section) {
        $(dropdowns[secId]).children("#dropdown-option__" + toKebabCase(item))
          .addClass("selected");
        $(dropdowns[secId]).children("#dropdown-option__" + toKebabCase(item)).children("p").children("i")
          .removeClass("far fa-square");
        $(dropdowns[secId]).children("#dropdown-option__" + toKebabCase(item)).children("p").children("i")
          .addClass("fas fa-check-square");
      }
      secId++;
    }
  }

  function renderTags(selected) {
    let tag, span, name, icon;

    for (let i = 0; i < selected.length; i++) {

      const langTags = document.getElementById("selected-tags__" + sections[i]);
      while (langTags.lastElementChild) {       
        langTags.removeChild(langTags.lastElementChild);
      }
      for (const item of selected[i]) {
        // HTML Sample:
        // <div>
        //   <span><i class="fas fa-times-circle"></i></span>
        //   <span>tag</span>
        // </div>
        tag = document.createElement("div");
        span = document.createElement("span");
        name = document.createElement("span");
        icon = document.createElement("i");
        tag.classList.add("en");
        icon.classList.add("fas", "fa-times-circle");
        span.appendChild(icon);
        tag.appendChild(span)
        tag.appendChild(name);
        name.innerText = item;

        document.getElementById("selected-tags__" + sections[i]).appendChild(tag);
      }
    }
    tags = $(".tag-search-container .selected-tags > div");
    tags.click(handleTagsClick);
  }
  
});
