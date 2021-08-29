document.querySelector(".form-container .submit-container button").addEventListener("click", function(event){
  event.preventDefault();
  let temp;
  // document.getElementById("completed-search-form__word").innerHTML = "";
  document.getElementById("completed-search-form__lang").innerHTML = "";
  document.getElementById("completed-search-form__category").innerHTML = "";
  document.getElementById("completed-search-form__stars").innerHTML = "";
  document.getElementById("completed-search-form__submit").innerHTML = "";


  // temp = document.querySelector(".form-container #word-search").value;
  // document.getElementById("completed-search-form__word").append(temp);

  temp = document.querySelectorAll(".form-container #dropdown__lang .dropdown-options.selected");
  for (let i = 0; i < temp.length; i++) {
    document.getElementById("completed-search-form__lang").append(temp[i].textContent + ",");
  }

  temp = document.querySelectorAll(".form-container #dropdown__category .dropdown-options.selected");
  for (let i = 0; i < temp.length; i++) {
    document.getElementById("completed-search-form__category").append(temp[i].textContent + ",");
  }

  temp = document.querySelector(".form-container #range-slider__min").value;
  document.getElementById("completed-search-form__stars").append(temp + ",");

  temp = document.querySelector(".form-container #range-slider__max").value;
  document.getElementById("completed-search-form__stars").append(temp + ",");

  document.getElementById("completed-search-form__submit").innerHTML = "true";
});
