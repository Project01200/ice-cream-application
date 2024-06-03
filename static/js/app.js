function searchIceCream() {
    const query = document.getElementById('searchBox').value.toLowerCase();
    const iceCreams = document.querySelectorAll('.iceCream');

    iceCreams.forEach(iceCream => {
        const label = iceCream.querySelector('label').innerText.toLowerCase();
        if (label.includes(query)) {
            iceCream.style.display = 'block';
        } else {
            iceCream.style.display = 'none';
        }
    });
}

function goToCheckout() {
    const selectedIceCream = document.querySelector('input[name="iceCream"]:checked');
    const selectedContainer = document.querySelector('input[name="container"]:checked');
    const selectedSize = document.querySelector('input[name="size"]:checked');
    const selectedToppings = Array.from(document.querySelectorAll('input[type="checkbox"]:checked'));

    if (!selectedIceCream || !selectedContainer || !selectedSize) {
        alert('Please select all required options.');
        return;
    }

    const orderDetails = {
        iceCream: selectedIceCream.value,
        container: selectedContainer.value,
        size: selectedSize.value,
        toppings: selectedToppings.map(topping => topping.value)
    };

    localStorage.setItem('orderDetails', JSON.stringify(orderDetails));
    window.location.href = 'checkout.html';
}

document.addEventListener('DOMContentLoaded', () => {
    const orderDetails = JSON.parse(localStorage.getItem('orderDetails'));
    if (!orderDetails) {
        alert('No order details found.');
        window.location.href = 'index.html';
        return;
    }

    const summaryText = `
        Ice Cream: ${orderDetails.iceCream}<br>
        Container: ${orderDetails.container}<br>
        Size: ${orderDetails.size}<br>
        Toppings: ${orderDetails.toppings.join(', ')}
    `;
    document.getElementById('summaryText').innerHTML = summaryText;

    const prices = {
        'Vanilla': 3.00,
        'Chocolate': 3.50,
        'Strawberry': 3.25,
        'Cone': 0.50,
        'Cup': 0.75,
        'Tub': 1.00,
        '25ml': 1.00,
        '50ml': 2.00,
        '250ml': 5.00,
        'Sprinkles': 0.25,
        'Nuts': 0.50,
        'Chocolate Syrup': 0.30
    };

    let totalPrice = prices[orderDetails.iceCream] + prices[orderDetails.container] + prices[orderDetails.size];
    orderDetails.toppings.forEach(topping => {
        totalPrice += prices[topping];
    });

    document.getElementById('totalPrice').innerText = totalPrice.toFixed(2);
});

function applyCoupon() {
    const couponCode = document.getElementById('couponCode').value;
    const totalPriceElement = document.getElementById('totalPrice');
    let totalPrice = parseFloat(totalPriceElement.innerText);

    if (couponCode === 'DISCOUNT10') {
        totalPrice *= 0.9;
    } else {
        alert('Invalid coupon code.');
        return;
    }

    totalPriceElement.innerText = totalPrice.toFixed(2);
}

function finalizeOrder() {
    alert('Order has been placed successfully!');
    localStorage.removeItem('orderDetails');
    window.location.href = 'index.html';
}