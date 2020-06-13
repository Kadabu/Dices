document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('.dice').forEach(item => {
    item.addEventListener('click', event => {
      item.style.display = "none";
    })
  });
  document.querySelector('#dices').children[0].addEventListener('click', event => {
      document.querySelector('#id_put_aside_0').checked = true;
    });
  document.querySelector('#dices').children[1].addEventListener('click', event => {
      document.querySelector('#id_put_aside_1').checked = true;
    });
  document.querySelector('#dices').children[2].addEventListener('click', event => {
      document.querySelector('#id_put_aside_2').checked = true;
    });
  document.querySelector('#dices').children[3].addEventListener('click', event => {
      document.querySelector('#id_put_aside_3').checked = true;
    });
  document.querySelector('#dices').children[4].addEventListener('click', event => {
      document.querySelector('#id_put_aside_4').checked = true;
    });
});
