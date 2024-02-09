// add to cart functionality

$('#add-to-cart-btn').on('click',function(){
    let quantity = $('#product-quantity').val()
    let product_title = $('.product-title').val()
    let product_id = $('.product-id').val()
    let product_price = $('#product-price').text()
    let this_val = $(this)


    console.log('Quantity:',quantity);
    console.log('Title:',product_title);
    console.log('Price:',product_price);
    console.log('ID:',product_id);
    console.log('Current Element:', this_val);

    $.ajax({
        url: '/add-to-cart',
        data: {
            'id':product_id,
            'qty': quantity,
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