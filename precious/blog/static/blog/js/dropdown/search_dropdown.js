// import DROPDOWN_OPTIONS from './dropdown_list.js';

$(document).ready(function () {
  'use strict';

  $('.dropdown .dropdown-options-container ul li').addClass('dropdown-options');

  const header = $('.dropdown .dropdown-header');
  const optionsContainer = $('.dropdown .dropdown-options-container');
  const optionsInput = $('.dropdown .dropdown-options-container .dropdown-options input[type="checkbox"]');
  let tags = $('.tag-search-container .selected-tags-container > div.selected-tag');
  // let dropdownOptions_langtags = $('#dropdown__langtags .dropdown-options');
  // let dropdownOptions_cats = $('#dropdown__cats .dropdown-options');
  
  // Add any dropdown section name in here, has to be specific obviously
  const sections = ['langtags', 'cats'];

  // Pushes an empty array for each of the sections
  let selected = [];
  for (let i = 0; i < sections.length; i++) selected.push([]);


  // Managing z-index of the dropdowns
  for (let i = optionsContainer.length; i > 0; i--) $(optionsContainer[i]).css({ 'z-index': i });



  // Removing checked checkboxes from the previous session
  for (let i = 0; i < optionsInput.length; i++) $(optionsInput[i]).prop('checked', false);


  header.click(function(e) {
    // Toggles the dropdown if clicked on the header of the dropdown
    $(this).siblings('.dropdown-options-container').slideToggle(300);

    $(this).hasClass('dropdown-header-radiusTop')
    ? $(this).removeClass('dropdown-header-radiusTop')
    : $(this).addClass('dropdown-header-radiusTop');
  });

  optionsInput.click(handleOptionsClick);

  // tags.on('click', '.tag-search-container .selected-tags-container > div.selected-tag', handleTagsClick);
  // tags.off('click', '.tag-search-container .selected-tags-container > div.selected-tag', handleTagsClick);

  // Filter dropdown options by typing
  $('.dropdown .dropdown-header > input').on('input', function(e) {
    const { value } = e.target;
    const secId = e.currentTarget.id.substring(e.currentTarget.id.indexOf('__') + 2);
    const dropdownOptions = $(`#dropdown__${secId} .dropdown-options`);

    $(`.dropdown #dropdown__${secId}`).slideDown(300);    

    for (let i = 0; i < dropdownOptions.length; i++) {
      $(dropdownOptions[i]).css({ 'display': 'none'  });

      if (dropdownOptions[i].textContent.toLowerCase().indexOf(value.toLowerCase()) >= 0) {
        $(dropdownOptions[i]).css({ 'display': 'block' });
      }
    }


    for (let i = 0; i < dropdownOptions.length; i++) {      
      if ($(dropdownOptions[i]).css('display') === 'block') {
        $(`#dropdown__${secId} .dropdown-noresult`).hide();
        break;
      }
      else {        
        $(`#dropdown__${secId} .dropdown-noresult`).show();
      }
    }
  });

  function handleTagsClick (e) {
    // Parses the sectionName out of the parent id
    // The id would be #selected-tags__sectionId
    const sectionId = $(e.currentTarget).parent('.selected-tags-container')[0].id
                    .substring( $(e.currentTarget).parent('.selected-tags-container')[0].id.indexOf('__') + 2 );

    updateSelected(e.currentTarget.textContent, sectionId);
  }

  function handleOptionsClick (e) {
    updateSelected(e.currentTarget.value.trim(), e.currentTarget.name);
  }

  function getSectionIndexById (sectionId) {
    let sectionIndex;
    for (const i in sections) {
      if (sections[i] === sectionId) {
        sectionIndex = i;
        break;
      } else {
        continue;
      }
      throw new Error('Undefined section. It might be a typo in your code or you didn\'t add it in the sections array.');
    }

    return sectionIndex;
  }

  function updateSelected (selectedItem, secId) {    
    const secIndex = getSectionIndexById(secId);
    let action = '';
    // Toggles selected option text in its own array in selected
    if (selected[secIndex].indexOf(selectedItem) >= 0) {
      selected[secIndex] = selected[secIndex].filter(el => el !== selectedItem);
      action = 'REMOVE';
    }
    else {
      selected[secIndex].push(selectedItem);
      action = 'ADD';
    }

    updateDropdowns(action, selectedItem, secId);
    updateTags(action, selectedItem, secId);
  }

  function updateDropdowns (action, selectedItem, secId) {
    const option = $(`.dropdown #dropdown__${secId} li input[value="${selectedItem}"]`)
                   .parent('label').parent('li');
    if (action === 'REMOVE') {
      option.removeClass('selected');
      $(`.dropdown #dropdown__${secId} li input[value="${selectedItem}"]`).prop('checked', false);
    } else if (action === 'ADD') {
      option.addClass('selected');
      $(`.dropdown #dropdown__${secId} li input[value="${selectedItem}"]`).prop('checked', true);
    } else {
      throw new Error("Undefined action value for updateDropdowns() function.");
    }
    
  }

  function updateTags (action, selectedItem, secId) {
    let currTags = $(`.tag-search-container #selected-tags-container__${secId} > div.selected-tag`);
    if (action === 'REMOVE') {
      for (let i = 0; i < currTags.length; i++) {
        if (currTags[i].textContent.trim() === selectedItem) {
          $(currTags[i]).remove();
          break;
        }
      }
    } else if (action === 'ADD') {
      // HTML Sample:
      // <div>
      //   <span><i class='fas fa-times-circle'></i></span>
      //   <span>tag</span>
      // </div>

      const tag = document.createElement('div');
      const span = document.createElement('span');
      const name = document.createElement('span');
      const icon = document.createElement('i');
      tag.classList.add('en', 'selected-tag');
      icon.classList.add('fas', 'fa-times-circle');
      span.appendChild(icon);
      tag.appendChild(span)
      tag.appendChild(name);
      name.innerText = selectedItem;

      document.getElementById(`selected-tags-container__${secId}`).appendChild(tag);
    } else {
      throw new Error("Undefined action value for updateTags() function.");
    }

    tags = $('.tag-search-container .selected-tags-container > div.selected-tag');
    tags.off('click');
    tags.on('click', handleTagsClick);
  }

  function toKebabCase (str) {
    let kebab = str.toLowerCase();  
    for (const char of kebab) {
      if ('abcdefghijklmnopqrstuvwxyz'.indexOf(char) < 0) {
        kebab = kebab.replace(char, '-');
      }
    }
    return kebab;
  }

});
