$(document).ready(function () {
  document.querySelector('.form-section-container.submit button').addEventListener('click', function(event){
    event.preventDefault();

    function validateInputs () {
      if ( +document.querySelector('.form-container #range-slider__min').value
        > +document.querySelector('.form-container #range-slider__max').value ) {

        $('.form-section-container.rating-filter .range-input-container').addClass('error');
        $('.form-section-container.message').show();
        document.querySelector('.form-section-container.message p').innerHTML = 'لطفاً خطاهای مشخص شده را رفع کنید.';

        $('.form-section-container.rating-filter .range-input-container input').on('input', function () {
          $('.form-section-container.rating-filter .range-input-container').removeClass("error");
          $('.form-section-container.message').hide();
          document.querySelector('.form-section-container.message p').innerHTML = '';
        });
        return false;
      } else return true;
    }

    if (validateInputs()) {
      let temp;
      // document.getElementById('completed-search-form__word').innerHTML = '';
      document.getElementById('completed-search-form__lang').innerHTML = '';
      document.getElementById('completed-search-form__category').innerHTML = '';
      document.getElementById('completed-search-form__stars').innerHTML = '';
      document.getElementById('completed-search-form__submit').innerHTML = '';


      // temp = document.querySelector('.form-container #word-search').value;
      // document.getElementById('completed-search-form__word').append(temp);

      temp = document.querySelectorAll('.form-container #dropdown__lang .dropdown-options.selected');
      for (let i = 0; i < temp.length; i++) {
        document.getElementById('completed-search-form__lang').append(temp[i].textContent + ',');
      }

      temp = document.querySelectorAll('.form-container #dropdown__category .dropdown-options.selected');
      for (let i = 0; i < temp.length; i++) {
        document.getElementById('completed-search-form__category').append(temp[i].textContent + ',');
      }

      temp = document.querySelector('.form-container #range-slider__min').value;
      document.getElementById('completed-search-form__stars').append(temp + ',');

      temp = document.querySelector('.form-container #range-slider__max').value;
      document.getElementById('completed-search-form__stars').append(temp + ',');

      document.getElementById('completed-search-form__submit').innerHTML = 'true';
    }
  });
});
