let form = document.querySelector('form'),
  resultTextarea = document.getElementById('perform-result');

form.onsubmit = function () {
  $.ajax({
    url: '/api/v1.0/perform',
    type: "POST",
    data: JSON.stringify({"text": form.elements.text.value}),
    contentType: "application/json; charset=utf-8",
  })
    .success(function (result) {
      resultTextarea.value = result.result
    })
    .error(function (message) {
      console.log(message)
    });
  return false;
};