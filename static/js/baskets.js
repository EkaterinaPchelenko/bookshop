window.onload = function (){
    $('.busket_product').on('click', 'input[type="number"]', function () {
        let t_href = event.target;
        console.log(t_href.name);
        console.log(t_href.value);

        $.ajax({
            url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/',
            success: function (data) {
                $('.busket_product').html(data.result)
            },
        });
        event.preventDefault()
    });
};