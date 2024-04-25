criar = document.getElementById('criar');
modal_criar = document.getElementById('modal_criar');
modal_criar_close = document.getElementById('modal_criar_close')

criar.addEventListener('click', () => {
    modal_criar.style.display = 'flex';
});

modal_criar_close.addEventListener('click', () => {
    modal_criar.style.display = 'none';
});



document.getElementById('photo-input').onchange = function(e) {
    var reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById('preview-image').src = e.target.result;
        document.getElementById('preview-image').style.display = 'block';
        document.getElementById('preview-before-image').style.display = 'none';
    };
    reader.readAsDataURL(this.files[0]);
};  