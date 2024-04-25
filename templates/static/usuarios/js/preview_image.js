document.getElementById('file-input').onchange = function(e) {
    var reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById('imagepreview').src = e.target.result;
        document.getElementById('imagepreview').style.display = 'block';
        document.getElementById('imagepreviewbefore').style.display = 'none';
    };
    reader.readAsDataURL(this.files[0]);
};  

