const modal_opens = document.querySelectorAll('.modal_comment_open');
const modals = document.querySelectorAll('.modal_comment');
const close_modal_comments = document.querySelectorAll('.close_modal_comment');
const body = document.querySelector('body');

modal_opens.forEach((modal_open, index) => {
    modal_open.addEventListener('click', () => {
        modals[index].style.display = 'flex'; // Exibe o modal correspondente ao ícone de chat clicado

        // Obtém a posição atual de rolagem da página
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Define o estilo 'top' do modal para a posição atual de rolagem da página
        modals[index].style.top = scrollTop + 'px';

        body.style.overflow = 'hidden';
    });
});

close_modal_comments.forEach(close_modal_comment => {
    close_modal_comment.addEventListener('click', () => {
        const modal = close_modal_comment.closest('.modal_comment');
        modal.style.display = 'none';
        body.style.overflow = 'auto';
    });
});


