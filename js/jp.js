function openEditModal(id) {
    //const id = item;
    alert(id)
    //const form = document.querySelector('form');
    //const fields = form.querySelectorAll('input, textarea');

    if (id === 0) {
        alert(id)
        // Desativa a validação dos campos do formulário
        fields.forEach(field => {
            field.removeAttribute('required');
        });
    }
}
