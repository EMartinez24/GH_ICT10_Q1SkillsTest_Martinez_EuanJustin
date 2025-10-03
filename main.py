from pyscript import display, document

def create_order (e):
    option1 = document.getElementById('option1')
    option2 = document.getElementById('option2')
    option3 = document.getElementById('option3')
    option4 = document.getElementById('option4')
    option5 = document.getElementById('option5')
    name = document.getElementById('name').value
    address = document.getElementById('address').value
    number = document.getElementById('number').value
    
    total = (float(option1.value) * option1.checked + float(option2.value) * option2.checked + float(option3.value) * option3.checked + float(option4.value) * option4.checked + float(option5.value) * option5.checked)

    display(f'Order for: {name}', target='result')
    display(f'Address: {address}', target='result')
    display(f'Contact Number: {number}', target='result')
    display(f'₱ {total}', target='result')