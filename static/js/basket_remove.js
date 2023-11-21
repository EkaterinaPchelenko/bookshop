window.onload = function (){
    $('.busket_product').on('click', 'a[class="remove"]', function () {
        let t_href = event.target;
        console.log(t_href.name);
        console.log(t_href.value);

        $.ajax({
            url: '/baskets/remove/' + t_href.name + '/',
            success: function (data) {
                $('.busket_product').html(data.result)
            },
        });
        event.preventDefault()
    });
};
