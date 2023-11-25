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
    $('.busket_product').on('click', 'a[class="remove"]', function () {
        let t_href = event.target;
        console.log(t_href.name);


        $.ajax({
            url: '/baskets/remove/' + t_href.name + '/',
            success: function (data) {
                $('.busket_product').html(data.result)
            },
        });
        event.preventDefault()
    });
    $('.products').on('click', 'a[id="add"]', function () {
        let t_href = event.target;
        t_href.innerHTML = 'УДАЛИТЬ ИЗ КОРЗИНЫ';
        t_href.setAttribute("id", 'remove');
        fl_basket = document.getElementById('float_basket');
        new_val= Number(fl_basket.getAttribute('value')) + 1;
        fl_basket.setAttribute("value", new_val);


        $.ajax({
            url: '/baskets/add/' + t_href.name + '/',
//            success: function (data) {
//                $('.products').html(data.result)
//            },
        });
        event.preventDefault()
    });
    $('.products').on('click', 'a[id="remove"]', function () {
        let t_href = event.target;
        console.log(t_href)
        t_href.innerHTML = 'ДОБАВИТЬ В КОРЗИНУ';
        t_href.setAttribute("id", 'add');
        fl_basket = document.getElementById('float_basket');
        new_val= Number(fl_basket.getAttribute('value')) - 1;
        fl_basket.setAttribute("value", new_val);

        $.ajax({
            url: '/baskets/remove_from_products/' + t_href.name + '/',
//            success: function (data) {
//                $('.products').html(data.result)
//            },
        });
        event.preventDefault()
    });
    $('.products').on('click', 'path[type="like"]', function () {
        let t_href = event.target;
        console.log(t_href.id);
        fill = t_href.getAttribute('fill')
        if (fill == "#fff"){
            t_href.setAttribute("fill","#c70000");
        }
        else{
            t_href.setAttribute("fill","#fff");
        }
        console.log(t_href)


        $.ajax({
            url: '/likes/like_action/' + t_href.id + '/',
            success: function (data) {
                $('.products').html(data.result)
            },
        });
    });
};
