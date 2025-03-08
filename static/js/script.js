<script>
  // JavaScript code here
  document.addEventListener('DOMContentLoaded', function() {
      const containerSelect = document.getElementById('container');
      const scoopSizeGroup = document.getElementById('scoopSizeGroup');

      containerSelect.addEventListener('change', function() {
          if (this.value === 'cup') {
              scoopSizeGroup.style.display = 'block';
          } else {
              scoopSizeGroup.style.display = 'none';
          }
      });

      // Submit form after calculating total price
      const orderForm = document.getElementById('orderForm');
      orderForm.addEventListener('submit', function(event) {
          event.preventDefault();  // Prevent default form submission

          // Calculate total price
          calculateTotalPrice();

          // Submit the form
          this.submit();
      });

      // Function to calculate total price
      function calculateTotalPrice() {
          let totalPrice = 0;

          // Add container price
          const containerPrice = parseFloat(containerSelect.options[containerSelect.selectedIndex].text.split(' Rs ')[1]);
          totalPrice += containerPrice;

          // Add scoop size price if applicable
          if (scoopSizeGroup.style.display === 'block') {
              const scoopSizePrice = parseFloat(document.getElementById('scoopSize').value.split(' Rs ')[1]);
              totalPrice += scoopSizePrice;
          }

          // Add ice cream flavor price
          const flavorPrice = parseFloat(document.getElementById('flavor').value.split(' Rs ')[1]);
          totalPrice += flavorPrice;

          // Add toppings price if selected
          const toppingsSelect = document.getElementById('toppings');
          const toppingsPrice = parseFloat(toppingsSelect.options[toppingsSelect.selectedIndex].text.split(' Rs ')[1]);
          totalPrice += toppingsPrice;

          // Multiply by quantity
          const quantity = parseInt(document.getElementById('quantity').value);
          totalPrice *= quantity;

          // Display total price (if needed)
          console.log('Total Price:', totalPrice);  // For debugging
      }
  });
</script>