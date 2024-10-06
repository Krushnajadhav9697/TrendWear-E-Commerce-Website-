    function updateSubtotal(quantityInput){
        const row = quantityInput.closest('tr');
        const price = parseFloat(row.querySelector('td:nth-child(3)').textContent);
        const quantity = parseInt(quantityInput.value);
        const subtotal = price * quantity;
        row.querySelector('.subtotal').value=subtotal.toFixed(2);
        updateTotal();
    }
    function updateTotal(){
        let total =0;
        document.querySelectorAll('.subtotal').forEach(function(subtotalInput){
            total += parseFloat(subtotalInput.value);
        });

        const gst = total * 0.18;
        const invoiceTotal = total + gst;

        document.getElementById('total-value').textContent = total.toFixed(2);
        document.getElementById('gst-value').textContent=gst.toFixed(2);
        document.getElementById('invoice-total-value').textContent=invoiceTotal.toFixed(2);

    }
    updateTotal();

// Function to update the subtotal of an item
// function updateSubtotal(input) {
//     const quantity = parseInt(input.value) || 0;
//     const itemRow = input.closest('.cart-item');
//     const price = parseFloat(itemRow.querySelector('.cart-item-details p').textContent.replace('Price: ₹', '').trim());

//     const subtotal = quantity * price;
//     itemRow.querySelector('.subtotal-value').textContent = `₹${subtotal.toFixed(2)}`;

//     updateTotals();
// }

// // Function to update the total price, delivery fee, and invoice total
// function updateTotals() {
//     let total = 0;
//     document.querySelectorAll('.cart-item').forEach(item => {
//         const quantity = parseInt(item.querySelector('.quantity').value) || 0;
//         const price = parseFloat(item.querySelector('.cart-item-details p').textContent.replace('Price: ₹', '').trim());
//         total += quantity * price;
//     });

//     const deliveryFee = 0; // Set your delivery fee here
//     const gst = 0.18 * total; // Example: 18% GST
//     const invoiceTotal = total + gst + deliveryFee;

//     document.getElementById('total-value').textContent = total.toFixed(2);
//     document.getElementById('delivery-fee').textContent = deliveryFee.toFixed(2);
//     document.getElementById('invoice-total-value').textContent = invoiceTotal.toFixed(2);
// }

// // Add event listeners to quantity inputs
// document.querySelectorAll('.quantity').forEach(input => {
//     input.addEventListener('change', () => updateSubtotal(input));
// });

// // Initial update
// updateTotals();

// Function to update the subtotal of an item

// function updateSubtotal(input) {
//     const quantity = parseInt(input.value) || 0;
//     const itemRow = input.closest('.cart-item');
//     const price = parseFloat(itemRow.querySelector('.cart-item-details p').textContent.replace('Price: ₹', '').trim());

//     const subtotal = quantity * price;
//     itemRow.querySelector('.subtotal-value').textContent = `₹${subtotal.toFixed(2)}`;

//     updateTotals();
// }

// // Function to update the total price, delivery fee, and invoice total
// function updateTotals() {
//     let total = 0;
//     document.querySelectorAll('.cart-item').forEach(item => {
//         const quantity = parseInt(item.querySelector('.quantity').value) || 0;
//         const price = parseFloat(item.querySelector('.cart-item-details p').textContent.replace('Price: ₹', '').trim());
//         total += quantity * price;
//     });

//     const deliveryFee = 0; // Set your delivery fee here
//     const gst = 0.18 * total; // Example: 18% GST
//     const invoiceTotal = total + gst + deliveryFee;

//     document.getElementById('total-value').textContent = total.toFixed(2);
//     document.getElementById('delivery-fee').textContent = deliveryFee.toFixed(2);
//     document.getElementById('invoice-total-value').textContent = invoiceTotal.toFixed(2);
// }

// // Add event listeners to quantity inputs
// document.querySelectorAll('.quantity').forEach(input => {
//     input.addEventListener('change', () => updateSubtotal(input));
// });

// // Initial update
// updateTotals();

