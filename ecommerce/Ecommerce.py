import streamlit as st
import os
import time
import random
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

# Sample product data
products = [
    {"name": "Product 1", "price": 19.99, "image": "https://via.placeholder.com/150"},
    {"name": "Product 2", "price": 29.99, "image": "https://via.placeholder.com/150"},
    {"name": "Product 3", "price": 39.99, "image": "https://via.placeholder.com/150"},
]

# Sample coupon data
coupons = {
    "DISCOUNT10": 0.10,  # 10% discount
    "DISCOUNT20": 0.20,  # 20% discount
}

# Initialize session state for cart
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'discount' not in st.session_state:
    st.session_state.discount = 0.0

# Function to add item to the cart
def add_to_cart(product):
    st.session_state.cart.append(product)
    st.success(f"{product['name']} added to cart!")

# Function to remove item from the cart
def remove_from_cart(product):
    st.session_state.cart.remove(product)
    st.success(f"{product['name']} removed from cart!")

# Function to calculate total price in cart
def calculate_total():
    total = sum(item['price'] for item in st.session_state.cart)
    discount_amount = total * st.session_state.discount
    return total - discount_amount

# Function to apply coupon code
def apply_coupon(code):
    if code in coupons:
        st.session_state.discount = coupons[code]
        st.success(f"Coupon applied! You get a {st.session_state.discount * 100}% discount.")
    else:
        st.error("Invalid coupon code!")

# Function to simulate payment processing
def process_payment(method):
    # Simulate loading for 5 seconds
    with st.spinner("Processing your payment... Please wait."):
        time.sleep(5)  # Simulating processing time

    total_price = calculate_total()
    receipt = generate_receipt(total_price, method)
    
    st.success(f"Payment successful using {method}!")
    st.download_button("Download Receipt", receipt, "receipt.pdf")

# Function to generate PDF receipt
def generate_receipt(total_price, payment_method):
    # Sample data for the receipt
    data = [["Date", "Name", "Subscription", "Price (Rs.)"]]
    for item in st.session_state.cart:
        data.append([time.strftime("%d/%m/%Y"), item['name'], "Lifetime", f"{item['price']:.2f}"])
    data.append(["Sub Total", "", "", f"{sum(item['price'] for item in st.session_state.cart):.2f}"])
    data.append(["Discount", "", "", f"-{total_price * st.session_state.discount:.2f}"])
    data.append(["Total", "", "", f"{total_price:.2f}"])
    data.append(["Payment Method", "", "", payment_method])

    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=A4)
    
    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    title_style.alignment = 1

    title = Paragraph("Receipt", title_style)

    style = TableStyle([
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.lightgrey),
        ("BACKGROUND", (0, -2), (-1, -2), colors.lightgreen),
        ("BACKGROUND", (0, -1), (-1, -1), colors.lightcoral),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ])

    table = Table(data)
    table.setStyle(style)

    pdf.build([title, table])
    buffer.seek(0)

    return buffer

# Streamlit UI
st.title("E-commerce Application")

# Product Listing
st.subheader("Available Products")
for product in products:
    col1, col2, col3 = st.columns([2, 2, 1])
    
    with col1:
        st.image(product["image"], width=150)
    with col2:
        st.write(product["name"])
        st.write(f"${product['price']:.2f}")
    with col3:
        if st.button("Add to Cart", key=product["name"]):
            add_to_cart(product)

# Cart Section
st.subheader("Shopping Cart")
if st.session_state.cart:
    for item in st.session_state.cart:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(item['name'])
        with col2:
            if st.button("Remove", key=f'remove_{item["name"]}'):
                remove_from_cart(item)

    total_price = calculate_total()
    st.write(f"Total: ${total_price:.2f}")

    # Coupon Code Input
    coupon_code = st.text_input("Enter Coupon Code")
    if st.button("Apply Coupon"):
        apply_coupon(coupon_code)

    # Payment Options
    st.subheader("Payment Options")
    payment_method = st.radio("Select Payment Method:", ["Card", "Cash", "UPI"])

    if payment_method in ["Card", "UPI"]:
        # Generate a random QR code URL
        qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?data={random.randint(100000, 999999)}&size=150x150"
        st.image(qr_code_url, caption='Scan the QR code to pay', width=150)

        if st.button("Pay"):
            process_payment(payment_method)

    elif payment_method == "Cash":
        cash_amount = st.number_input("Enter Cash Amount", min_value=0.0, format="%.2f")
        if st.button("Pay with Cash"):
            if cash_amount < total_price:
                st.error("Cash amount is insufficient! Please enter a valid amount.")
            else:
                process_payment("Cash")

    # Clear Cart Button
    if st.button("Clear Cart"):
        st.session_state.cart = []
        st.session_state.discount = 0.0  # Reset discount
        st.success("Cart cleared!")
else:
    st.error("Your cart is empty! Please add some products to the cart.")
