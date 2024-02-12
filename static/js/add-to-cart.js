// add to cart functionality

$('.add-to-cart-btn').on('click',function(){

    let this_val = $(this)
    let index = this_val.attr('data-index')


    let quantity = $('.product-quantity-' + index).val()
    let product_title = $('.product-title-' + index).val()
    let product_id = $('.product-id-' + index).val()
    let product_price = $('.product-price-' + index).val()
    let product_pid = $('.product-pid-' + index).val()
    let product_image = $('.product-image-' + index).val()

    console.log('Quantity:',quantity);
    console.log('Title:',product_title);
    console.log('Price:',product_price);
    console.log('ID:',product_id);
    console.log('PID:', product_pid)
    console.log('Image:', product_image)
    console.log('Index:', index)
    console.log('Current Element:', this_val);
    


    $.ajax({
        url: '/add-to-cart',
        data: {
            'id':product_id,
            'pid':product_pid,
            'qty': quantity,
            'image':product_image,
            'title':product_title,
            'price':product_price,
        },
        dataType: 'json',
        beforeSend:function(){
            console.log('Adding Product to Cart...');
        },
        success: function(response){
            this_val.html('Product Added to Cart');
            console.log('Successfully Added the Product to Cart.');
            $('.cart-items-count').text(response.totalcartitems)
        }
    })
})



$(document).on("click", '.delete-product', function(){
    let product_id = $(this).attr('data-product')
    let this_val = $(this)

    console.log('product id: ', product_id);

    $.ajax({
        url: '/delete-from-cart',
        data: {
            'id': product_id
        },
        dataType:'json',
        beforeSend: function(){
            this_val.hide()
        },
        success: function(response){
            this_val.show()
            $('.cart-items-count').text(response.totalcartitems)
            $('#cart-list').html(response.data)
        }
    })
})

$(document).on("click", '.update-product', function(){
    let product_id = $(this).attr('data-product')
    let this_val = $(this)
    let product_quantity = $('.product-qty-' + product_id).val()

    console.log('product id: ', product_id);
    console.log('product qty: ', product_quantity);

    $.ajax({
        url: '/update-cart',
        data: {
            'id': product_id,
            'qty':product_quantity
        },
        dataType:'json',
        beforeSend: function(){
            this_val.hide()
        },
        success: function(response){
            this_val.show()
            $('.cart-items-count').text(response.totalcartitems)
            $('#cart-list').html(response.data)
        }
    })
})






// $('#add-to-cart-btn').on('click',function(){
//     let quantity = $('#product-quantity').val()
//     let product_title = $('.product-title').val()
//     let product_id = $('.product-id').val()
//     let product_price = $('#product-price').text()
//     let this_val = $(this)


//     console.log('Quantity:',quantity);
//     console.log('Title:',product_title);
//     console.log('Price:',product_price);
//     console.log('ID:',product_id);
//     console.log('Current Element:', this_val);

//     $.ajax({
//         url: '/add-to-cart',
//         data: {
//             'id':product_id,
//             'qty': quantity,
//             'title':product_title,
//             'price':product_price,
//         },
//         dataType: 'json',
//         beforeSend:function(){
//             console.log('Adding Product to Cart...');
//         },
//         success: function(response){
//             this_val.html('Product Added to Cart');
//             console.log('Successfully Added the Product to Cart.');
//             $('.cart-items-count').text(response.totalcartitems)
//         }
//     })
// })