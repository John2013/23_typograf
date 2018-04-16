let form = document.querySelector('form'),
  resultTextarea = document.getElementById('perform-result');

form.onsubmit = function () {
  $.post(
    '/api/v1.0/perform',
    `{"text": "${this.elements.text.value}"}`
  )
    .success(function (result) {
      console.log(result);
      resultTextarea.value = result
    })
    .error(function (message) {
      console.log(message)
    });
  return false;
};